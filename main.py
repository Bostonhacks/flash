from config import config
from config import generate


generate.generate_config()
config.read_config("flash")