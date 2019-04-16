class Configuration():
    """Stores the data from the .flash file genereted by the user

    Attributes:
        project_dir (str): project name or directory.
        aws_secret (str): key to use aws cli.

    """
    project_dir = ''
    aws_secret = ''
    project_type = ''
    remote_location = ''

    def __init__(self):
        pass

    def set_project_dir(self, project_dir):
        self.project_dir = project_dir

    def get_project_dir(self):
        return self.project_dir

    def set_aws_secret(self, secret):
        self.aws_secret = secret

    def get_aws_secret(self):
        return self.aws_secret

    def set_project_type(self, project_type):
        self.project_type = project_type

    def get_project_type(self):
        return self.project_type

    def set_remote_location(self, location):
        self.remote_location = location

    def get_remote_location(self):
        return self.remote_location