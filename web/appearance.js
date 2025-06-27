import { app } from "/scripts/app.js";

app.registerExtension({
    name: "Fill-Example-Nodes.appearance",
    async nodeCreated(node) {
        if (node.comfyClass.startsWith("FLExample")) {
            node.color = "#6A006F";
            node.bgcolor = "#FFFFFF";
        }
    }
});