import Gaffer
import GafferExamples

Gaffer.Metadata.registerNode(

	GafferExamples.RenderPass,

	"description",
	"""
	Example of creating a monolithic node representing a render pass.
	""",

	plugs = {

		"in" : [

			"description",
			"""
			The scene to be rendered.
			""",

			"nodule:type", "GafferUI::StandardNodule",

		],

	}

)
