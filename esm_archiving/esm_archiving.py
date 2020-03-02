#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Author: Paul Gierz <pgierz>
# @Date:   2020-02-28T07:08:00+01:00
# @Email:  pgierz@awi.de
# @Filename: esm_archiving.py
# @Last modified by:   pgierz
# @Last modified time: 2020-03-02T11:55:49+01:00


"""Main module."""

import logging
import os
import re

# Third-Party Libraries:
import pandas as pd


def find_indices_of(char, in_string):
    """
    Finds indicies of a specific character in a string

    Parameters
    ----------
    char : str
        The character to look for
    in_string : str
        The string to look in

    Yields
    ------
    int
        Each round of the generator gives you the next index for the desired
        character.
    """
    index = -1
    while True:
        index = in_string.find(char, index + 1)
        if index == -1:
            break
        yield index


def group_indexes(index_list):
    """
    Splits indexes into tuples of monotonically ascending values.

    Parameters
    ----------
    list :
        The list to split up

    Returns
    -------
    list :
        A list of tuples, so that you can get only one group of ascending tuples.

    Example
    -------
    >>> indexes = [0, 1, 2, 3, 12, 13, 15, 16]
    >>> group_indexes(indexes)
    [(0, 1, 2, 3), (12, 13), (15, 16)]
    """
    rlist, group = [], []
    for idx, i in enumerate(index_list):
        group.append(i)
        try:
            if i + 1 != index_list[idx + 1]:
                rlist.append(tuple(group))
                group = []
        except IndexError:
            if idx == len(index_list) - 1:
                if i - 1 == index_list[idx - 1]:
                    rlist.append(tuple(group))
                else:
                    rlist.append((i,))
    return rlist


# PLAN
# Go through the experiment and determine the filetypes
# For each filetype, build file groups
def group_files(top, filetype):
    """
    Generates quasi-regexes for a specific filetype, replacing all numbers with #.

    Parameters
    ----------
    top : str
        Where to start looking (this should normally be top of the experiment)
    filetype : str
        Which files to go through (e.g. outdata, restart, etc...)

    Returns
    -------
    dict
        A dictonary containing keys for each folder found in ``filetype``, and
        values as lists of files with strings where numbers are replaced by #.
    """
    model_dirs = [
        model
        for model in os.listdir(os.path.join(top, filetype))
        if os.path.isdir(os.path.join(top, filetype, model))
    ]
    model_files = {model: None for model in model_dirs}
    for model_dir in model_dirs:
        cleaned_filepatterns = []
        for root, _, files in os.walk(os.path.join(top, filetype, model_dir)):
            for file in files:
                filepattern = "".join([r"#" if c.isdigit() else c for c in file])
                filepattern = os.path.join(root, filepattern)
                if filepattern not in cleaned_filepatterns:
                    cleaned_filepatterns.append(filepattern)
        model_files[model_dir] = cleaned_filepatterns
    return model_files


def purify_expid_in(model_files, expid, restore=False):
    """
    Puts or restores >>>EXPID<<< marker in filepatterns

    Parameters
    ----------
    model_files : dict
        The model files for archiving
    expid : str
        The experiment ID to purify or restore
    restore : bool
        Set experiment ID back from the temporary marker

    Returns
    -------
    dict :
        Dictionary containing keys for each model, values for file patterns
    """
    for model in model_files:
        for idx, filepattern in enumerate(model_files[model]):
            try:
                if restore:
                    new_filepattern = filepattern.replace(">>>EXPID<<<", expid)
                else:
                    new_filepattern = filepattern.replace(expid, ">>>EXPID<<<")
                model_files[model][idx] = new_filepattern
            except:
                logging.debug("Can't replace experiment id for: %s", filepattern)
    return model_files


def stamp_files(model_files):
    for model in model_files:
        for idx, filepattern in enumerate(model_files[model]):
            try:
                stamped_filepattern = stamp_filepattern(filepattern)
                model_files[model][idx] = stamped_filepattern
            except:
                logging.debug("Can't stamp file: %s", filepattern)
    return model_files


def get_list_from_filepattern(filepattern):
    dirname = os.path.dirname(filepattern)
    files = os.listdir(dirname)
    regex_files = re.compile(os.path.basename(filepattern).replace("#", "\d"))
    matching_files = sorted(
        [
            os.path.join(dirname, file)
            for file in os.listdir(dirname)
            if re.match(regex_files, file)
        ]
    )
    return matching_files


