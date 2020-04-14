import os

from esm_archiving.esm_archiving import (
    _generate_model_dirs,
    _walk_through_model_dir_clean_numbers,
)

from .fake_fs_utils import create_fs_benchmark


BENCHMARK = "AWIESM1.1_benchmark_001"
BASE_DIR = "tmp/esm_archiving/"
TOP = "/tmp/esm_archiving/" + BENCHMARK


@create_fs_benchmark(BENCHMARK)
def test_tree_exists(fs):
    assert os.path.isdir(BASE_DIR)
    assert os.path.isdir(TOP)


@create_fs_benchmark(BENCHMARK)
def test_generate_model_dirs(fs):
    model_dirs = _generate_model_dirs(TOP, "outdata")
    assert sorted(model_dirs) == sorted(
        ["echam", "fesom", "hdmodel", "jsbach", "oasis3mct"]
    )


@create_fs_benchmark(BENCHMARK)
def test_clean_filepatterns_echam_outdata(fs):
    cleaned_patterns = _walk_through_model_dir_clean_numbers(TOP + "/outdata/echam")
    expected_filepatterns = [
        "AWIESM1.1_benchmark_###_echam6_ATM_mm_######.nc",
        "AWIESM1.1_benchmark_###_echam6_BOT_mm_######.nc",
        "AWIESM1.1_benchmark_###_echam6_LOG_mm_######.nc",
        "AWIESM1.1_benchmark_###_echam6_accw_######.codes",
        "AWIESM1.1_benchmark_###_echam6_accw_######.grb",
        "AWIESM1.1_benchmark_###_echam6_aeropt#hrpt_######.codes",
        "AWIESM1.1_benchmark_###_echam6_aeropt#hrpt_######.grb",
        "AWIESM1.1_benchmark_###_echam6_aeroptday_######.codes",
        "AWIESM1.1_benchmark_###_echam6_aeroptday_######.grb",
        "AWIESM1.1_benchmark_###_echam6_aeroptmon_######.codes",
        "AWIESM1.1_benchmark_###_echam6_aeroptmon_######.grb",
        "AWIESM1.1_benchmark_###_echam6_cfdiag3hrpt_######.codes",
        "AWIESM1.1_benchmark_###_echam6_cfdiag3hrpt_######.grb",
        "AWIESM1.1_benchmark_###_echam6_cfdiag6hrpt_######.codes",
        "AWIESM1.1_benchmark_###_echam6_cfdiag6hrpt_######.grb",
        "AWIESM1.1_benchmark_###_echam6_cfdiagday_######.codes",
        "AWIESM1.1_benchmark_###_echam6_cfdiagday_######.grb",
        "AWIESM1.1_benchmark_###_echam6_cfdiagmon_######.codes",
        "AWIESM1.1_benchmark_###_echam6_cfdiagmon_######.grb",
        "AWIESM1.1_benchmark_###_echam6_co2_######.codes",
        "AWIESM1.1_benchmark_###_echam6_co2_######.grb",
        "AWIESM1.1_benchmark_###_echam6_co2mon_######.codes",
        "AWIESM1.1_benchmark_###_echam6_co2mon_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echam3hr_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echam3hr_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echam3hrpt_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echam3hrpt_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echam6hr_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echam6hr_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echam6hrpt_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echam6hrpt_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echam_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echam_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echamday_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echamday_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echamdaymax_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echamdaymax_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echamdaymin_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echamdaymin_######.grb",
        "AWIESM1.1_benchmark_###_echam6_echammon_######.codes",
        "AWIESM1.1_benchmark_###_echam6_echammon_######.grb",
        "AWIESM1.1_benchmark_###_echam6_ma_######.codes",
        "AWIESM1.1_benchmark_###_echam6_ma_######.grb",
        "AWIESM1.1_benchmark_###_echam6_tdiagday_######.codes",
        "AWIESM1.1_benchmark_###_echam6_tdiagday_######.grb",
        "AWIESM1.1_benchmark_###_echam6_tdiagmon_######.codes",
        "AWIESM1.1_benchmark_###_echam6_tdiagmon_######.grb",
        "echam_output_results_.txt",
        "echam_output_setup_########.txt",
    ]
    expected_filepatterns = [
        TOP + "/outdata/echam/" + item for item in expected_filepatterns
    ]
    assert sorted(expected_filepatterns) == sorted(cleaned_patterns)
