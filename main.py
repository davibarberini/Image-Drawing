import math
from PIL import Image


# Image resolution and ratio
imgWidth = 120
imgHeight = 60


# Choose dices | cards | dominó pieces | add a new list yourself
# caracterMap = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# caracterMap = ["🂱", "🂲", "🂳", "🂴", "🂵", "🂶", "🂷", "🂸", "🂹", "🂺"]
caracterMap = ["🁣", "🁫", "🁳", "🁻", "🂃", "🂋", "🂓"]

# Comment this to have less darker images
caracterMap.insert(0, "'")

divisionValue = 255 / (len(caracterMap) - 1)

# Some images are better with the reverse effect
# All it does is reverse the string in a way that the darker value will be the first one
caracterMap.reverse()


# Opening the image
im = Image.open('./test.png')

# Comment this line if gives any error, some images doesn't need to be converted
im = im.convert('RGBA')

# Resizing the image to the resolution defined above
im = im.resize((imgWidth, imgHeight), Image.Resampling.LANCZOS)

# Checking every pixel of the image
diceImage = []
pix = im.load()
for y in range(imgHeight):
  for x in range(imgWidth):
    # Getting the average value of how light is the pixel based on the rgb value
    r, g, b, a = pix[x, y]
    average = (r + g + b) / 3
    # Adding the value to a list instanciated above, the value maps between the size of the caraterMap list and gets the value accordingly
    # If average = 255 then the caracter will be the last item of the caracterMap, if average = 0 it will be the first one
    diceImage.append(caracterMap[math.floor(average / divisionValue)])
    

# Parsing from array to a string
# After imgWidth number of caracters we add a \n to go to the next line
finalString = ''
count = 0
for p in diceImage:
  finalString += p
  count += 1
  if count >= imgWidth:
    finalString += "\n"
    count = 0

# Printing the result on the console
print(finalString)

# Writing the result on a txt file for better visualization
text_file = open("./result.txt", "w")
text_file.write(finalString)
text_file.close()