import boto3
import os 

s3 = boto3.client('s3')
files = get_files('.')
project_dir = "grab info from config"

def upload_files(files):
    for file in files:
        upload = open(file)
        s3.put_object(  Body=upload,
                        Bucket=project_dir,
                        Key=file,
                        ContentType='text/html' )


def get_files(project_dir):
    """Reads configuration file a given project
    Args:
       project_dir (str): string describing directory or project name
    Returns:
        files: returns a list of files to push to the s3 bucket
    """
    return []

files = get_files(project_dir)

 
