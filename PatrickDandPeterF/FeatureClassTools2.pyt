import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "fctoolsPYT"

        # List of tool classes associated with this toolbox
        self.tools = [BasicDescribe, FeatureClassLister]


class BasicDescribe(object):
    def BasicDescribe(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Basic Describe associated with Describe03.py"
        self.description = " "
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        param1 = arcpy.Parameter(
            displayName = "Feature Class",
            name = "Feature Class",
            datatype = "DEFeatureClass",
            parameterType = "Required",
            direction = "Input")
        params = [param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        from arcpy import GetParameterAsText
        fc = parameters[0].valueAsText
        Dfc = arcpy.Describe(fc)
        arcpy.AddMessage("{:13}: {}".format("BaseName", Dfc.BaseName))
        arcpy.AddMessage("{:13}: {}".format("CatalogPath", Dfc.CatalogPath))
        arcpy.AddMessage("{:13}: {}".format("DataType", Dfc.DataType))
        return


class FeatureClassLister(object):
    def FeatureClassLister(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Feature Class Lister associated with List02.py"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        Folparam = arcpy.Parameter(
            displayName = "Folder",
            name = "Folder",
            datatype = "DEFolder",
            parameterType = "Required",
            direction = "Input")
        params = [Folparam]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        qwe = arcpy.env.workspace = parameters[0].valueAsText
        if arcpy.Exists(qwe):
            f = arcpy.ListFeatureClasses()
            for i in f:
                arcpy.AddMessage(i)


