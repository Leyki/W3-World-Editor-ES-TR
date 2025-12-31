import os
import sys
import lib.blizzini as bini
# basic settings
vers = ["1.27b"]
langs = ["es", "en"]
files = ["WorldEditStrings.txt", "WorldEditGameStrings.txt", "WorldEditLayout.txt", "TriggerData.txt", "TriggerStrings.txt"]
# hints to parse
matchstart = [
        [
        "WESTRING_UEVAL_",   # Object Editor Unit fields
        "WESTRING_BEVAL",    # Destructable Editor fields
        "WESTRING_DEVAL_",   # Doodad Editor fields
        "WESTRING_AEVAL_",   # Ability Editor fields / Ability Specific Values
        "WESTRING_FEVAL_",   # Buff Editor Fields
        "WESTRING_GEVAL_",   # Upgrade Editor Fields
        "WESTRING_EEVAL_",   # Upgrade Effect Fields
        "WESTRING_MISCVAL_", # Misc data fields
        ]
    ]

def iter_base_data(langs: list, vers: list, files: list, parse_other, parse_none):
    for lang in langs:
        for ver in vers:
            for file in files:
                print(f"data/{lang}/versions/{ver}/UI/{file}")
                yield [lang, ver, file, bini.parse(f"data/{lang}/versions/{ver}/UI/{file}", parse_other, parse_none)]

def make_hints(files=["WorldEditStrings.txt"]):
    iterdata = iter_base_data(langs, vers, files, False, False)
    i = -1
    prev_file = ""
    for lang, ver, file, parsed in iterdata:
        if prev_file != file: i += 1 ; prev_file = file
        usable = []
        for element in parsed:
            for val in matchstart[i]:
                if element["name"].startswith(val): usable.append(element)
        bini.write_hints(f"{file[ :-4]}_hints_{lang}.txt", usable)


def make_release(langs=langs, vers=vers, files=files):
    iterdata = iter_base_data(langs, vers, files, True, True)
    for lang, ver, file, parsed in iterdata:
        if file == "WorldEditStrings.txt":
            parsed_hints = bini.parse(f"data/{lang}/versions/shared/Hints/{file}", False, False)
            parsed = parsed + parsed_hints
        os.makedirs(f"release/{lang}/{ver}/UI", exist_ok=True)
        bini.write(f"release/{lang}/{ver}/UI/{file[: -4]}.txt", parsed)

# run run
argl = len(sys.argv)
file, action = sys.argv
if argl == 1: print("Not enough arguments passed")
if argl == 2:
    match action:
        case "hints":
            make_hints() ; print("Hints done.")
        case "release":
            make_release() ; print("Release done.")
        case _:
            print("No valid argument has been passed.")
