import json
import os

with open("intermediatesData/splitKey.json") as f:
  myDict = json.load(f)

lines = [f'For key "{key}", the value is "{value}".\n' for key, value in myDict.items()]


os.makedirs("output", exist_ok = True)
with open("output/formattedTxt.txt", 'w') as f:
  f.write("\n".join(lines))
  
