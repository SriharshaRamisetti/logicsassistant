import subprocess
import screen_brightness_control as sbc
import pyautogui as pygui
import pyttsx3 as p
import datetime as dt
import random as r
import speech_recognition as sr
import webbrowser  as wb
import pyjokes
import tkinter as tk
import time

sp=p.init()
def speak(text):#this is speak function which will gives a speech output for a text input
    rate=sp.setProperty('rate',150)
    sp.say(text)
    sp.runAndWait()
#----------

def wish():#this is a function which will wish you according to the time
    m=int(dt.datetime.now().hour)
    if m>=6 and m<=12:
        speak('good morning')
    elif m>=13 and m<=15:
        speak('good afternoon')
    elif m>=16 and m<=18:
        speak('good evening')
    else:
        speak('good night')
#--------------

b=0
def audioinput():
    time.sleep(8)
    global b
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=1000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening.....')
        audio=r.listen(source)
    try:
        print("identifying........")
        text=r.recognize_google(audio)
        return text
    except Exception as e:#this exception will be executed if any errors occurs in finding audio into text
        print(e)
        speak('unable to recognize due to some error')
        print('unable to recognize')
        b=b+1
        speak('can you please enter it in text:')
        text=input('can you please enter it in text:')
        return text
        
    return text
#----------------------------------------------

system_name="logics"

#this is the function which is used to send email
def gmailsend():
    z=pygui.confirm(text='Have you done all required login procedures through your email or else it wont work',title='reminder',buttons=['yes','no'])
    if z=='yes':
        c=input('enter the receiver email address:')
        subject=input('subject:')
        content=input('content:')
        time.sleep(2)
        pygui.hotkey('win','s')
        speak('dont disturb me i am sending your mail')
        
        pygui.typewrite('mail',0.01)
        
        pygui.press('enter')
        time.sleep(2)
        pygui.hotkey('win','up')
        time.sleep(5)
        pygui.click(1,100,2,0.01,button='left')
        time.sleep(6)
        pygui.click(1150,180,2,0.01,button='left')
        pygui.typewrite(c,0.01)

        time.sleep(2)
        pygui.click(1150,235,2,0.01,button='left')#the values in the click are the locations of the specific app are icon according to my pc
        pygui.typewrite(subject,0.01)
        time.sleep(2)
        pygui.click(1150,265,2,0.01,button='left')
        pygui.typewrite('  '+str(content),0.01)
        time.sleep(2)
        pygui.click(1300,50,2,0.01,button='left')
        time.sleep(2)
        speak('your email has sent successfuly')
        try:
            pygui.hotkey('alt','f4')
        except:
            speak("unexpected error occurred please try after sometime")
        print('email sent successfully')
#--------------

#this function is used with the help of ctypes
def changebackground():
    z=[[441,500],[556,499],[603,493],[707,465]]
    rands=r.choice(z)
    pygui.hotkey('win','s')
    pygui.typewrite('wallpaper',0.02)
    pygui.press('enter')
    time.sleep(2)
    pygui.hotkey('win','up')
    time.sleep(2)
    pygui.click(rands[0],rands[1],1,0,button='left')
    time.sleep(4)
    pygui.hotkey('alt','f4')
#-----------

#this function is used for getting jokes using a python module pyjokes
def jokes():
    c=pyjokes.get_jokes()
    c=c[r.randint(1,len(c))]
    speak(c)
    print(c)
#----------
def capturing(text):#works for all systems
    if 'record' in text:
        time.sleep(3)
        pygui.hotkey('win','s')
        pygui.typewrite('camera',0.01)
        time.sleep(2)
        pygui.press("enter")
        time.sleep(2)
        pygui.hotkey('win','up')
        time.sleep(4)
        pygui.press('up')
        pygui.press('up')
        time.sleep(2)
        pygui.hotkey('up','up')
        speak('see me')
        pygui.press('enter')
        time.sleep(8)
        pygui.click(1300,0,2,0,button='left')
    elif 'pic' in text:
        time.sleep(3)
        pygui.hotkey('win','s')
        pygui.typewrite('camera',0.01)
        pygui.press('enter')
        time.sleep(4)
        pygui.hotkey('win','up')
        time.sleep(2)
        pygui.press('down')
        for i in range(3,0,-1):
            speak(i)
        speak('say cheers')
        pygui.press('enter')
        time.sleep(2)
        pygui.hotkey('alt','f4')
    else:
        speak('i cant get it')
