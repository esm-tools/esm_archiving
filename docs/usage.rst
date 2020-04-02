=====
Usage
=====

After installation, you have a new command in your path::

    esm_archive

Passing in the argument ``--help`` will show available subcommands::

   Usage: esm_archive [OPTIONS] COMMAND [ARGS]...

   Console script for esm_archiving.

    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.

    Commands:
      create
      upload

To use the tool, you can first ``create`` a tar archive and then use ``upload``
to put it onto the tape server.


Creating tarballs
-----------------

Use ``esm_archive create`` to generate tar files from an experiment::

    esm_archive create /path/to/top/of/experiment start_date end_date

The arguments ``start_date`` and ``end_date`` should take the form
``YYYY-MM-DD``. A complete example would be::

    esm_archive create /work/ab0246/a270077/from_ba0989/AWICM/LGM_6hours 1850-01-01 1851-01-01

The archiving tool will automatically pack up all files it finds matching these
dates in the ``outdata`` and ``restart`` directories and generate logs in the
top of the experiment folder. Note that the final date (1851-01-1 in this
example) is **not included**. During packing, you get a progress bar indicating
when the tarball is finished.


Uploading tarballs
------------------

A second command ``esm_archive upload`` allows you to put tarballs onto to tape server at DKRZ::

    esm_archive upload /path/to/top/of/experiment start_date end_date

The signature is the same as for the ``create`` subcommand. Note that for this
to work; you need to have a properly configured ``.netrc`` file in your home
directory::

    $ cat ~/.netrc
    machine tape.dkrz.de login a270077 password OMITTED

This file needs to be readable/writable **only** for you, e.g. ``chmod 700``.
The archiving program will then be able to automatically log into the tape
server and upload the tarballs.

=============
Library Usage
=============
To use ESM Archiving in a project::

    import esm_archiving

This gives you a few functions you can integrate into your Python programs.
They are documented in the API. Perhaps immediately useful are:

+ ``get_files_for_date_range``
+ ``sum_tar_lists``
+ ``split_list_due_to_size_limit``
+ ``pack_tarfile``
+ ``archive_mistral``

==================
Plugin to ESM Runs
==================

.. warning::
    This functionality is still under construction

The library described above can also be used as a plug-in to automatically
generate and upload tarballs as the simulation runs. Still under construction...
