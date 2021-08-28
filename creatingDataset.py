import pandas as pd
import numpy as np
import os
import re
from datetime import datetime

whatsAppTexts = raw_input('Do you have any whatsAppTexts to parse (y/n?)')
hangoutsTexts = raw_input('Do you have an hangoutsTexts to parse (y/n)?')

def getWhatsAppData():
    personName = raw_input("Enter your name in WhatsApp: ")
    df = pd.read_csv('whatsapp_chats.csv')
    responsesDict = dict()
    receivedtexts = df[df['From']!=personName]
    senttexts = df[df['From']==personName]
    alltexts = pd.concat([senttexts, receivedtexts])
    otherPersonsMessage, myMessage = "",""
    firsttext = True
    for index,row in alltexts.iterrows():
        if(row['From']!=personName):
            if myMessage and otherPersonsMessage:
                otherPersonsMessage = cleantext(otherPersonsMessage)
                myMessage = cleantext(myMessage)
                responsesDict[otherPersonsMessage.rstrip()] = myMessage.rstrip()
                otherPersonsMessage, myMessage = "",""
            otherPersonsMessage = otherPersonsMessage + str(row['Content']) + " "
        else:
            # To exclude convos when I initiate it
            if (firsttext):
                firsttext = False
                continue
            myMessage = myMessage + str(row['Content']) + " "
    return responsesDict

def getHangoutsData():
    personName = raw_input("Enter your full Hangouts name: ")
    allFiles = [] #List of file names

    for filename in os.listdir('GoogleTexts'):
        if filename.endswith(".txt"):
            allFiles.append('GoogleTexts/'+ filename)

    responsesDict = dict()

    # Key is other person's name and value is my reply
    # This records their texts to me and my replies to them

    for currentFile in allFiles:
        myMessage, otherPersonsMessage, currentSpeaker = "","",""
        with open(currentFile,'r') as openedFile:
            allLines = openedFile.readlines()
        for index, lines in enumerate(allLines):
            #senders name is sep. by < >
            leftBracket = lines.find('<')
            rightBracket = lines.find('>')

            # messages I sent
            if(lines[leftBracket+1: rightBracket]==personName):
                if not myMessage:
                    # if not the first of multiple texts i senttexts
                    startMessageIndex = index -1
                myMessage += lines[rightBracket+1:]

            elif myMessage:
                # To find messages that others sent for which I replied
                #So we need to check previous messages by decrementing indices

                for counter in range(startMessageIndex,0,-1):
                    currentLine = allLines[counter]
                    #if message isnt formatted
                    if(currentLine.find('<')<0 or currentLine.find('>') < 0):
                        myMessage, otherPersonsMessage, currentSpeaker = "","",""
                        break
                    if not currentSpeaker:
                        currentSpeaker = currentLine[currentLine.find('<')+1:currentLine.find('>')]
                    elif (currentSpeaker != currentLine[currentLine.find('<')+1:currentLine.find('>')]):
                        otherPersonsMessage = cleantext(otherPersonsMessage)
                        myMessage = cleantext(myMessage)
                        responsesDict[otherPersonsMessage] = myMessage
                        break
                    otherPersonsMessage = currentLine[currentLine.find('>')+1:] + otherPersonsMessage
                myMessage, otherPersonsMessage,currentSpeaker="","",""
    return responsesDict

def cleantext(text):
    cleaned = text.replace('\n',' ').lower()
    cleaned = cleaned.replace("\xc2\xa0","")
    cleaned = re.sub('([.,!?])','',cleaned)
    cleaned = re.sub(' +',' ',cleaned)
    return cleaned

combinedDict ={}
if(hangoutsTexts == 'y'):
    print("Getting Hangouts Texts")
    combinedDict.update(getHangoutsData())
if(whatsAppTexts=='y'):
    print("Getting WhatsApp Texts")
    combinedDict.update(getWhatsAppData())
print 'Total length of dictionary', len(combinedDict)

print('Saving conversations...')
np.save('conversationDictionary.npy', combinedDict)

conversationFile = open('conversationData.txt','w')
for key, value in combinedDict.items():
    if (not key.strip() or not value.strip()):
        continue #empty strings
    conversationFile.write(key.strip() + value.strip())
