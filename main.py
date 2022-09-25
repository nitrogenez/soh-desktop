dict = {
    "def": {
        "hello": False,
        "hithere": False
    },
    "rare": {
        "hier": False,
        "eil": False
    },
    "mythical": {
        "ach-huh": False,
        "sus": False
    }
}

texts = {
    "ach": {
        "ach-huh": "Hello, there!",
        "sus": "Hello!"
    }
}

def iterate_a(level, text):
    for i in dict[level]:
        if text == texts["ach"][i]:
            print(i + ' ' + text)

iterate_a("mythical", texts["ach"]["ach-huh"])