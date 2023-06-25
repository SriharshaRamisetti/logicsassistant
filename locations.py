import random as r
import time
import pyautogui as pygui
print(pygui.position())
z=[[860,443],[847,578],[734,418],[316,476],[448,446],[238,572],[541,588],[478,595],[342,579],[565,416],[666,424],[651,566],[760,580],[966,584],[1066,601],[1206,591],[956,428],[1292,580],[1189,458],[1315,457]]
ra=r.choice(z)
print(ra[0],ra[1])
pygui.hotkey('win','e')
#pygui.click(124,748,1,0,button='left')
#pygui.typewrite('explorer',0.01)
#pygui.press('enter')
time.sleep(4)
pygui.hotkey('win','up')
time.sleep(2)
pygui.click(481,301,2,0.01,button='left')
time.sleep(4)
pygui.click(ra[0],ra[1],2,0.01,button='left')
print(ra)
#860,443 movie of julay
#847,578 is the location of anando brahma
#734,418 movie of iddharammalathos
#124,748 is the location of start search button
#481,301 is the location of movies and songs in explorer
'''pygui.click(124,748,1,0,button='left')
pygui.typewrite('explorer',0.01)
pygui.press('enter')
time.sleep(3)
pygui.click(481,301,2,0.01,button='left')
time.sleep(3)
pygui.click(860,443,2,0.01,button='left')
'''
#316,476 is location of adhurs
#(x=448, y=446) location of anabelle
#(x=238, y=572) location of prette2016
#(x=541, y=588) location of syee ra
#(x=478, y=595) location of svsc
#(x=342, y=579) location of racegurram#(x=565, y=416) location of baadhshah
#x=666, y=424) location of Ghazi
#(x=651, y=566) location of KHAIDI
#(x=760, y=580) location of hoobs shadow
#(x=966, y=584) location of lie
#x=1066, y=601) location of nenu local
#(x=1206, y=591) location of sarrainodu
#(x=956, y=428) location of london
#(x=1292, y=580) location of nene raju nene manthri
#(x=1189, y=458) location of mirchi
#(x=1315, y=457) location of nenu sailaja
