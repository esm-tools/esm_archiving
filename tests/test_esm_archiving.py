# @Author: Paul Gierz <pgierz>
# @Date:   2020-02-28T07:08:00+01:00
# @Email:  pgierz@awi.de
# @Filename: test_esm_archiving.py
# @Last modified by:   pgierz
# @Last modified time: 2020-03-02T10:00:06+01:00


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `esm_archiving` package."""


import unittest
from click.testing import CliRunner

from esm_archiving import esm_archiving
from esm_archiving import cli


class TestEsm_archiving(unittest.TestCase):
    """Tests for `esm_archiving` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert "esm_archiving.cli.main" in result.output
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output

    def test_find_indicies(self):
        """Checks if find_indices_of can find # correctly"""
        test_str = "abc#e#f"
        gen = esm_archiving.find_indices_of("#", test_str)
        out = list(gen)
        self.assertEqual([3, 5], out)

    def test_group_indexes(self):
        """Groups indexes into connected monotonically ascending tuples"""
        test_input = [0, 1, 2, 3, 12, 13, 15, 16]
        expected_output = [(0, 1, 2, 3), (12, 13), (15, 16)]
        actual_output = esm_archiving.group_indexes(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_group_indexes_seperate_back(self):
        """Checks group indexes if the last value is on it's own"""
        test_input = [0, 1, 2, 3, 12, 13, 15, 16, 19]
        expected_output = [(0, 1, 2, 3), (12, 13), (15, 16), (19,)]
        actual_output = esm_archiving.group_indexes(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_datestamp_location(self):
        test_files = [
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
        slice_ = esm_archiving.determine_datestamp_location(test_files)
        self.assertEqual(slice_, slice(33, 39))

    def test_get_files_for_date_range(self):
        test_files = [
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
        out_files = esm_archiving.get_files_for_date_range(
            "LGM_24hourly_PMIP4_echam6_BOT_mm_>>>DATE<<<.nc",
            "1890-07",
            "1891-11",
            "1M",
            date_format="%Y%m",
        )
        self.assertEqual(out_files, test_files)
