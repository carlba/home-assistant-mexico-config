#!/usr/bin/env python

import json
import re
import sys

def parse_logline(logline):
    # Define the regular expression pattern to match the logline
    pattern = (r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) '
               r'(?P<level>[A-Z]+) '
               r'\((?P<worker>[^)]+)\) '
               r'\[(?P<component>[^\]]+)\] '
               r'(?P<message>.*)')
    
    match = re.match(pattern, logline)
    if match:
        return match.groupdict()
    else:
        raise ValueError("Logline format is incorrect")

def logline_to_json(logline):
    log_dict = parse_logline(logline)
    return json.dumps(log_dict, indent=4)

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                log_json = logline_to_json(line)
                print(log_json)
            except ValueError as e:
                print(f"Error parsing logline: {e}", file=sys.stderr)