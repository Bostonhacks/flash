import Configuration
import yaml

def read_config(project_dir):
    """Reads configuration file a given project
    Args:
       project_dir (str): string describing directory or project name
    Returns:
        config: returns a configuration class 
    """
    config = Configuration.Configuration()

    with open("config.flash", 'r') as ymlfile:
        input_config = yaml.load(ymlfile)

    config.set_project_dir(input_config['flash']['project'])
    config.set_aws_secret(input_config['flash']['secret'])
    config.set_project_type(input_config['flash']['type']) 
    config.set_remote_location(input_config['remote']['location'])


    return config