import inspect

import IECore
import IECoreScene

import Gaffer
import GafferDispatch
import GafferScene
import GafferArnold

class RenderPass( GafferDispatch.TaskNode ) :

	def __init__( self, name = "RenderPass" ) :

		GafferDispatch.TaskNode.__init__( self, name )

		# Plugs
		# =====
		#
		# These define the interface that the user sees.

		self["in"] = GafferScene.ScenePlug()
		self["passName"] = Gaffer.StringPlug()

		# Internal node network
		# =====================
		#
		# This implements the functionality of the node

		# Delete any outputs the user has defined in the scene.
		# We want to be in complete control of these ourselves.
		self["__deleteOutputs"] = GafferScene.DeleteOutputs()
		self["__deleteOutputs"]["names"].setValue( "*" )
		self["__deleteOutputs"]["in"].setInput( self["in"] )

		# Add an outputs node with the outputs we do want to make.
		self["__outputs"] = GafferScene.Outputs()
		self["__outputs"]["in"].setInput( self["__deleteOutputs"]["out"] )
		self["__outputs"].addOutput(
			"beauty",
			IECoreScene.Output( "/tmp/renderPass/${passName}/beauty/beauty.####.exr", "exr", "rgba", {} )
		)
		self["__outputs"].addOutput(
			"diffuse",
			IECoreScene.Output( "/tmp/renderPass/${passName}/diffuse/diffuse.####.exr", "exr", "color diffuse", {} )
		)

		# Add a "passName" variable that the user can use upstream
		# to generate different scenes for different passes.
		self["__variables"] = GafferScene.SceneContextVariables()
		self["__variables"]["in"].setInput( self["__outputs"]["out"] )
		passNameVariable = self["__variables"]["variables"].addMember( "passName", Gaffer.StringPlug() )
		passNameVariable["value"].setInput( self["passName"] )

		# Add a render node to render the scene. This is the meat
		# of our functionality.

		self["__arnoldRender"] = GafferArnold.ArnoldRender()
		self["__arnoldRender"]["in"].setInput( self["__variables"]["out"] )

		# Add a post-process node to do something to the images that
		# we've generated. Use an expression to grab the filenames of
		# all output images and connect that into a variable the python
		# command can use.
		## \todo Gaffer should provide a simple utility node to grab all the
		# filenames so we don't even need an expression.

		self["__postProcess"] = GafferDispatch.PythonCommand()
		self["__postProcess"]["preTasks"][0].setInput( self["__arnoldRender"]["task"] )
		self["__postProcess"]["variables"].addMember( "filenames", Gaffer.StringVectorDataPlug( defaultValue = IECore.StringVectorData() ), "filenames" )
		self["__postProcess"]["command"].setValue(
			"for filename in variables['filenames'] : print 'Post-processing {0}'.format( filename )"
		)

		self["__postProcessExpression"] = Gaffer.Expression()
		self["__postProcessExpression"].setExpression( inspect.cleandoc(
			"""
			sceneGlobals = parent["__arnoldRender"]["in"]["globals"]
			filenames = IECore.StringVectorData()
			for name, value in sceneGlobals.items() :
				if not name.startswith( "output:" ) :
					continue
				filenames.append( value.getName() )

			parent["__postProcess"]["variables"]["filenames"]["value"] = filenames
			"""
		) )

		# Connect the post-process directly into our output task plug.
		# This means we don't need to implement any of the usual TaskNode
		# methods because we are deferring all the work to the internal
		# network.
		self["task"].setInput( self["__postProcess"]["task"] )

IECore.registerRunTimeTyped( RenderPass, typeName = "GafferExample::RenderPass" )
