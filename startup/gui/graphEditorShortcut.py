import GafferUI

def __graphEditorKeyPress( graphEditor, event ) :

	if event.key in ( "Plus", "Minus" ) :

		viewportGadget = graphEditor.graphGadgetWidget().getViewportGadget()
		camera = viewportGadget.getCamera()

		screenWindow = camera.parameters()["screenWindow"].value
		center = screenWindow.center()
		size = screenWindow.size() / 2.0

		if event.key == "Plus" :
			size /= 1.4
		else :
			size *= 1.4

		screenWindow.setMin( center - size )
		screenWindow.setMax( center + size )

		camera.parameters()["screenWindow"].value = screenWindow
		viewportGadget.setCamera( camera )

		# Return `True` to signify that we've handled the keypress.
		# This stops the event from being passed to anyone else.
		return True

	return False

def __graphEditorCreated( graphEditor ) :

	graphEditor.keyPressSignal().connect( __graphEditorKeyPress, scoped = False )

GafferUI.GraphEditor.instanceCreatedSignal().connect( __graphEditorCreated, scoped = False )
