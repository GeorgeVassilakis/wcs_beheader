#!/usr/bin/env python3

import argparse
import subprocess
import os

# Set up argument parser (take in a list of files or a directory)
parser = argparse.ArgumentParser(description='Run beheader, update WCS, and convert SIP to TPV on FITS files.')

# Set it up to take either a list of files of files or a directory (one or the other is required, not both)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--files', metavar='F', type=str, nargs='+', help='A list of files to run the scripts on.')
group.add_argument('--dir', type=str, help='A directory of files to run the scripts on.')

# Parse command line arguments
args = parser.parse_args()

def run_script(script_name, argdirectory, argfiles):

    # If a directory is provided, get the list of files in the directory
    if argdirectory:
        files = [f for f in os.listdir(args.dir) if f.endswith('.fits')]
    else:
        files = argfiles

    # Construct the command to run the script
    command = ['python3', script_name, '--fits_files'] + files

    print(f"Running command: {' '.join(command)}")
    subprocess.run(command, check=True)

# Run beheader.py
run_script('beheader.py', args.dir, args.files)

# Run update_wcs.py
run_script('update_wcs.py', args.dir, args.files)

# Run sip_to_tpv.py
run_script('sip_to_tpv.py', args.dir, args.files)

print("All operations completed.")
