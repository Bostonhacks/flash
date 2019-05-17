from config import Configuration
import yaml

def read_config(project_name):
    """Reads configuration file a given project
    Args:
       project_dir (str): string describing directory or project name
    Returns:
        config: returns a configuration class 
    """
    config = Configuration.Configuration()

    with open(project_name+".flash", 'r') as flash:
        input_config = yaml.safe_load(flash)


    config.set_project_name(input_config['flash']['name'])
    config.set_aws_secret(input_config['flash']['secret'])
    config.set_project_type(input_config['flash']['type']) 
    config.set_remote_location(input_config['remote']['location'])


    return config