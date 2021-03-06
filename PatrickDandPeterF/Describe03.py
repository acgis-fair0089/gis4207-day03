#-------------------------------------------------------------------------------

# Name:     Describe03.py

# Purpose:

##Same as Describe02.py but pass the feature class in on the command-line using

##sys.argv.  If there is no argument, print the following usage:

##

##Usage:  Describe03.py <FeatureClassName>



# Author:      David Viljoen

# Created:     22/01/2015

#-------------------------------------------------------------------------------

#!/usr/bin/env python

import os

import sys

import arcpy



# Make sure there is one argument

if len(sys.argv) != 2:

    arcpy.AddMessage ("Usage:  Describe03.py <FeatureClassName>")

    sys.exit()



fc = sys.argv[1]

dsc = arcpy.Describe(fc)

fmt = "%-11s: %s"

##arcpy.AddMessage(fmt % ("BaseName",dsc.BaseName)+fmt % ("CatalogPath", dsc.CatalogPath) + fmt % ("DataType",dsc.DataType))
arcpy.AddMessage (fmt % ("BaseName",dsc.BaseName))

arcpy.AddMessage (fmt % ("CatalogPath", dsc.CatalogPath))

arcpy.AddMessage (fmt % ("DataType",dsc.DataType))


