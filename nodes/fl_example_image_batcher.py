import torch

class FLExampleImageBatcher:
    """
    An example node that demonstrates how to handle image tensor shapes and create batches.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "batch_size": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 64,
                    "step": 1,
                }),
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    FUNCTION = "run"
    CATEGORY = "Fill-Example-Nodes"

    def run(self, image, batch_size):
        shape = image.shape
        shape_str = f"Original shape: {shape}"
        
        # Repeat the image to create a batch
        batched_image = image.repeat(batch_size, 1, 1, 1)
        
        return (batched_image, shape_str)