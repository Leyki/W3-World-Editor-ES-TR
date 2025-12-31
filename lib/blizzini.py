import re
number = re.compile(r"^[0-9]*$") # todo, negatives, dotted

def _parse_list(values: str) -> list:
    parsed = []
    stored = ""
    value_open = False
    string_open = False
    for char in values:
        if char == ",":
            if string_open: stored += char
            if value_open: value_open = False

            if not string_open and not value_open:
                parsed.append(stored) ; stored = ""
            continue

        if char == '"': string_open = not string_open
        if not value_open and not string_open: value_open = True
        stored += char
    parsed.append(stored)
    return parsed

 
def _parse_types(value: str) -> int | list | str | None:
    if value == "": return ""
    if value.count('"') == 2: return value
    if not '\"' in value and not ',' in value:
        return value
    # m = number.match(value)
    # if m != None: return int(value)
    return _parse_list(value)
    
def _parse(result: list, file: str, parse_other, parse_none):
    # I don't know if converting everything to utf8 is fine but i don't wanna deal with blizzard deciding to use any encoding at random
    with open(file, "r", encoding="utf8") as ini:
        for line in ini:
            line = line.lstrip().rstrip("\n")
            
            if line == "" or line.startswith("//"): 
                if parse_other: result.append({ "kind": "other", "value": line})
                continue
            if line[0] == "[":
                if parse_other: result.append({ "kind": "section", "value": line}) 
                continue

            i = line.find("=")
            if i == -1: continue
            
            value = _parse_types(line[i+1: ])
            if not parse_none and (value == None or value == ""): continue
            result.append({"kind": "data", "name": line[ :i], "value": value})

def parse(file: str, parse_other=True, parse_none=True):
    result = []
    _parse(result, file, parse_other, parse_none)
    return result

def parse_files(files: list, parse_other=True, parse_none=True):
    results = []
    for file in files:
        result = []
        _parse(result, file, parse_other, parse_none)
        results.append(result)
    return results

def write(file_name: str, data: list):
    with open(file_name, "w", encoding="utf8") as file:
        for line in data:
            if line["kind"] == "data":
                wvalue = line["value"]
                if not line["value"] == None and type(line["value"]) == list:
                    wvalue = ""
                    for value in line["value"]:
                        wvalue += value + ","
                    wvalue = wvalue.rstrip(",")
                file.write(line["name"] + "=" + wvalue + "\n")
            else: file.write(line["value"] + "\n")

def write_hints(file_name: str, data: list, test=False):
    with open(file_name, "w", encoding="utf8") as file:
        for line in data:
            if not line["kind"] == "data" or line["name"].endswith("_HINT"): continue
            wvalue = line["value"]
            if not line["value"] == None and type(line["value"]) == list:
                wvalue = ""
                for value in line["value"]:
                    wvalue += value + ","
                wvalue = wvalue.rstrip(",")
            if test: file.write(f'//-- {wvalue}\n{line["name"]}_HINT="{wvalue} hint"\n')
            else: file.write(f'//-- {wvalue}\n{line["name"]}_HINT=\n')
