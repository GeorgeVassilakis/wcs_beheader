# wcs_beheader
Behead current WCS keywords from header, solve new astrometry, convert SIP to TPV

# Usage notes
- Requires astrometry-net to be installed. Follow instructions here: https://astrometry.net/use.html
- When running, make sure that `solve-field` is accessible in your path!
- We strongly recommend the use of the 5200-series index files, preferably 5200-5202 but no smaller (>5203). Index files whose scales are too small may lead to inaccurate WCS solutions. You may have to move or even deleting smaller-scale index files from the default index directory, as astrometry-net will always default to the smallest scale possible. 
- References to tangent plane projections can be found [here](https://www.researchgate.net/publication/333841450_Astrometry_The_Foundation_for_Observational_Astronomy) and [here](https://astronomy.stackexchange.com/questions/43449/plotting-equatorial-coordinates-to-x-y-plane-simulating-telescope-camera-view)
