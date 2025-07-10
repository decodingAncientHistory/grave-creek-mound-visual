###### SAMPLE PYTHON 3 CODE TO VISUALIZE USGS LIDAR DATA OVER MOUNDSVILLE, WV

    There are two Python 3 source files in this repository: liday.py and native_american_mounds.py.
    The liday.py file is a utility file, that contains a class for reading Lidar files (.laz extension).
    The so-called "main()" method is in native_american_mounds.py.

    This is just a short simple program that shows some code of how to read an .laz file with
    Lidar data, and visualize the data within. The code first reads the data from the input .laz file,
    and re-projects the coordinates from meters to a WGS-84 (decimal-degrees) projection. From there,
    the points are filtered to a very small bounding box centered over the Grave Creek Mound, in
    Moundsville, WV. 

    Then the data is visualized in 3D, sending this visaul to a PNG file that you see below.
       
###### COMMAND-LINE USAGE:

    Install pre-requisites (if necessary). For example, on Ubuntu/Debian:
    $ pip3 install numpy
    $ pip3 install matplotlib
    $ pip3 install laspy
    $ pip3 install "laspy[laszip]"

    Then to run:
    $ python3 native_american_mounds.py USGS_LPC_WV_FEMAR3_Southcentral_2018_D19_e1286n1981.laz

###### INPUT DATA

    Input data file(s) can be downloaded from the U.S. Geological Survey's
    Earth Explorer Website:
      https://earthexplorer.usgs.gov/
    
###### Python version:
     
    Uses Python 3.8.x+
       
###### Sample Outputs

![Alt text](https://64.media.tumblr.com/4b2b3f3adcfc56d22ba5799679ab0eca/258731833f755aed-be/s1280x1920/d9db5433980ccd6715ab1f4a53de7f7983068111.pnj)

    A 1-band Geotiff is written out to disk. This Geotiff contains 1s and 0s. The 1s 
    mark areas of so-called "flood-fill." This is the area that is "filled-in" by the 
    algorithm according to the elevation boundaries of the Digital Elevation Model.

    We can use any common plotting software (e.g. Python, Matlab, QGIS, GrADS, etc.)
    to visualize the output (here we are using's Python 3.x's Matplotlib module.
        
###### @author: 
    Gerasimos Michalitsianos
    gerasimosmichalitsianos@protonmail.com
    Lakithra@protonmail.com
    10 July 2025
