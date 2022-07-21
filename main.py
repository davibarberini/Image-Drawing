import math
from PIL import Image


# Image resolution and ratio
imgWidth = 120
imgHeight = 60


# Choose dices | cards | dominó pieces
# caracterMap = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# caracterMap = ["🂱", "🂲", "🂳", "🂴", "🂵", "🂶", "🂷", "🂸", "🂹", "🂺"]
caracterMap = ["🁣", "🁫", "🁳", "🁻", "🂃", "🂋", "🂓"]

# Comment this to have less darker images
caracterMap.insert(0, "'")

divisionValue = 255 / (len(caracterMap) - 1)

# Some images are better with the reverse effect
# caracterMap.reverse()

diceImage = []

# Checking every pixel of the image
im = Image.open('./teste.png')
im = im.convert('RGBA')
im = im.resize((imgWidth, imgHeight), Image.Resampling.LANCZOS)
pix = im.load()
for y in range(imgHeight):
  for x in range(imgWidth):
    r, g, b, a = pix[x, y]
    average = (r + g + b) / 3
    diceImage.append(caracterMap[math.floor(average / divisionValue)])
    

# Parsing from array to a string with spacing
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

# Writing the result on a txt file
text_file = open("./result.txt", "w")
text_file.write(finalString)
text_file.close()