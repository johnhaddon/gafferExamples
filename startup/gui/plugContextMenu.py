import functools

import Gaffer
import GafferUI

def __double( plug ) :

	with Gaffer.UndoScope( plug.ancestor( Gaffer.ScriptNode ) ) :
		plug.setValue( plug.getValue() * 2 )

def __halve( plug ) :

	with Gaffer.UndoScope( plug.ancestor( Gaffer.ScriptNode ) ) :
		plug.setValue( plug.getValue() / 2 )

# This will be called dynamically when generating the popup
# menu for any plug.
def __popupMenu( menuDefinition, plugValueWidget ) :

	plug = plugValueWidget.getPlug()
	if not isinstance( plug, Gaffer.FloatPlug ) :
		return

	menuDefinition.append(
		"/Maths/Double",
		{
			"command" : functools.partial( __double, plug ),
			"active" : plug.settable() and not Gaffer.MetadataAlgo.readOnly( plug )
		}
	)

	menuDefinition.append(
		"/Maths/Halve",
		{
			"command" : functools.partial( __halve, plug ),
			"active" : plug.settable() and not Gaffer.MetadataAlgo.readOnly( plug )
		}
	)

GafferUI.PlugValueWidget.popupMenuSignal().connect( __popupMenu, scoped = False )
