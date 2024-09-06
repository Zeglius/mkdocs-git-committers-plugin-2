from mkdocs.config import config_options as c
from mkdocs.config.base import Config


class PluginConfig(Config):
    enterprise_hostname = c.Type(str, default="")
    gitlab_hostname = c.Type(str, default="")
    repository = c.Type(str, default="")
    gitlab_repository = c.Type(int, default=0)
    api_version = c.Type(str, default=None)
    branch = c.Type(str, default="master")
    docs_path = c.Type(str, default="docs/")
    enabled = c.Type(bool, default=True)
    cache_dir = c.Type(str, default=".cache/plugin/git-committers")
    exclude = c.Type(list, default=[])
    token = c.Type(str, default="")
