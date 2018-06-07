import functools

import IECore

import GafferUI
import GafferSceneUI

def __contextMenu( sceneHierarchy ) :

	menu = IECore.MenuDefinition()
	menu.append(
		"/Collapse All",
		{
			"command" : functools.partial( GafferSceneUI.ContextAlgo.clearExpansion, sceneHierarchy.getContext() ),
			"active" : not GafferSceneUI.ContextAlgo.getExpandedPaths( sceneHierarchy.getContext() ).isEmpty()
		}
	)

	sceneHierarchy.__popupMenu = GafferUI.Menu( menu )
	sceneHierarchy.__popupMenu.popup()

def __instanceCreated( sceneHierarchy ) :

	sceneHierarchy.contextMenuSignal().connect( __contextMenu, scoped = False )

GafferSceneUI.SceneHierarchy.instanceCreatedSignal().connect( __instanceCreated, scoped = False )
