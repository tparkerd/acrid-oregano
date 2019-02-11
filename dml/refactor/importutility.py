#!/usr/bin/env python
"""Utility methods for import.py"""
from datetime import datetime as dt

def growout_name_to_year(value):
  """Takes in a LOYR (Location-Year) string and converts year digits to four-digit year"""
  # Pre-cleaning
  value = value.strip()
  try:
    if len(value) < 4:
      return None
    else:
      prefix = value[:2]
      suffix = value[-2:]
      current_year_suffix = str(dt.now().year)[-2:]
      # Assume if the last two digits are greater than those of the current year,
      # then we are working in the previous millennium
      if int(suffix) > int(current_year_suffix):
        value = f"19{suffix}"
      else:
        value = f"20{suffix}"
      return value
  except:
    return None