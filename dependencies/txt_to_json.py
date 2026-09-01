import json
import os

with open("input/inputTxt.txt") as f:
  lines = f.readlines()

result = dict()


for line in lines:
  if ":" in line:
    splitLine = line.split(":")
    key = splitLine[0].strip()
    value = splitLine[1].strip()
    result[key] = value


os.makedirs("intermediatesData", exist_ok=True)
with open("intermediatesData/splitKey.json", 'w') as f:
  json.dump(result, f, indent=4)


