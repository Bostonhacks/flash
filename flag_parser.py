import argparse


def parse_input():
    """Parses flags from the command line
    Returns:
        str: returns the project directory  or the name of the directory 
    """
    flag_parser = setup_parser()
    arguments = flag_parser.parse_args()
    project_dir = arguments.projectdir
    return project_dir[0]

def setup_parser():
    """Sets up flag parser
    Returns:
        parser: returns a flag parser
    """
    flag_parser = argparse.ArgumentParser(description='Deployments in <2 minutes')
    flag_parser.add_argument('-d', nargs=1, dest='projectdir', help='deploying a dynamic project to remote location')
    flag_parser.add_argument('-s', nargs=1, dest='projectdir', help='serving a static project to a remote location')
    flag_parser.add_argument('-t', nargs=1, dest="projectdir", help='Run tests on project')
    return flag_parser