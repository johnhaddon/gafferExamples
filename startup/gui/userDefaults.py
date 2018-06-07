import imath
import Gaffer
import GafferScene

# User defaults are applied automatically whenever a node is created by the user through the UI.

Gaffer.Metadata.registerValue( GafferScene.Sphere, "radius", "userDefault", 100.0 )
Gaffer.Metadata.registerValue( GafferScene.StandardOptions, "options.renderResolution.value", "userDefault", imath.V2i( 2048, 1556 ) )
