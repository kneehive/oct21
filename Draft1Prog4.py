# Roo Lerner
# Programming Assignment 4
# Sunday, October 16

from graphics import *
from random import randrange
from time import sleep

def main():
    wFreq = {}
    stopfile = open("stopwords.txt", "r", encoding="utf-8")
    stopwords = stopfile.read()
    stopwords = stopwords.upper()
    donaldfile = open("DonaldSpeech2016.txt", "r", encoding="utf-8")
    donaldfile = donaldfile.read()
    donaldfile = donaldfile.upper()

    win = GraphWin("Words and Clouds!", 600, 600)
    win.setCoords(-1, -1, 100, 100)

    exit = drawButton(win,Point(85,5), Point(95,15), "Exit")
    gotime = drawButton(win,Point(40,40),Point(60,60),"Go!")
    prompt = Text(Point(50,35),"Type a file name, then click anywhere to see your word cloud!")
    prompt.draw(win)
    prompt.setFill("Purple")
    inputBox = Entry(Point(50,30),70)
    inputBox.draw(win)



    pt = win.getMouse()
    while not (40 <= pt.getX() <= 60 and 40 <= pt.getY() <= 60):
        if (85 <= pt.getX() <= 95 and 5 <= pt.getY() <= 15):
            win.close()
        else:
            pt = win.getMouse()


    usertext = inputBox.getText()
    #use donald speech as default file in the absence of user input
    if usertext [-4:]!= ".txt":
        subjectFile = donaldfile
    elif usertext[-4:40] == ".txt":
        subjectFile = usertext

    # establish an empty dictionary of word frequencies

    punct = "’!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~'"

    for char in punct:
        subjectFile = subjectFile.replace(char, "")

    originalwordlist = subjectFile.split()
    stopwordlist = stopwords.split("\n")

    for word in stopwordlist:
        while word in originalwordlist:
            originalwordlist.remove(word)

    for word in originalwordlist:
        if not (word in wFreq):
            wFreq[word] = 1 # establish entry in dictionary for this new word
        else: # otherwise, add one to the number of times this word occurs
            wFreq[word] = wFreq[word]+1

    seq = wFreq.items()
    wordList = list(seq)
    wordList.sort(key=getFreq, reverse = True)
    topList = wordList[:20]

    lowestScore = topList[19][1]
    collisionlist = []

    sleep(.1)
    # undraw the current objects (except the exit button) so they don't overlap with the word cloud
    inputBox.undraw()
    prompt.undraw()
    gotime.undraw()

    for item in topList:
        size = int(12*(item[1] / lowestScore))
        red = randrange(0,255)
        green = randrange(0,55)
        blue = randrange(0,255)
        color = color_rgb(red,green,blue)


        anchor = randomizeAnchor()
        iscoll = isCollision(collisionlist, anchor)
        while (iscoll == False):
            anchor = randomizeAnchor()
            iscoll = isCollision(collisionlist, anchor)

        collisionlist.append(anchor)

        depiction = Text(anchor, item[0])
        depiction.setFill(color)
        depiction.setSize(size)

        # using lowest score, calculate percentage increase of each word from that frequency
        depiction.draw(win)


    pt = win.getMouse()
    while not (85 <= pt.getX() <= 95 and 5 <= pt.getY() <= 15):
        pt = win.getMouse()

    win.close()

def isCollision(collisionlist, curranchor):
    pixeldistance = 10
    for pastanchor in collisionlist:
        if abs(pastanchor.getX() - curranchor.getX()) < pixeldistance and abs(pastanchor.getY() - curranchor.getY()) < pixeldistance:
            return False
    return True

def randomizeAnchor():
    xanchor = randrange(15,85)
    yanchor = randrange(25,90)
    return Point(xanchor,yanchor)




def getFreq(listItem):
    return listItem[1]

    # We will do this like the letter frequency in Lab 7
    # Fill the dictionary with (non-stop) words and their frequencies
    # Then, use those dictionary entries to inform graphics of how to generate
    # The word cloud that will be displayed

    # if the user doesn't desire to enter a file ,establish default


def drawButton(gwin, pt1, pt2, word):
    button = Rectangle(pt1, pt2)
    button.setFill("black")
    button.draw(gwin)
    center = Point((pt1.getX() + pt2.getX()) / 2, (pt1.getY() + pt2.getY()) / 2)

    buttonLabel = Text(center, word)
    buttonLabel.setSize(10)
    buttonLabel.setFill("MintCream")
    buttonLabel.draw(gwin)
    #return the rectangle object to undraw it when word cloud is generated
    return button

main()
