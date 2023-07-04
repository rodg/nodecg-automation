# Nodecg Automation

This is a template for creating a continuously delivered nodecg dashboard for speedrun marathons.

## Usage

1. Create your own repository from this template. Make it a private repository if you plan to have any sensitive info stored.
2. Edit `config/values.yaml` with your domain info. For the most basic setup you only need to fill in the `dashboard` info.
3. Edit the env vars at the top of `.github/workflow/publish-to-ecr.yml` to match where you wish to publish stuff and what you want to call it.
4. [Create an access token for DigitalOcean](https://docs.digitalocean.com/reference/api/create-personal-access-token/). Name it `DIGITALOCEAN_ACCESS_TOKEN`
   1. You can modify this repo to use other cloud providers or run locally, but it'll take more effort.
5. Drop any bundles you want into `nodecg/bundles`. These are included in the container. They must be fully built and ready to run.
6. Modify and add any configs in the `nodecg/templates` folder. These are run through jinja2 using the `config_generator.py` script to include secrets from a secret called `ENV_FILE`. The expected secrets for some basic marathon things is in `example.env`.
   1. You might have to modify `config_generator.py` to have it run nicely if you add/remove secrets.
7. Push your changes to your repo, if all goes well it should automatically build and deploy the changes.
