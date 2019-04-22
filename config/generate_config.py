"""
format for flash file
flash:
    directory: flash
    type: dynamic
    secret: shhhhh
    db: write-math
remote:
    location: www.bostonhacks.io
    prod: true/false
    circle: yes
"""

project_dir = ''
project_type = ''
project_secret = ''
remote_location = ''

def generate_config():
    project_dir = input("What's your project name/directory?")
    project_type = input("What kind of project is this (static or dynamic)?")
    project_secret = input("Paste your AWS secret here")
    
    string_format = "\n+\t"
    flash = open(project_dir+'.flash', 'w')
    flash.write("flash:"+string_format)
    flash.write("directory: "+project_dir+string_format)
    flash.write("type: "+project_type+string_format)
    flash.write("secret: "+project_secret)


generate_config()