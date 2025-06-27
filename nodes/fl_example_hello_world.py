class FLExampleHelloWorld:
    """
    A simple example node that takes a string and returns it with a prefix.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": False,
                    "default": "Hello, World!"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "Fill-Example-Nodes"

    def run(self, text):
        return (f"You said: {text}",)
