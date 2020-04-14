"""
When run from either the command line or in library mode (note **not** as an
ESM Plugin), ``esm_archiving`` can be configured to how it looks for specific
files. The configuration file is called ``esm_archiving_config``, should be
written in YAML, and have the following format::

    echam:  # The model name
        archive: # archive seperator **required**
            # Frequency specification (how often
            # a datestamp is generated to look for)
            frequency: "1M"
            # Date format specification
            date_format: "%Y%m"


By default, ``esm_archive`` looks in the following locations:

    1. Current working directory
    2. Any files in the XDG Standard:
        https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html


Note that the default configuration is hard coded in
``esm_archiving/esm_archiving/config.py``
"""
import os

from xdgenvpy import XDGPedanticPackage
import yaml

# Add XDG Standard
xdg = XDGPedanticPackage("esm_archiving")
config_dirs = xdg.XDG_CONFIG_DIRS.split(":")
config_dirs = [l + "/esm_archiving" for l in config_dirs]
config_dirs.insert(0, os.curdir)

# Defaults:
CONFIG_FNAME = "esm_archiving_config"
DEFAULT_CONFIG = {
    "echam": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "jsbach": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "hdmodel": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "fesom": {"archive": {"frequency": "1Y", "date_format": "%Y%m"}},
    "oasis3mct": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    "general": {"database_file": xdg.XDG_DATA_HOME+"/esm_archiving.db"},
}



def load_config():
    """
    Loads the configuration from one of the default configuration directories.
    If none can be found, returns the hard-coded default configuration.

    Returns
    -------
    dict
        A representation of the configuration used for archiving.
    """
    for loc in config_dirs:
        read_config_fname = CONFIG_FNAME
        try:
            with open(os.path.join(loc, read_config_fname)) as source:
                config = yaml.load(source, Loader=yaml.FullLoader)
                return config
        except IOError:
            pass
    return DEFAULT_CONFIG
