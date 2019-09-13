from config import config
from config import generate
from static.StaticHandler import StaticHandler

generate.generate_config()
config = config.read_config("firstprojectflash") # dummy name

# If project_type is static, call the following functions.
if config.project_type == "static":
    bucket = StaticHandler(config)
    bucket.create_bucket() 
    bucket.set_public_policy()
    bucket.configure_website_hosting()
    bucket.upload_files("./upload")
