#!/work/mccleary_group/vassilakis.g/miniconda3/envs/astrometry-net/bin/python

import argparse
from astropy.io import fits
import sip_tpv

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert SIP headers to TPV headers in FITS files.')
parser.add_argument('files', metavar='F', type=str, nargs='+',
                    help='A list of FITS files to convert SIP to TPV headers for')

# Parse command line arguments
args = parser.parse_args()

def convert_sip_to_tpv(fits_filename):
    # Open the FITS file
    with fits.open(fits_filename) as hdul:
        # Modify the header in-place
        sip_tpv.sip_to_pv(hdul[0].header)
        
        # Save the modified file, overwriting the original file
        hdul.writeto(fits_filename, overwrite=True)
        print(f"Converted {fits_filename}")

# Iterate over the provided FITS files and convert their headers
for file in args.files:
    convert_sip_to_tpv(file)

print("Files converted")
