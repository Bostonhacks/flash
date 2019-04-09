class Configuration:
    """Stores the data from the .flash file genereted by the user

    Attributes:
        project_dir (str): project name or directory.
        aws_secret (str): key to use aws cli.

    """
    project_dir = ''
    aws_secret = ''

    def __init__(self):
        pass

    def set_project_dir(self, project_dir):
        pass

    def get_project_dir(self):
        return self.project_dir
