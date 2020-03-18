#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `esm_archiving` package."""

# Standard Library
import os
import pickle

# import unittest

# Third-Party
from click.testing import CliRunner
from pyfakefs.fake_filesystem_unittest import TestCase

# This module
from esm_archiving import esm_archiving
from esm_archiving import cli


class TestESM_archiving_fakefs(TestCase):
    # TODO: Make this setUpClass
    def setUp(self):
        """Set up test fixtures, if any."""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        test_walk_file = os.path.join(dir_path, "exp_walk.dat")
        with open(test_walk_file, "rb") as f:
            rvalue = pickle.load(f)
        self.setUpPyfakefs()
        for root, dirs, files in rvalue:
            for dir_ in dirs:
                # Skip post dirs
                if dir_.startswith("post"):
                    continue
                os.makedirs(os.path.join(root, dir_))
            for file in files:
                self.fs.create_file(os.path.join(root, file))

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_walk_through_model_dir(self):
        """
        Checks if walking through a modeltype file directory for a specific
        model can clean numbers correctly.
        """

        grouped_files = esm_archiving._walk_through_model_dir_clean_numbers(
            "./AWIESM1.1_benchmark_001/outdata/echam"
        )

        expected_answer = [
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_co#_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam#hrpt_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamdaymax_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam#hrpt_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_tdiagmon_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_accw_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_ma_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echammon_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeropt#hrpt_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_co#_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiagmon_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_tdiagday_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_LOG_mm_######.nc",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_BOT_mm_######.nc",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam#hr_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeroptday_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiagmon_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamday_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_co#mon_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeropt#hrpt_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiag#hrpt_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeroptday_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiagday_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamdaymin_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamdaymin_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/echam_output_results_.txt",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_co#mon_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_ma_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_tdiagmon_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeroptmon_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiag#hrpt_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamdaymax_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_ATM_mm_######.nc",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_cfdiagday_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echamday_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_tdiagday_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_aeroptmon_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echam#hr_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_accw_######.codes",
            "./AWIESM1.1_benchmark_001/outdata/echam/AWIESM#.#_benchmark_###_echam#_echammon_######.grb",
            "./AWIESM1.1_benchmark_001/outdata/echam/echam_output_setup_########.txt",
        ]
        self.assertEqual(expected_answer, grouped_files)

    def test_generate_model_dirs(self):
        """
        Checks if grouping files works correctly
        """
        model_dirs = esm_archiving._generate_model_dirs(
            "./AWIESM1.1_benchmark_001", "outdata"
        )
        self.assertEqual(
            model_dirs, ["echam", "oasis3mct", "hdmodel", "jsbach", "fesom"]
        )


class TestEsm_archiving(TestCase):
    """Tests for `esm_archiving` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "  --help     Show this message and exit." in help_result.output

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
