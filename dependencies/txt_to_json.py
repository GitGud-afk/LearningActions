import json

with open("input/inputTxt.txt") as f:
  lines = f.readlines()

result = dict()


for line in lines:]
  if ":" in line:
    splitLine = line.split(":")
    key = splitLine[0].strip()
    value = splitLine[1].strip()
    result[key] = value


with open("intermediatesData/splitKey.json") as f:
  json.dump(result, f, indent=4)


