#!/work/mccleary_group/vassilakis.g/miniconda3/envs/astrometry-net/bin/python

import argparse
import subprocess

# Set up argument parser
parser = argparse.ArgumentParser(description='Run beheader, update WCS, and convert SIP to TPV on FITS files.')
parser.add_argument('files', metavar='F', type=str, nargs='+',
                    help='A list of FITS files to process')

# Parse command line arguments
args = parser.parse_args()

def run_script(script_name, files):
    command = ['python', script_name] + files
    print(f"Running command: {' '.join(command)}")
    subprocess.run(command, check=True)

# Run beheader.py
run_script('/work/mccleary_group/vassilakis.g/Software/wcs_beheader/beheader.py', args.files)

# Run update_wcs.py
run_script('/work/mccleary_group/vassilakis.g/Software/wcs_beheader/update_wcs.py', args.files)

# Run sip_to_tpv.py
run_script('/work/mccleary_group/vassilakis.g/Software/wcs_beheader/sip_to_tpv.py', args.files)

print("All operations completed.")
