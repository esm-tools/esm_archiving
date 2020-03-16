#!/usr/bin/env python3
"""
Use this program to create a binary representation of a os.walk for a
particular directory; useful when you want to re-hydrate and use a particular
folder/file structure for unit testing.

Example Usage::

    $ ./make_exp_walk /work/ab0246/a270077/esm_benchmarks/exp_001 exp_001_walk.dat


Author:
    Paul Gierz
    AWI Bremerhaven
    2020
"""
import argparse
import os
import pickle


def parse_args():
    """
    Gets command line arguments to generate a binary file representing a binary
    exp_walk which can be used for unit testing.
    """
    parser = argparse.ArgumentParser(
        usage="""Use this program to create a virtual
            representation of a file system for a particular experiment to do
            unit testing with. When pointed at the top level folder of a
            particular experiment, the program will write a binary file which
            you can use to make fake filesystem objects with."""
    )
    parser.add_argument("root")
    parser.add_argument("ofile")
    return parser.parse_args()


def save_tree(obj, ofile):
    """ Saves object to a pickle file

    Parameters
    ----------
    obj:
        The thing to pickle
    ofile : str
        Filename to write to for pickling
    """
    with open(ofile, "wb") as f:
        pickle.dump(obj, f)


def main():
    """
    Main Program: Parse arguments, run os.tree, and save result to a file
    """
    args = parse_args()
    tree_answer = list(os.walk(args.root))
    save_tree(tree_answer, args.ofile)


if __name__ == "__main__":
    main()
