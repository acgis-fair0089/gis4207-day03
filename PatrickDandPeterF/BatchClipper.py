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
import arcpy
import os
import sys
from arcpy import env


Clipfeature = "../../../Data/BatchClipData/TargetData"
Clipingfeature = "../../../Data/BatchClipData/Sites"



arcpy.env.workspace = Clipfeature
Cliplist = arcpy.ListFeatureClasses()

arcpy.env.workspace = Clipingfeature
ClipingList = arcpy.ListFeatureClasses()

OuputWorkspace = "../../../Data/BatchClipData/OuputFolder"

for x in Cliplist:
    for y in ClipingList:
        arcpy.Clip_analysis(Clipfeature +"/" + x, Clipingfeature +"/" + y, OuputWorkspace +"/"+y[:-4]+"_"+x)






