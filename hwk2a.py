def showTwoPictures():
  file=pickAFile()
  pic=makePicture(file)
  show(pic)
  file=pickAFile()
  pic=makePicture(file)
  show(pic)
def printInvite():
  print "party tonight!"
  print "all are welcome"
def printDisclaimer():
  print "you must be over the age of 22 and under the age of 35 to attend"
  print "if you arrive late you will asked to leave as soon as the sun sets"
  print "pets are welcome if they like to bark and hop"
  print "the party is free minus the 45 dollar entrance charge and the 3 dollar hello fee"

def printFullInvite():
  print printInvite()
  print printDisclaimer()