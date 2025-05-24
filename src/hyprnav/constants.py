import os

# This is the version of the application.
APP_VERSION = "0.1.6"
# This is the name of the application.
APP_NAME = "hyprnav"

CONFIG_FILE = os.path.join(
    os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
)

STYLE_FILE = os.path.join(
    os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "style.css"
)

SPACES_DEFAULT = 20
