"""A main program for Byterun."""

import argparse
import logging
import sys
import builtins
import types
import importlib.util

from byterun.execfile import run_python_file, run_python_module

parser = argparse.ArgumentParser(
    prog="byterun",
    description="Run Python programs with a custom bytecode interpreter.",
)
parser.add_argument(
    "-m",
    dest="module",
    action="store_true",
    help="prog is a module name, not a file name.",
)
parser.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Trace the execution of the bytecode.",
)
parser.add_argument(
    "prog",
    help="The program to run.",
)
parser.add_argument(
    "args",
    nargs=argparse.REMAINDER,
    help="Arguments to pass to the program.",
)

args = parser.parse_args()

# Set up logging
level = logging.DEBUG if args.verbose else logging.WARNING
logging.basicConfig(level=level)

# Prepare arguments
sys.argv = [args.prog] + args.args

# Choose runner
if args.module:
    run_fn = run_python_module
else:
    run_fn = run_python_file

# Run the program
try:
    run_fn(args.prog, sys.argv)
except Exception as e:
    logging.error("Error during execution: %s", e)
    sys.exit(1)
