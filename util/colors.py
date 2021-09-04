import json

colors = json.loads(open("theme/default.json").read())

class colors:
    main = colors["main_color"]
    sencondary = colors["sencondary"]
    text = colors["text"]
    darktext = colors["darktext"]
    error = colors["error"]

def returnColor(string) -> str:
    return f'{colors.main}{string}{colors.text}'