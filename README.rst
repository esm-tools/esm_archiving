=============
ESM Archiving
=============


.. image:: https://gitlab.awi.de/esm_tools/esm_archiving/badges/master/pipeline.svg
        :target: https://gitlab.awi.de/esm_tools/esm_archiving/commits/master

.. image:: https://readthedocs.org/projects/esm-archiving/badge/?version=latest
        :target: https://esm-archiving.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




ESM Archiving gives you modern tools for putting your run on the tape

This project helps you in uploading and downloading your simulations to a tape
archive. It provides the command ``esm_archive`` which can be used to generate,
upload, and retrieve simulation archives in the form of zipped tarballs.
Additionally, it provides a plug-in functionality for the ``esm_runscripts``
tool; allowing you to create archives while your simulations runs. As the
project is written in Python, any of the functionality can also be embedded in
other scripts.


Installing
----------

Run the following::

    # Set up a modern git and python environment:
    # Maybe needed on some machines:
    module load git
    module load python3
    # Install the archive project:
    pip install git+https://github.com/esm-tools/esm_archiving

Usage
-----

Once installed, you get the new binary ``esm_archiving``. You can generate tarballs for a standard run::

    esm_archive create /path/to/exp 1860-01-01 1870-01-01

Then upload to the tape server::

    esm_archive upload /path/to/exp 1860-01-01 1870-01-01

For more detailed descriptions, see the documentation.

Roadmap
-------

There are a few issues which shows what is planned for the near future:

* Support for ``hssrv2.awi.de`` tape archive
* Download and unpack functionality
* Integrity checks for the tarballs

Please feel free to add to the list by opening an issue with the tag 

Benchmarked Tests
-----------------

``esm_archiving`` is tested against a few standard runs to ensure everything
works smoothly. The table below shows which experiments are tested

Please note that currently, the benchmark run is still in production. Automatic
testing will resume once the data are available.

+-----------------------------+-----------------------+------------+
| Experiment                  | ESM Runscript Version | Model      |
+-----------------------------+-----------------------+------------+
| ``AWIESM1.1_benchmark_001`` | ?                     | AWIESM 1.1 |
+-----------------------------+-----------------------+------------+

