import boto3
import json

s3 = boto3.client('s3')
project_name = "todo" # grab from the config object

def generate_policy():
    """Generates S3 bucket policy for a given project

    """
    policy = { } 
    policy = json.dumps(policy)
    s3.put_bucket_policy(Bucket=project_name, Policy=policy)


def static_hosting():
    """Sets up bucket to allow static hosting  

    """
    s3.put_bucket_website(
     Bucket=project_name,
     WebsiteConfiguration={
     'ErrorDocument': {'Key': 'error.html'},
     'IndexDocument': {'Suffix': 'index.html'},
    })
 