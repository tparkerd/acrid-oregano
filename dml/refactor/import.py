#!/usr/bin/env python
"""Importation script that handles retrieving user-input for initializing data"""

import argparse
import os
import shutil
import datetime
import json


from pprint import pprint

def process(args):
  """Method to preprocess dataset to parse out the necessary """
  # try:
  #   with open(args.meta, 'r') as mfp:
  #     m = json.load(mfp)

  #     pprint(m)
  # except:
  #   raise


  # Dependency rundown
  # Independent values -- require extraction or user-input
  #   NAME                           ABBR     DEP(S)
  #   Location                       L
  #   Species                        S
  #   Traits                         T
  #   Growout_type                   GT
  #   GWAS_algorithm                 GA
  #   Imputation_method              IM
  #   Kinship_algorithm              KA
  #   Population_structure_algortihm PSA
  # 
  # One Independent Dependency
  #   Population                     P        S
  #   Chromosome                     C        S
  #   Kinship                        K        KA
  #   Population_structure           PS       PSA
  # 
  # One Dependent Dependency
  #   Line                           L        P
  # 
  # Two Dependencies (Mixed only)
  #   Genotype_version               GV       L, P
  #   Variant                        V        S, C
  #   Phenotype                      PH       L, T
  # 
  # Three Dependencies (Mixed only)
  #   Genotype                       G        L, C, GV
  #   Growout                        GO       L, P, GT
  # 
  # Many Dependencies (Mixed only)
  #   GWAS_run                       GRUN     T, GA, GV, IM, K, PS
  #   GWAS_result                    GRES     C, GRUN


  # Get all of the independent values
  # NOTE: this includes finding them if the value already exists in the database
  # Location
  #   These values can be extracted from phenotype files.
  #   Their filenames include the location code and year (for growout)
  # Find directory of phenotype files




  # Species
  # Traits
  # Growout_type
  # GWAS_Algorithm
  # Imputation_method
  # Kinship_algorithm
  # Population_structure_algorithm








  pass


def parseOptions():
  """
  Function to parse user-provided options from terminal
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-m", "--meta", required = True,
                      help="JSON format file that contains metadata about the dataset to import.")
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
  try:
    process(args)
  except:
    raise
