from .nodes.fl_example_hello_world import FLExampleHelloWorld
from .nodes.fl_example_progress_bar import FLExampleProgressBar
from .nodes.fl_example_image_batcher import FLExampleImageBatcher
from .nodes.fl_example_canvas_color_picker import FLExampleCanvasColorPicker

NODE_CLASS_MAPPINGS = {
    "FLExampleHelloWorld": FLExampleHelloWorld,
    "FLExampleProgressBar": FLExampleProgressBar,
    "FLExampleImageBatcher": FLExampleImageBatcher,
    "FLExampleCanvasColorPicker": FLExampleCanvasColorPicker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FLExampleHelloWorld": "Fill Example: Hello World",
    "FLExampleProgressBar": "Fill Example: Progress Bar",
    "FLExampleImageBatcher": "Fill Example: Image Batcher",
    "FLExampleCanvasColorPicker": "Fill Example: Canvas Color Picker",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]