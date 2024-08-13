#!/usr/bin/env python3

import argparse
import os

# Set up argument parser (take in a list of files or a directory)
parser = argparse.ArgumentParser(description='Run beheader, update WCS, and convert SIP to TPV on FITS files.')

# Set it up to take either a list of files of files or a directory (one or the other is required, not both)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--files', metavar='F', type=str, nargs='+', help='A list of files to run the scripts on.')
group.add_argument('--dir', type=str, help='A directory of files to run the scripts on.')

parser.add_argument('--num_threads', type=int, default=30, help='Number of threads to use for solve-field command')

# Parse command line arguments
args = parser.parse_args()

def run_script(script_name, argdirectory, argfiles, argnum_threads=None):

    # If a directory is provided, get the list of files in the directory
    if argdirectory:
        files = [f for f in os.listdir(args.dir) if f.endswith('.fits')]

        # Prepend the directory to the file names
        files = [os.path.join(args.dir, f) for f in files]

    else:
        files = argfiles

    # Construct the command to run the script
    if argnum_threads is None:
        command = 'python3 ' + script_name + ' --files ' + ' '.join(files)
    else:
        command = 'python3 ' + script_name + ' --files ' + ' '.join(files) + ' --num_threads ' + str(argnum_threads)

    # Run the command
    print(f"Running command: {command}")
    os.system(command)

# Get path to runner.py
runner_path = os.path.abspath(__file__)

# Run beheader.py
run_script(runner_path.replace('runner.py', 'beheader.py'), args.dir, args.files)

# Run update_wcs.py
run_script(runner_path.replace('runner.py', 'update_wcs.py'), args.dir, args.files, args.num_threads)

# Run sip_to_tpv.py
run_script(runner_path.replace('runner.py', 'sip_to_tpv.py'), args.dir, args.files)

print("All operations completed.")
