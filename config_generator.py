import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

load_dotenv()

# Load the templates from the "templates" directory
template_dir = "./nodecg/templates"
env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)

# Define your secrets
secrets = {
    # nodecg-speedcontrol.json
    "TWITCH_ID":os.environ.get("TWITCH_ID"),
    "TWITCH_SECRET":os.environ.get("TWITCH_SECRET"),
    "STREAM_TITLE":os.environ.get("STREAM_TITLE"),
    # nodecg.json
    "SESSION_SECRET":os.environ.get("SESSION_SECRET"),
    "AUTH_DISCORD_ID":os.environ.get("AUTH_DISCORD_ID"),
    "AUTH_DISCORD_SECRET":os.environ.get("AUTH_DISCORD_SECRET"),
    "AUTH_TWITCH_ID":os.environ.get("AUTH_TWITCH_ID"),
    "AUTH_TWITCH_SECRET":os.environ.get("AUTH_TWITCH_SECRET"),
    # speedcontrol-layouts.json
    "TILTIFY_ID":os.environ.get("TILTIFY_ID"),
    "TILTIFY_TOKEN":os.environ.get("TILTIFY_TOKEN"),
}

# Generate the configuration files
output_dir = "./nodecg/cfg"
os.makedirs(output_dir, exist_ok=True)

for template_filename in os.listdir(template_dir):
    template = env.get_template(template_filename)
    output_filename = os.path.join(output_dir, template_filename)
    rendered = template.render(secrets)
    
    with open(output_filename, "w") as f:
        f.write(rendered)
