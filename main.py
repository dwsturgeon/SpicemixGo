# import
# appJar, json
import json
from appJar import gui

#import json file for testing
def loadJson():
	with open('SpiceDir.json') as f:
		data = json.loads(f.read())


	Spices = data["Spices"]
	SpiceType = data["SpiceTypes"]
	SpiceMixes = data["SpiceMixes"]

	for x in range(0,len(Spices)):
		print(Spices[x])


# handle button events
def press(button):
	if button == "Cancel":
		app.stop()



def spiceSelect(optionBox):

	options = app.getAllOptionBoxes()
	obTitle = optionBox.title()
	obItem = app.getOptionBox(obTitle)
	

	print(obTitle)
	print(obItem)

	spiceListImpose = list(spiceListOrig)
	spiceListImpose.remove(obItem)
	print(spiceListImpose)
	print(spiceListOrig)

	for x in options.keys():
		spiceVal =  options[x]
		spiceKey = x
		
		#if spiceKey != obTitle:
			#print(spiceListImpose)


loadJson()

spiceListOrig = [
	"-Select-",
	"Tumeric",
	"Garlic",
	"Thyme",
	"Parsley",
	"Black Peppercorn",
	"White Peppercorn",
	"Basil",
	"Oregano",
	"Ginger",
	"Nutmeg",
	"Cinnamon",
	"Cumin",
	"Paprika"
]

spiceListImpose =[]
spiceListNew = []
spiceListNew = spiceListOrig


# create a GUI variable called app
app = gui("SpiceGo", "1000x800")


for x in range(1,7):
	title = "Spice #"+str(x)
	label = app.addLabelOptionBox ( title, spiceListOrig)
	app.setOptionBoxChangeFunction(title, spiceSelect)

# link the buttons to the function called press
app.addButtons(["Cancel"], press)

app.go()