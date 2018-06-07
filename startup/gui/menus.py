import GafferUI
import GafferExamples
import GafferExamplesUI

nodeMenu = GafferUI.NodeMenu.acquire( application )

nodeMenu.append( "/Examples/Render Pass", GafferExamples.RenderPass, searchText = "RenderPass" )
nodeMenu.append( "/Examples/Globals Expression", GafferExamples.GlobalsExpression, searchText = "GlobalsExpression" )
