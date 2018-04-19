import imath

import IECore

import Gaffer
import GafferScene

# You can use metadata to register named presets for any plug.
# These will be shown on the right-click context menu for the
# plug in the NodeEditor.

Gaffer.Metadata.registerValue( GafferScene.Plane, "dimensions", "preset:Small", imath.V2f( 0.1 ) )
Gaffer.Metadata.registerValue( GafferScene.Plane, "dimensions", "preset:Medium", imath.V2f( 1 ) )
Gaffer.Metadata.registerValue( GafferScene.Plane, "dimensions", "preset:Large", imath.V2f( 10 ) )

# If the number of presets varies dynamically, you can register
# callbacks to generate the preset names and values on the fly.

def __presetNames( plug ) :

	return IECore.StringVectorData( [
		"Sporty",
		"Architectural",
		"Geometric"
	] )

def __presetValues( plug ) :

	return IECore.StringVectorData( [
		"pitch",
		"wall",
		"plane"
	] )

Gaffer.Metadata.registerValue( GafferScene.Plane, "name", "presetNames", __presetNames )
Gaffer.Metadata.registerValue( GafferScene.Plane, "name", "presetValues", __presetValues )
