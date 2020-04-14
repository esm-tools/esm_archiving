#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import os
import pickle

from fsforge import create_fs


def create_fs_benchmark(benchmark):
    fake_fs_root = "/tmp/esm_archiving/" + benchmark
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_walk_file = os.path.join(dir_path, benchmark + "_fs_snapshot.dat")
    with open(test_walk_file, "rb") as f:
        tree = pickle.load(f)

    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            fs = kwargs["fs"]
            create_fs(fs, tree, fake_fs_root)
            func(*args, **kwargs)

        return wrapper

    return inner_function