#-----------------------------------------------------------------------------------
#this function is used to open any applications in computer with a module pyautogui
def open_applications(inputs):
    if 'open' in inputs:
        inputs=inputs.replace('open','')
    elif 'search' in inputs:
        inputs=inputs.replace('search','')
    pygui.hotkey('win','s')
    pygui.typewrite(inputs,0.01)
    time.sleep(2)
    pygui.press('enter')
    time.sleep(2)
    pygui.hotkey('win','up')
#---------------------------------------------------------
#this function is used to browse the information which we have given to the voice assistant to search
def browse_web(inputs):
    try:
        import pywhatkit as pw
        if 'in incognito' in inputs:
            webdriver= wb.open('www.google.com')
            inputs = inputs.replace('incognito' ,'')
            if 'search' in inputs:
                if 'google' in inputs:
                    inputs=inputs.replace('search','')
                    inputs=inputs.replace('google','')
                if 'in' in inputs:
                    inputs=inputs.replace('in','')
                time.sleep(10)
                pygui.hotkey('ctrl','shift','n')
                pygui.typewrite(inputs,0.01)
                pygui.press('enter')
        elif 'send' in inputs:
            if 'whatsapp' in inputs:
                speak('enter the receiver details:')
                number=input('receiver number(with country code):')
                msh=input('message to send:')
                times = input('hours:')
                minutes=input('minutes:')
                try:
                    pw.sendwhatmsg(number,msh,int(times),int(minutes))
                        
                    pygui.press('enter')
                except Exception as e:
                    print(e)
        elif 'play' in inputs:
            if 'youtube' in inputs:
                    #speak('on what topic you need  a search operation')
                inputs=inputs.replace('play','')
                inputs=inputs.replace('youtube','')
                if 'randomvideo' in inputs:
                    inputs=inputs.replace('video','')
                try:
                    pw.playonyt(inputs)
                    speak('showing your results........')
                except Exception as e:
                    print(e)
        elif 'get' in inputs:
            if 'information' in inputs:
                inputs=inputs.replace('get','')
                inputs=inputs.replace('information','')
                try:
                    pw.info(inputs,lines=4)
                except Exception as e:
                    print(e)
        elif 'search' in inputs:
            if 'google' in inputs:
                inputs=inputs.replace('google','')
                inputs=inputs.replace('search','')
                try:
                    pw.search(inputs)
                except Exception as e:
                    print(e)
    except Exception as e:
        print('ERROR:'+str(e))
#---------------------------------------------------------
def playamovie():
    z=[[860,443],[847,578],[734,418],[316,476],[448,446],[238,572],[541,588],[478,595],[342,579],[565,416],[666,424],[651,566],[760,580],[966,584],[1066,601],[1206,591],[956,428],[1292,580],[1189,458],[1315,457]]
    ra=r.choice(z)
    pygui.hotkey('win','r')
    pygui.typewrite('explorer',0.01)
    pygui.press('enter')
    time.sleep(5)
    pygui.hotkey('win','up')
    time.sleep(4)
    pygui.click(300,147,2,0.01,button='left')
    pygui.typewrite('movies',0.01)
    pygui.press('enter')
    time.sleep(5)
    pygui.click(ra[0],ra[1],2,0.01,button='left')
#-----------------------------------------------------------------------------------------------

#this is the function which will show you a digital clock
def clock():
    current=time.strftime("%H:%M:%S")
    label1['text']=current
    root.after(1000,clock)
