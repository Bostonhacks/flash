"""
format for flash file
flash:
    name: flash
    type: dynamic
    secret: shhhhh
    db: write-math
remote:
    location: www.bostonhacks.io
    prod: true/false
    circle: yes
"""

project_name = ''
project_type = ''
project_secret = ''
remote_location = ''

def generate_config():
    project_name = input("What's your project name? ")
    project_type = input("What kind of project is this (static or dynamic)? ")
    project_access_key = input("Paste your AWS access key here ")
    project_secret = input("Paste your AWS secret here ")
    remote_location = input("If this is a static site, please put the name of the bucket, else the name of the EC2 ")

    string_format = "\n    "
    flash = open(project_name+'.flash', 'w')
    flash.write("flash: ")
    flash.write(string_format+"name: "+project_name)
    flash.write(string_format+"type: "+project_type)
    flash.write(string_format+"access_key: "+project_access_key)
    flash.write(string_format+"secret: "+project_secret)
    flash.write("\nremote: ")
    flash.write(string_format+"location: "+remote_location)
    flash.close()


def verify_config(project_name):
    pass