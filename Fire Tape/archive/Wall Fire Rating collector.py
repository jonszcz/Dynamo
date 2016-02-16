#Copyright(c) 2014, Nathan Miller
# The Proving Ground, http://theprovingground.org

import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#The input to this node will be stored in the IN[0] variable.

doc =  DocumentManager.Instance.CurrentDBDocument
app =  DocumentManager.Instance.CurrentUIApplication.Application

toggle = IN[0]
walltype = IN[1]

#output = []
#walls = []
#locations = []
#heights = []
#areas = []
#levelnames =[]
#elementids = []
#uniqueids = []
firerating = []

if toggle == True:

	collector = FilteredElementCollector(doc)
	collector.OfCategory(BuiltInCategory.OST_Walls)
	collector.OfClass(Wall)
 
	famtypeitr = collector.GetElementIdIterator()
	famtypeitr.Reset()

	for item in famtypeitr:
		famtypeID = item
		faminst = doc.GetElement(famtypeID)
    
		if walltype == '*':
			#API references to get wall data
			#loc = Revit.GeometryConversion.RevitToProtoCurve.ToProtoType( faminst.Location.Curve, True )
			#wall = faminst
    		#levname = faminst.Parameter['Base Constraint'].AsValueString()
			#height = faminst.Parameter['Unconnected Height'].AsDouble()
			#area = faminst.Parameter['Area'].AsDouble()
			#elementid = faminst.Id.ToString()
			#uniqueid = faminst.UniqueId
			firerating = faminst.Parameter['Fire Rating'].AsValueString()
    	
			#Apply wall data to containers to export
			#walls.append(wall)
			#locations.append(loc)
			#heights.append(height)
			#areas.append(area)
			#levelnames.append(levname)
			#elementids.append(elementid)
			#uniqueids.append(uniqueid)  
			firerating.append(firerating)
    	
		elif faminst.WallType.Id == UnwrapElement(walltype).Id:
			#loc = Revit.GeometryConversion.RevitToProtoCurve.ToProtoType( faminst.Location.Curve, True )
			#wall = faminst
    		#levname = faminst.Parameter['Base Constraint'].AsValueString()
			#height = faminst.Parameter['Unconnected Height'].AsDouble()
			#area = faminst.Parameter['Area'].AsDouble()
			#elementid = faminst.Id.ToString()
			#uniqueid = faminst.UniqueId
			firerating = faminst.Parameter['Fire Rating'].AsValueString()
    	
			#walls.append(wall)
			#locations.append(loc)
			#heights.append(height)
			#areas.append(area)
			#levelnames.append(levname)
			#elementids.append(elementid)
			#uniqueids.append(uniqueid)
			firerating.append(firerating)
        
	#output.append(walls)
	#output.append(locations)
	#output.append(heights)
	#output.append(areas)
	#output.append(levelnames)
	#output.append(elementids)
	#output.append(uniqueids)
	output.append(firerating)
        
#Assign your output to the OUT variable
OUT = output