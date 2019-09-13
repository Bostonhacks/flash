import boto3
import json
from helpers.helpers import *
import os

class StaticHandler:
    def __init__(self, config):
        self.boto_client =  boto3.client(
            's3',
            aws_access_key_id=config.get_aws_access_key(),
            aws_secret_access_key=config.get_aws_secret(),
            region_name='us-east-1' # assume northeastern region, can customize later
        )
        self.project_name = config.project_name
        self.bucket_name = self.generate_bucket_name()

    def create_bucket(self):
        try:
            bucket_response = self.boto_client.create_bucket(Bucket=self.bucket_name)
            print(self.bucket_name)
            print(bucket_response)
        except Exception as e:
            print(e)
            return False
        return True

    # Applies Bucket Policy
    # default public policy 
    # Reference link: https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html
    def set_public_policy(self):
        # Default public policy
        policy = {
            "Version":"2012-10-17",
            "Statement":[
                {
                "Sid":"AddPerm",
                "Effect":"Allow",
                "Principal": "*",
                "Action":["s3:GetObject"],
                "Resource":["arn:aws:s3:::" + self.bucket_name + "/*"]
                }
            ]
        }
        # Converts policy into a json and puts into the S3 bucket
        try:
            policy = json.dumps(policy)
            self.boto_client.put_bucket_policy(
                Bucket=self.bucket_name,
                Policy=policy
            )
        except Exception as e:
            print(e)
            return False
        return True


    def upload_files(self, path):
        """ Upload all files in directory to s3 bucket """
        # preprocess path to make sure there is a '/' at the end
        if path[-1] != "/":
            path += "/"

        # traverse through all the files in the directory and upload to s3 bucket
        try:
            for root, dirs, files in os.walk(path):
                for name in files:
                    file_path = os.path.join(root, name)
                    s3_file_path = remove_prefix(file_path, path)
                    print(s3_file_path)
                    # manually set content_type for s3 objects, otherwise it's default to binary/octet-stream
                    content_type = get_content_type(s3_file_path)

                    print("Uploading: ", s3_file_path, "with content_type", content_type)                    
                    self.boto_client.upload_file(file_path, self.bucket_name, s3_file_path, ExtraArgs={'ContentType': content_type})
        except ClientError as e:
            print(e)
            return False
        return True

    def generate_bucket_name(self):
        """ generate a (hopefully) unique name for s3 bucket from project name """
        # id = sum of ascii values of characters in project_name
        return ''.join([self.project_name, '-', str(sum([ord(c) for c in self.project_name]))])


    def configure_website_hosting(self):
        """ Configuring the bucket for Static Website Usage """
        try:
            self.boto_client.put_bucket_website(
                Bucket=self.bucket_name, 
                WebsiteConfiguration = {
                    # default index and error used for now
                    'ErrorDocument': {'Key': "error.html"},
                    'IndexDocument': {'Suffix': "index.html"},
                }
            )
        except Exception as e:
            print(e)
            return False
        return True