def stamp_filepattern(filepattern):
    """
    Transforms # in filepatterns to >>>DATE<<< and replaces other numbers back to original

    Parameters
    ----------
    filepattern : str
        Filepattern to get date stamps for

    Returns
    -------
    str :
        New filepattern, with >>>DATE<<<
    """
    # Get full file list:
    matching_files = get_list_from_filepattern(filepattern)
    datestamp_location = determine_datestamp_location(matching_files)
    files = [f.replace(f[datestamp_location], ">>>DATE<<<") for f in matching_files]
    files = set(files)
    try:
        assert len(files) == 1
    except AssertionError:
        print(files)
        raise
    filepattern = files.pop()
    return filepattern


# Figure out where the datestamp is in the file pattern
def determine_potential_datestamp_locations(filepattern):
    """
    For a filepattern, gives back index of potential date locations

    Parameters
    ----------
    filepattern : str
        The filepattern to check.

    Returns
    -------
    list :
        A list of slice object which you can use to cut out dates from the filepattern
    """
    indexes = list(
        find_indices_of("#", "".join([r"#" if c.isdigit() else c for c in filepattern]))
    )

    aligned_indexes = []
    if indexes[0] + 1 == indexes[1]:
        aligned_indexes.append(0)
    for idx, i in enumerate(indexes[1:-1]):
        idx += 1
        expected_previous = i - 1
        expected_next = i + 1
        if (indexes[idx + 1] == expected_next) or (
            indexes[idx - 1] == expected_previous
        ):
            aligned_indexes.append(i)
    if indexes[-1] - 1 == indexes[-2]:
        aligned_indexes.append(indexes[-1])

    grouped_indexes = group_indexes(aligned_indexes)

    slices = []
    for group in grouped_indexes:
        slices.append(slice(group[0], group[-1] + 1))
    return slices


def determine_datestamp_location(files):
    """
    Given a list of files; figures where the datestamp is by checking if it varies.

    Parameters
    ----------
    files : list
        A list (longer than 1!) of files to check

    Returns
    -------
    slice :
        A slice object giving the location of the datestamp

    Raises
    ------
    LookupError :
        Raised if there is more than one slice found where the numbers vary over
        different files

    AssertionError :
        If the length of the file list is not longer than 1.
    """
    assert len(files) > 1
    filepattern = files[0]  # Use the first file as a template (Probably a bad idea)
    slices = determine_potential_datestamp_locations(filepattern)
    valid_slices = []
    for slice_ in slices:
        if files[0][slice_] == files[1][slice_]:
            continue
        else:
            valid_slices.append(slice_)
    if len(valid_slices) > 1:
        raise LookupError("Unable to determine a unique datestamp!")
    return valid_slices[0]


# Build a regex to go through a certain number of dates (e.g. 1 decade)
def get_files_for_date_range(
    filepattern, start_date, stop_date, frequency, date_format=r"%Y%m%d"
):
    """
    Creates a list of files for specified start/stop dates

    Parameters
    ----------
    filepattern : str
        A filepattern to replace dates in
    start_date : str
        The starting date, in a pandas-friendly date format
    stop_date : str
        Ending date, pandas friendly. Note that for end dates, you need to **add
        one month** to assure that you get the last step in your list!
    frequency : str
        Frequency of dates, pandas friendly
    date_format : str
        How dates should be formatted, defaults to %Y%m%d

    Returns
    -------
    list
        A list of strings for the filepattern with correct date stamps.

    Example
    -------
    >>> filepattern =  "LGM_24hourly_PMIP4_echam6_BOT_mm_>>>DATE<<<.nc"
    >>> get_files_for_date_range(filepattern, "1890-07", "1891-11", "1M", date_format="%Y%m")
    [
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189007.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189008.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189009.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189010.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189011.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189012.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189101.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189102.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189103.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189104.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189105.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189106.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189107.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189108.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189109.nc",
        "LGM_24hourly_PMIP4_echam6_BOT_mm_189110.nc",
    ]
    """
    # I had initially wanted to do a regex for this; but I get the impression
    # that's a horrible idea. Or at least, a difficult one. If we know the date
    # format, we can just build a list of the desired dates.

    # BUG: determine_datestamp_location takes a list, not a string!!!
    date_stamp = ">>>DATE<<<"
    dates = [
        date.to_pydatetime().strftime(date_format)
        for date in pd.date_range(start=start_date, end=stop_date, freq=frequency)
    ]
    files = [filepattern.replace(date_stamp, str(date)) for date in dates]
    return files


# Sort the files into lists dependening on the dates
def sort_files_to_tarlists(model_files, start_date, end_date, config):
    out_lists = {}
    for model in model_files:
        frequency = config[model]["frequency"]
        out_lists[model] = []
        for filepattern in model_files[model]:
            out_lists[model].append(
                get_files_for_date_range(filepattern, start_date, end_date, frequency)
            )
    return out_lists


# Check size of all files in each list
# Pack the files into tarball(s), depending on the size of the list
# Perform an integrity check
# Write a small log of what is in that tarball
# Upload the tarball to the tape
# If requested, delete the original data
