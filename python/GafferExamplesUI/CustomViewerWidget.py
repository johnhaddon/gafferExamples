import Gaffer
import GafferUI
import GafferImageUI

# Define our widget class. There are no requirements on this other than
# that it should accept a node argument to the constructor - in this case
# `imageView`.
class CustomViewerWidget( GafferUI.Button ) :

	def __init__( self, imageView, **kw ) :

		GafferUI.Button.__init__( self, "Hello World", **kw )

		self.__imageView = imageView

		self.clickedSignal().connect( Gaffer.WeakMethod( self.__clicked ), scoped = False )

	def __clicked( self, widget ) :

		print "Hello World"

# Register the widget into the top toolbar of the ImageView.
Gaffer.Metadata.registerNode(

	GafferImageUI.ImageView,

	"toolbarLayout:customWidget:MyWidget:widgetType", "GafferExamplesUI.CustomViewerWidget",
	"toolbarLayout:customWidget:MyWidget:section", "Top",

)

