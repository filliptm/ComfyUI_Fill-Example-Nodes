import torch
import numpy as np

class FLExampleCanvasColorPicker:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "selected_color": ("STRING", {"default": "#FF0000"}),
                "width": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 8}),
                "height": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 8}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING",)
    FUNCTION = "get_color"
    CATEGORY = "Fill-Example-Nodes"

    def get_color(self, selected_color, width, height):
        # Convert hex to RGB
        hex_color = selected_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        # Create a blank image
        image = np.full((height, width, 3), (r, g, b), dtype=np.uint8)

        # Convert to tensor
        image_tensor = torch.from_numpy(image).unsqueeze(0).float() / 255.0

        return (image_tensor, selected_color,)