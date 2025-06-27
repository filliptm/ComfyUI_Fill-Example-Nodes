import time
import comfy.utils

class FLExampleProgressBar:
    """
    An example node that demonstrates how to use a progress bar.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "iterations": ("INT", {
                    "default": 10,
                    "min": 1,
                    "max": 100,
                    "step": 1,
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "Fill-Example-Nodes"

    def run(self, iterations):
        pbar = comfy.utils.ProgressBar(iterations)
        for i in range(iterations):
            time.sleep(0.1)
            pbar.update(1)
        return ("Finished!",)