root=tk.Tk()
root.title('Digital clock')
label1=tk.Label(root,font='article 80',bg='black',fg='blue')
label1.grid(row=0,column=0)
#-------------------------------------------------------
#this function is used to activate or deactivate wifi or airplane mode
number_of_clicks=0
number_of_clicksairplane=0
def clicking(inputz):
    inputs=list(map(str,inputz.split(' ')))
    global number_of_clicks
    global number_of_clicksairplane
    if 'wifi' in inputs[-1].lower().replace('-',''):
        if inputs[0]=='activate' and number_of_clicks==0:
            
            number_of_clicks=number_of_clicks+1
            pygui.click(1163,743,1,0,button='left')
            time.sleep(2)
            pygui.click(1050,705,1,0,button='left')
            print('activated')
        elif inputs[0]=='deactivate' and number_of_clicks==1:
            
            number_of_clicks=number_of_clicks-1
            pygui.click(1163,743,1,0,button='left')
            time.sleep(2)
            pygui.click(1050,705,1,0,button='left')
            print('deactivated')
        elif inputs[0]=='activate':
            print('already activated')
        elif inputs[0]=='deactivate':
            print('already deactivated')
    elif 'airplane' in inputs[-1].lower().replace(' ',''):
        if inputs[0]=='activate' and number_of_clicksairplane==0:
           
            number_of_clicksairplane=number_of_clicksairplane+1
            pygui.click(1163,743,1,0,button='left')
            time.sleep(2)
            pygui.click(1114,706,1,0,button='left')
            print('activated')
        elif inputs[0]=='deactivate' and number_of_clicksairplane==1:
            
            number_of_clicksairplane=number_of_clicksairplane-1
            pygui.click(1163,743,1,0,button='left')
            time.sleep(2)
            pygui.click(1114,706,1,0,button='left')
            print('deactivated')
        elif inputs[0]=='activate':
            print('already activated')
        elif inputs[0]=='deactivate':
            print('already deactivated')
    elif 'notifications' in inputz.lower():
        if 'display' in inputz.lower():
            pygui.hotkey('win','a')
            time.sleep(5)
            pygui.hotkey('win','a')
        elif 'show' in inputz.lower():
            pygui.hotkey('win','a')
            time.sleep(5)
            pygui.hotkey('win','a')
        else:
            q=pygui.confirm(text='do you want to display notifications?',title='reminder',buttons=['yes','no'])
            if q=='yes':
                clicking('show notifications')
    else:
        print('i cant understand')
        speak('i can\'t understand')
#-----------------------------------------------------------

#this is a function which will give you a boost up a little from now\
def motivate_me():
    z=['Crying doesnt mean your are weak.Since birth,it\'s been a sign that you are alive','remember that your are capable,brave and loved-even when it feels like you are not',
       'Be proud of who you are ,instead of ashamed of how someone else sees you','never ever ever give up on yourself','when you feel low talk to your mother everthing will become alright',
       'love yourself first,then  every thing loves you','even the worst depressive episodes won\'t last forever','Right now,stop whatever you are doing and think of all the things in life that you are grateful for.This is a really easy way to lift your mood!',
       'Having depression does not mean you are weak , a failure or worth less than anybody else.please,don\'t discriminate against ypurself',
       'you are brave,courageous and strong for continuing to fight an illness that nobody else can see',
       'Never put the key to your happiness in someone else\'s pocket']
    rand=r.choice(z)
    print(rand)

    speak(rand)

