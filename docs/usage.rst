=====
Usage
=====

This section describes the usage of the ``esm_archiving`` tool. It can be used
from the command line, from other Python scripts, or as a plugin for the ESM
Infrastructure.

Command Line Interface
----------------------

.. automodule:: esm_archiving.cli
    :noindex:


Library Usage
-------------

To use ESM Archiving in a project::

    import esm_archiving

This gives you a few functions you can integrate into your Python programs.
They are documented in the API. Perhaps immediately useful are:

+ ``get_files_for_date_range``
+ ``sum_tar_lists``
+ ``split_list_due_to_size_limit``
+ ``pack_tarfile``
+ ``archive_mistral``

Plugin to ESM Runs
------------------

.. warning::
    This functionality is still under construction

The library described above can also be used as a plug-in to automatically
generate and upload tarballs as the simulation runs. Still under construction...
