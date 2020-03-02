# -*- coding: utf-8 -*-

"""Console script for esm_archiving."""
import sys
import os
import click
import pprint



from .esm_archiving import *




pp = pprint.PrettyPrinter(width=41, compact=True)


@click.group()
@click.version_option()
def main(args=None):
    """Console script for esm_archiving."""
    click.echo("Replace this message by putting your code into "
               "esm_archiving.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0

@main.command()
@click.argument("base_dir")
@click.argument("filetype")
@click.argument("start_date")
@click.argument("end_date")
def create_archive(base_dir, filetype, start_date, end_date):
    click.secho("Creating archives for:", color="green")
    click.secho(base_dir, color="green")
    click.secho("File: %s" % filetype, color="green")
    click.secho("From: %s" % start_date, color="green")
    click.secho("To: %s" % end_date, color="green")
    files = group_files(base_dir, filetype)
    files = stamp_files(files)

    config = {
            "echam": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
        "jsbach": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
        "hdmodel": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
        "fesom": {"archive": {"frequency": "1Y", "date_format": "%Y%m"}},
        "oasis3mct": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
    }

    files = sort_files_to_tarlists(files, start_date, end_date, config)
    pp.pprint(files)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
