import pyttsx3
import PyPDF2

book= open('The Alchemist.pdf','rb')
pdf_reader= PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
#print(pages)



speaker = pyttsx3.init()

rate = speaker.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
speaker.setProperty('rate', 130)     # setting up new voice rate


voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

for num in range(0,pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

