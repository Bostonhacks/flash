class Configuration():
    """Stores the data from the .flash file genereted by the user

    Attributes:
        project_dir (str): project name or directory.
        aws_secret (str): key to use aws cli.

    """
    def __init__(self):
        self.project_name = ''
        self.aws_access_key = ''
        self.aws_secret = ''
        self.project_type = ''

    def set_project_name(self, project_name):
        self.project_name = project_name

    def get_project_dir(self):
        return self.project_name

    def set_aws_access_key(self, key):
        self.aws_access_key = key

    def get_aws_access_key(self):
        return self.aws_access_key

    def set_aws_secret(self, secret):
        self.aws_secret = secret

    def get_aws_secret(self):
        return self.aws_secret

    def set_project_type(self, project_type):
        self.project_type = project_type

    def get_project_type(self):
        return self.project_type
