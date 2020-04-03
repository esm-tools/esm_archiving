"""
This contains the default configuration used in esm_archiving. If possible, it
is read from a file .esm_archiving_config. The configuration can be over-ridden
in the following locations:

    1. Current working directory (As a hidden file)
    2. Users ${HOME}/.config/esm_archiving
    3. Users home folder (As a hidden file)
    4. /etc/esm_archiving
    5. Environmental Variable ESM_ARCHIVING_CONF

The configuration file should in the YAML format. As an example:

.. code::
    echam:  # The model name
        archive: # archive seperator **required**
            frequency: "1M" # Frequency specification
            date_format: "%Y%m" # Date format specification
"""
import os
import yaml




# Defaults:
CONFIG_FNAME = "esm_archiving_config"
DEFAULT_CONFIG = {
    "echam": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "jsbach": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "hdmodel": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "fesom": {"archive": {"frequency": "1Y", "date_format": "%Y%m"}},
    "oasis3mct": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
}

def load_config():
    for loc, hidden in zip(
        [
            os.curdir,
            os.path.join(os.path.expanduser("~"), ".config", "esm_archiving"),
            os.path.expanduser("~"),
            "/etc/esm_archiving",
            os.environ.get("ESM_ARCHIVING_CONF"),
        ],
        [True, False, True, False, False,],
    ):
        if hidden:
            read_config_fname = "." + CONFIG_FNAME
        else:
            read_config_fname = CONFIG_FNAME
        try:
            with open(os.path.join(loc, read_config_fname)) as source:
                config = yaml.load(source, Loader=yaml.FullLoader)
                return config
        except IOError:
            pass
    return DEFAULT_CONFIG
