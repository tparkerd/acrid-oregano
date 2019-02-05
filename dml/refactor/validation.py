#!/usr/bin/env python
"""Handles data validation and preprocessing for importation module"""

import argparse
import os
import shutil


def parseOptions():
  """
  Function to parse user-provided options from terminal
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", action="store_true",
                      help="Increase output verbosity")
  parser.add_argument("-o", "--outdir", default = f"output_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}",
                      help="Path of output directory")
  parser.add_argument("--debug", action = "store_true", help = "Enables --verbose and disables writes to disk")
  args = parser.parse_args()
  if args.debug is True:
    args.verbose = True
    args.write = False
  
  return args

if __name__ == "__main__":
  args = parseOptions()
  process(args)
