# -*- coding: utf-8 -*-

"""Console script for esm_archiving."""
import sys
import os
import click
import pprint


from .esm_archiving import (
    check_tar_lists,
    group_files,
    pack_tarfile,
    sort_files_to_tarlists,
    stamp_files,
    sum_tar_lists_human_readable,
)


pp = pprint.PrettyPrinter(width=41, compact=True)


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
    click.secho("Creating archives for:", color="green")
    click.secho(base_dir, color="green")
    for filetype in ["outdata", "restart"]:
        click.secho("File: %s" % filetype, color="green")
        click.secho("From: %s" % start_date, color="green")
        click.secho("To: %s" % end_date, color="green")
        files = group_files(base_dir, filetype)
        files = stamp_files(files)

        # TODO: Remove this; it needs to be automatically found or asked for:
        config = {
            "echam": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
            "jsbach": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
            "hdmodel": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
            "fesom": {"archive": {"frequency": "1Y", "date_format": "%Y%m"}},
            "oasis3mct": {"archive": {"frequency": "1M", "date_format": "%Y%m"}},
        }

        files = sort_files_to_tarlists(files, start_date, end_date, config)
        existing, missing = check_tar_lists(files)
        click.secho("The following files were requested and found:")
        pp.pprint(existing)
        pp.pprint(sum_tar_lists_human_readable(existing))
        if interactive:
            pass
        if not force:
            input("Press Enter to continue...")
        if missing:
            click.secho("The following files were requested but missing:")
            pp.pprint(missing)
            if interactive:
                pass
            if not force:
                input("Press Enter to continue...")
        for model in files:
            click.secho(f"Generating archive for {model} {filetype}")
            archive_name = os.path.join(base_dir, f"{model}_{filetype}_{start_date}_{end_date}.tgz")
            click.secho(archive_name)
            input("Press Enter to continue...")
            out_fname = pack_tarfile(existing[model], archive_name)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
