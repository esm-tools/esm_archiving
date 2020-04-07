=======================
Configuring ESM Archive
=======================

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

1. Current working directory (As a hidden file)
2. Users ${HOME}/.config/esm_archiving
3. Users home folder (As a hidden file)
4. /etc/esm_archiving
5. Environmental Variable ESM_ARCHIVING_CONF

If nothing is found, the hard-coded defaults in ``esm_archiving/esm_archiving/config.py`` are used.
