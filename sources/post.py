import glob
from pathlib import Path
from fontTools.ttLib import TTFont

for file in Path("fonts").glob("**/*.ttf"):
	font = TTFont(str(file))
	if font["gasp"].gaspRange != {65535: 0x000A}:
		font["gasp"].gaspRange = {65535: 0x000A}

	if "variable" in str(file):
		font["name"].setName("42dot Sans",1,3,1,1033)
		font["name"].setName("42dot Sans Regular",4,3,1,1033)
		font["name"].setName("42dotSans-Regular",6,3,1,1033)
	
	try:
		del font["prep"]
	except KeyError:
		pass

	font.save(file)