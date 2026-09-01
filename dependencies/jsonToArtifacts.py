import json

with open("intermediatesData/splitKey.json") as f:
  myDict = json.load()

lines = [f'For key "{key}", the value is "{value}".\n' for key, value in myDict.items()]



with open("output/formattedTxt.txt", 'w') as f:
  f.write("\n".join(lines))
  
