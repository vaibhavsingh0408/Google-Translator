from tkinter import *
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from tkinter.ttk import Combobox
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image,ImageTk
import pytesseract
import cv2

t=Tk()
t.geometry("1350x750+0+0")
t.title('translator')
def translator():
    if combo.get()=='hindi':

        result=textvalue.get()
        p = Translator()
        k = p.translate(result, dest='hi')
        l=k.text

        s.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo.get()=='english' :

        result=textvalue.get()
        p=Translator()
        k=p.translate(result,dest='en')
        l=k.text
        s.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo.get()=='urdu':
        result=textvalue.get()
        p=Translator()
        k=p.translate(result,dest='ur')
        l=k.text
        s.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo1.get()=='urdu':
        result=s.get()
        p=Translator()
        k=p.translate(result,dest='ur')
        l=k.text
        textvalue.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo.get()=='france':
        result=textvalue.get()
        p=Translator()
        k=p.translate(result,dest='fr')
        l=k.text
        s.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo1.get()=='france':
        result = textvalue.get()
        p = Translator()
        k = p.translate(result, dest='fr')
        l = k.text
        textvalue.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo1.get()=='english':
        result =s.get()
        p=Translator()
        k=p.translate(result,dest='en')
        l=k.text
        textvalue.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()
    elif combo.get=='italian':
        result=textvalue.get()
        p=Translator()
        k=p.translate(result,dest='it')
        l=p.text
        s.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()

    elif combo1.get()=='italian':
        result=s.set()
        p=Translator()
        k=p.translate(result,dest='it')
        l=k.text
        textvalue.set(l)
        engine = pyttsx3.init()
        engine.say(l)
        engine.runAndWait()

    else:
        notification.set('First select the language')


def speak():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('say something')
        notification.set('say something')
        audio=r.listen(source)
        print('done')
        notification.set('done')
    text=r.recognize_google(audio)
    textvalue.set(text)

def searching():
    if option.get()=='Browser link':

        response = urllib.request.urlopen(browser.get())
        h = response.read()
        soup = BeautifulSoup(h, 'html5lib')
        text = soup.get_text(strip=False)
        print(text)
        textvalue.set(text)
    elif option.get()=='Image Link':
        img=Image.open(browser.get())
        notification.set(img)
        pytesseract.pytesseract.tesseract_cmd='E:/Tesseract-OCR/tesseract.exe'
        result=pytesseract.image_to_string(img)
        textvalue.set(result)
    else:
        notification.set('PLEASE SELECT OPTION')
def capture():
   
    
    import cv2

    cap = cv2.VideoCapture(0)

    count=0
    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("img", img)
        k = cv2.waitKey(30) & 0xFF
    
        if k == ord('q'):
        
            cv2.imwrite("C:/Users/pc1/Desktop/"+str(count)+"id.png",img)
            
            a="C:/Users/pc1/Desktop/"+str(count)+"id.png"
            
            count=count+1
        #break
        elif k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()   
    import ocrspace
    api = ocrspace.API()

    api = ocrspace.API('enter your OCR-API', ocrspace.Language.Croatian)

    api.ocr_file(a)

    a=api.ocr_file(open(a, 'rb'))
    textvalue.set(a)

v=['blank','hindi','english','france','urdu','italian']
combo=Combobox(t,values=v,width=35)
combo.set('select language')
combo.place(x=190,y=160)
combo1=Combobox(t,values=v,width=35)
combo1.set('select language')
combo1.place(x=890,y=160)
Label(t,text="VIET ",font="Ebrima 50 bold").place(x=590,y=0)
Label(t,text="TRANSLATOR",font="Ebrima 10 bold").place(x=620,y=80)

#------------------------------------------------------

textvalue=StringVar()
textentry=Entry(t,textvariable=textvalue,font='Ebrima 30',width=20,bd=5).place(x=100,y=260)
s=StringVar()
notification=StringVar()
T = Entry(t,textvariable=s, font='Ebrima 30', width=20,bd=5).place(x=800, y=260)
#-----------------

trans=Button(t,text='Translate',command=translator,font="Ebrima 11 bold",bd=5).place(x=700,y=360)
voice=Button(t,command=speak,text='VOICE',font='Ebrima 11 bold',bd=5).place(x=600,y=360)
#---------------------notificatiion-------------------
Label(t,text="NOTIFICATION SCREEN",font='Ebrima 15 bold').place(x=200,y=500)
noti=Entry(t,textvariable=notification,bd=5,font='Ebrima 10 bold',width=40).place(x=510,y=500)

#----------------------------browser an image-----------------------------------------

Label(t,text='BROWSER AND IMAGE LINK',font='Ebrima 20 bold').place(x=100,y=550)
o=['Browser link','Image Link']
option=Combobox(t,values=o,width=35)
option.set('Select any one option')
option.place(x=100,y=600)
browser=StringVar()
brows=Entry(t,textvariable=browser,font='52',bd=5,width=50).place(x=400,y=600)
search=Button(t,command=searching,bd=5,font='Ebrima 10 bold',text='search').place(x=900,y=598)
#-----------------------------------------------
pic=Button(t,command=capture,bd=5,font="Ebrima 11 bold",text='capture').place(x=800,y=360)
#---------------------------------------
t.mainloop()




