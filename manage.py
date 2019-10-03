#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
from FantasyFootballDjango.GatherData import *

def main():

    # espn league ID
    league_id = 555232

    # espn league year
    year = 2019

    rawData = gatherRawData(league_id, year)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(rawData, f, ensure_ascii=False, indent=4)

    analyzeData(rawData)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FantasyFootballDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
