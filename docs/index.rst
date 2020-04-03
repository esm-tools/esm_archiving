Welcome to ESM Archiving's documentation!
=========================================

This project facilitates uploading and downloading your simulations to a tape
archive. It provides the command ``esm_archive`` which can be used to generate,
upload, and retrieve simulation archives in the form of zipped tarballs.
Additionally, it provides a plug-in functionality for the ``esm_runscripts``
tool; allowing you to create archives while your simulations runs. As the
project is written in Python, any of the functionality can also be embedded in
othere scripts.

See the installation guide for full instructions, but to get up and running,
you can do::

    # Set up a modern git and python environment:
    # Maybe needed on some machines:
    module load git
    module load python3
    # Install the archive project:
    pip install git+https://gitlab.awi.de/esm_tools/esm_archiving.git


Now, you can use ``esm_archive --help`` to get started with the command line
interface. To create an archive::

    esm_archive create /path/to/experiment start_date end_date

To upload::

    esm_archive upload /path/to/experiment start_date end_date


The next page is a quickstart. More information can be found in the usage
section.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   usage
   configuration
   modules
   authors
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
