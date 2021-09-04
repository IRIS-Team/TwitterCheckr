import json

colours = json.loads(open("theme/default.json").read())

class colours:
    main = colours["main_color"]
    sencondary = colours["sencondary"]
    text = colours["text"]
    darktext = colours["darktext"]
    error = colours["error"]

def returnColor(string) -> str:
    return f'{colours.main}{string}{colours.text}'