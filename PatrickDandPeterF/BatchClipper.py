#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MCE
#
# Created:     23/01/2018
# Copyright:   (c) MCE 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Name: Clip_Example2.py
# Description: Clip major roads that fall within the study area.

# Import system modules
import sys
import os


if len(sys.argv) != 4:
    print "Usage: BatchClipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>"
    sys.exit()

import arcpy
from arcpy import env


InWorkspace = sys.argv[1]
ClipWorkspace = sys.argv[2]
OuputWorkspace = sys.argv[3]


arcpy.env.workspace = InWorkspace
Cliplist = arcpy.ListFeatureClasses()

arcpy.env.workspace = ClipWorkspace
ClipingList = arcpy.ListFeatureClasses()


for x in Cliplist:
    for y in ClipingList:
        arcpy.Clip_analysis(InWorkspace +"/" + x, ClipWorkspace +"/" + y, OuputWorkspace +"/"+y[:-4]+"_"+x)