#-----------------------------------------------------------------------------------------------------
##########################################-M-A-I-N-+-C-O-D-E-#########################################
#-----------------------------------------------------------------------------------------------------
print('❤ 😎'*40)
speak('hello i am your voice assistant:'+str(system_name))
wish()
while True:
    #z=audioinput()
    z=input('enter your command:').lower()
    #l=list(map(str,z.split(' ')))
    if z=='hi' or z=='hello':
        speak('hello nice to meet you')
    elif 'iloveyou' in z.replace(' ',''):
        speak('is it? i am so lucky to have you')
    elif 'loveyou' in z.replace(' ',''):
        speak('is it? i am so lucky to have you')
    
    elif 'whatislove' in z.replace(' ',''):
        speak('it can be found only from your mother')
    elif 'what is your name' in z:
        print('my name is :'+system_name)
        speak('my name is :'+system_name)
    elif 'googlesearch' in z.replace(' ',''):
        browse_web(z)
    elif 'youtube' in z:
        browse_web(z)
    elif 'whatsapp' in z:
        browse_web(z)
    elif 'get' in z:
        browse_web(z)
    elif 'record' in z:
        capturing(z)
    elif 'capture' in z:
        capturing(z)
    elif 'tellmeajoke' in z.replace(' ',''):
        jokes()
    elif 'motivateme' in z.replace(' ',''):
        motivate_me()
    elif 'digitalclock' in z.replace(' ',''):
        clock()
        root.mainloop()
    elif z=='exit' or z == 'quit' :
        speak('okay thank you for speanding your valuable time with me  byeee')
        #print('okay thank you for speanding your valuable time with me byee')
        print('❤'*40)
        break
    elif 'tellaboutme' in z.replace(' ',''):
        praise_me=['you are so gorgeous creature in the world','you are the most beautiful creature across the globe',
                   'i am so lucky, as i met you','you are soo nice human in my view','your prespective on life makes me want to live more thoughtfully','you make me laugh so much-i love how you hit the perfect tone and expression everytime',
                   'i admire your determination when you strongly believe in something','i feel heard and seen when we have difficult conversations','i appreciate your patience','your are like a torch barrier to some group of people']
        z=r.choice(praise_me)
        speak(str(z))
        print(str(z))
    elif 'willyoubemymate' in z.replace(' ',''):
        speak("aah! i am so confused")
        print("aah! i am so confused")
    elif 'willyoubemyvalentine' in z.replace(' ',''):
        speak('it will be weird for viewers')
        print('it will be weird for viewers')
    elif 'okay' in z:
        speak("nice to here")
        print('nice to here')
    elif 'changebackground' in z.replace(' ',''):
        changebackground()
        speak('background changed successfully')
        print('background changed successfully')
    elif 'wishme' in z.replace(' ',''):
        wish()
    elif 'wifi' in z:
        clicking(z)
    elif 'airplane' in z:
        clicking(z)
    elif 'notifications' in z:
        clicking(z)
    elif 'tictactoe' in z.replace(' ',''):
        ins=pygui.confirm(text='i have only one feature that is person versuses person is it ok for you?',title='reminder',buttons=['ok','cancel'])
        if ins == 'ok':
            import tictactoe
        else:
            pass
    elif 'please' in z:
        input('what happen to you:')
        motivate_me()
    elif 'staywithme' in z.replace(' ',''):
        speak('always and forever,i will become a permanent person to support you in this temporary world')
        print("always and forever,i will become a permanent person to support you in this temporary world")
    elif 'playarandommovie' in z.replace(' ',''):
        playamovie()
    elif 'displayscreenbrightness' in z.replace(' ',''):
        print(sbc.get_brightness())
    elif 'screenbrightness' in z.replace(' ',''):
        bright=sbc.get_brightness()
        #speak('do you want to increase or decrease the brightness')
        while True:
            if 'increase' in z.replace(' ',''):
                bright[0]=bright[0]+5
                sbc.fade_brightness(bright[0],interval=0.01)
                print(sbc.get_brightness())
                v=input('is it enough or not:')
                if v=='enough':
                    break
                elif v=='not':
                    if bright[0]<100:
                        bright[0]=bright[0]+5
                        sbc.fade_brightness(bright[0],interval=0.01)
                    else:
                        print('it has already reached maximum')
                        break
            elif 'decrease' in z.replace(' ',''):
                bright[0]=bright[0]-10
                sbc.fade_brightness(bright[0],interval=0.01)
                print(sbc.get_brightness())
                v=input('is it enough or not:')
                if v=='enough':
                    break
                elif v=='not':
                    if bright[0]>1:
                        bright[0]=bright[0]-10
                        sbc.fade_brightness(bright[0],interval=0.01)
                    else:
                        print('it has already reached minimum')
                        break
    elif 'shutdown' in z.replace(' ',''):
        z1z=pygui.confirm(text='system is shutting down',title='reminder',buttons=['ok','close'])
        if z1z=='ok':
            speak('hold on a second your system is about to shut down')
            print('shuting down')
            subprocess.call('shutdown /p /f')
        else:
            pass
    elif 'sleep' in z:
        speak('hold on your system is about to sleep')
        print('sleeping..........')
        subprocess.call('shutdown /h')
    elif 'restart' in z:
        z1z2=pygui.confirm(text='you system is about to restart',title='reminder',buttons=['ok','close'])
        if z1z2=='ok':
            speak('hold on your system is about to restart')
            print('restarting.........')
            subprocess.call(['shutdown','/r'])
        else:
            pass
    elif 'hibernate' in z:
        speak("hold on your system is about to hibernate")
        print('hibernating.......')
        subprocess.call('shutdown /h')
    elif 'email' in z:
        gmailsend()
    elif 'open'in z:
        open_applications(z)
    else:
        if b>=4:
            speak('your internet connection is low,try again when internet connection is stable')
            print('your internet connection is low,try again when internet connection is stable')
            break
        else:
            speak('i can\'t understand, can you please repeat it again')
            print('i can\'t understand, can\ you please repeat it again')