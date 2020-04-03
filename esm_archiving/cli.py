#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for esm_archiving."""
import sys
import os
import pprint

import click
import emoji

from .esm_archiving import (
    archive_mistral,
    check_tar_lists,
    group_files,
    pack_tarfile,
    sort_files_to_tarlists,
    stamp_files,
    sum_tar_lists_human_readable,
)

from .config import load_config

pp = pprint.PrettyPrinter(width=41, compact=True)
config = load_config()


@click.group()
@click.version_option()
def main(args=None):
    """Console script for esm_archiving."""
    return 0


@main.command()
@click.argument("base_dir")
@click.argument("start_date")
@click.argument("end_date")
@click.option("--force", is_flag=True)
@click.option("--interactive", is_flag=True)
def create(base_dir, start_date, end_date, force, interactive):
    click.secho(
        emoji.emojize(":file_cabinet:") + " Creating archives for:", color="green"
    )
    click.secho(base_dir, color="green")
    click.secho("From: %s" % start_date, color="green")
    click.secho("To: %s" % end_date, color="green")
    for filetype in ["outdata", "restart"]:
        files = group_files(base_dir, filetype)
        files = stamp_files(files)

        files = sort_files_to_tarlists(files, start_date, end_date, config)
        existing, missing = check_tar_lists(files)
        if interactive:
            click.secho("The following files were requested and found:")
            pp.pprint(existing)
            pp.pprint(sum_tar_lists_human_readable(existing))
        if missing:
            if interactive:
                click.secho("The following files were requested but missing:")
                pp.pprint(missing)
        for model in files:
            click.secho(
                emoji.emojize(":open_file_folder: --> :package:", use_aliases=True)
                + f" Packing up files for {model} ({filetype})"
            )
            archive_name = os.path.join(
                base_dir, f"{model}_{filetype}_{start_date}_{end_date}.tgz"
            )
            click.secho(archive_name)
            out_fname = pack_tarfile(existing[model], base_dir, archive_name)


@main.command()
@click.argument("base_dir")
@click.argument("start_date")
@click.argument("end_date")
def upload(base_dir, start_date, end_date):
    # Try to make the Pftp object before anything else happens to ensure that
    # that at least works...

    click.secho(" Uploading archives for:")
    click.secho(base_dir)

    for filetype in ["outdata", "restart"]:
        files = group_files(base_dir, filetype)
        files = stamp_files(files)

        files = sort_files_to_tarlists(files, start_date, end_date, config)

        for model in files:
            archive_name = os.path.join(
                base_dir, f"{model}_{filetype}_{start_date}_{end_date}.tgz"
            )
            remote_archive_name = archive_name.replace(base_dir, remote_base_dir)
            archive_mistral(archive_name, remote_archive_name)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
