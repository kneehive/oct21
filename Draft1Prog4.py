#Roo Lerner
#Programming Assignment 4
#Sunday, October 16

from graphics import *
from random import randrange

def main():
    #establish an empty dictionary of word frequencies
    wFreq = {}
    stopfile = open("stopwords.txt", "r", encoding = "utf-8")
    stopwords = stopfile.read()
    stopwords = stopwords.upper()
    donaldfile = open("DonaldSpeech2016.txt", "r", encoding = "utf-8")
    donaldspeech = donaldfile.read()
    donaldspeech = donaldspeech.upper()
    punct = "’!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~'"

    for char in punct:
        donaldspeech = donaldspeech.replace(char, "")

    donaldwordlist = donaldspeech.split()
    stopwordlist = stopwords.split("\n")

    for word in stopwordlist:
        while word in donaldwordlist:
            donaldwordlist.remove(word)

    for word in donaldwordlist:
        if not (word in wFreq):
            wFreq[word] = 1 #establish entry in dictionary for this new word
        else: #otherwise, add one to the number of times this word occurs
            wFreq[word] = wFreq[word]+1

    seq = wFreq.items()
    wordList = list(seq)
    wordList.sort(key=getFreq, reverse = True)
    topList = wordList[:30]
    tier1List = topList[:10]
    tier2List = topList[11:20]
    tier3List = topList[21:30]

    win = GraphWin("Words and Clouds!", 600, 600)
    win.setCoords(-1, -1, 100, 100)
    #drawButton(win, Point(10, 20), Point(30, 30), "Wanna cookie?")
    drawButton(win,Point(85,85), Point(95,95), "Exit")

    lowestScore = topList[29][1]

    for item in topList:
        print(item)
        location = Point(randrange(10, 80), randrange(10, 80))
        depiction = Text(location, item[0])
        sizeIncrease = item[1] / lowestScore
        depiction.setSize(int(12*sizeIncrease))
        #using lowest score, calculate percentage increase of each word from that frequency
        depiction.draw(win)

    # for item in tier1List:
    #     print(item)
    #     location = Point(randrange(5,90),randrange(5,90))
    #     depiction = Text(location,item[0])
    #     depiction.setSize(72)
    #     depiction.draw(win)
    #
    # for item in tier2List:
    #     print(item)
    #     location = Point(randrange(5, 90), randrange(5, 90))
    #     depiction = Text(location, item[0])
    #     depiction.setSize(54)
    #     depiction.draw(win)
    # for item in tier3List:
    #     print(item)
    #     location = Point(randrange(5, 90), randrange(5, 90))
    #     depiction = Text(location, item[0])
    #     depiction.setSize(32)
    #     depiction.draw(win)



    pt = win.getMouse()
    while not (85<=pt.getX()<=95 and 85<=pt.getY()<=95):
            pt = win.getMouse()
    win.close()








def getFreq(listItem):
    return listItem[1]


    #We will do this like the letter frequency in Lab 7
    #Fill the dictionary with (non-stop) words and their frequencies
    #Then, use those dictionary entries to inform graphics of how to generate
    #The word cloud that will be displayed

    #if the user doesn't desire to enter a file ,establish default


def drawButton(gwin, pt1, pt2, word):
    button = Rectangle(pt1, pt2)
    button.setFill("black")
    button.draw(gwin)
    center = Point((pt1.getX() + pt2.getX()) / 2, (pt1.getY() + pt2.getY()) / 2)

    buttonLabel = Text(center, word)
    buttonLabel.setFace("courier")
    buttonLabel.setSize(10)
    buttonLabel.setFill("white")
    buttonLabel.draw(gwin)

main()

