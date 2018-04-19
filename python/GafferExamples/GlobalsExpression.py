import inspect

import IECore

import Gaffer
import GafferScene

class GlobalsExpression( GafferScene.SceneProcessor ) :

	def __init__( self, name = "GlobalsExpression" ) :

		GafferScene.SceneProcessor.__init__( self, name )

		# Pass everything through
		self["out"].setInput( self["in"] )

		# But insert an expression to do something
		# to the globals.
		self["__expression"] = Gaffer.Expression()
		self["__expression"].setExpression( inspect.cleandoc(
			"""
			import IECoreScene

			inGlobals = parent["in"]["globals"]
			outGlobals = inGlobals.copy()

			for name, value in outGlobals.items() :

				if name.startswith( "output:Interactive" ) :
					del outGlobals[name]

				if isinstance( value, IECoreScene.Output ) :
					value.setName( "iCouldPutThisFileAnywhereIWanted.exr" )

			parent["out"]["globals"] = outGlobals
			"""
		) )

IECore.registerRunTimeTyped( GlobalsExpression, typeName = "GafferExamples.GlobalsExpression" )
