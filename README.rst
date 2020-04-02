=============
ESM Archiving
=============


.. image:: https://gitlab.awi.de/esm_tools/esm_archiving/badges/master/pipeline.svg
        :target: https://gitlab.awi.de/esm_tools/esm_archiving/commits/master

.. image:: https://readthedocs.org/projects/esm-archiving/badge/?version=latest
        :target: https://esm-archiving.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




ESM Archiving gives you modern tools for putting your run on the tape


* Free software: GNU General Public License v3
* Documentation: https://esm-archiving.readthedocs.io.


Installing
----------

Run the following::

    pip install git+https://gitlab.awi.de/esm_tools/esm_archiving

Usage
-----

Once installed, you get the new binary ``esm_archiving``. You can generate tarballs for a standard run::

    esm_archiving create /path/to/exp 1860-01-01 1870-01-01

Then upload to the tape server::

    esm_archiving upload /path/to/exp 1860-01-01 1870-01-01

For more detailed descriptions, see the documentation.


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

