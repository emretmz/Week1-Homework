import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import  Label, Entry, StringVar

import random
score=0
rounds=0

window=tk.Tk()
window.geometry("1000x780")
frame=tk.Frame(window)
frame.pack() 

img_1=Image.open('C:\\Users\\conko\\OneDrive\\Desktop\\vscode_python\\rock_paper_scissors_game\\tas.png')   
img_1=img_1.resize((250, 200), Image.ANTIALIAS)
tas= ImageTk.PhotoImage(img_1) 
 

img_2=Image.open('C:\\Users\\conko\\OneDrive\\Desktop\\vscode_python\\rock_paper_scissors_game\\kagit.png')   
img_2=img_2.resize((250, 200), Image.ANTIALIAS)
kagit= ImageTk.PhotoImage(img_2) 

img_3=Image.open('C:\\Users\\conko\\OneDrive\\Desktop\\vscode_python\\rock_paper_scissors_game\\makas.png')   
img_3=img_3.resize((250, 200), Image.ANTIALIAS)
makas= ImageTk.PhotoImage(img_3) 
 
def player_info():
    def update_text():
        player_name_label.configure(text=player_name.get()) 

    
    player_name_label=tk.Label(window,text="oyuncu adi")
    player_name=StringVar(None)
    player_name_entry=tk.Entry(window,textvariable=player_name,width=20 )
    player_name_entry.pack()

    
        


    btn_pl_name_add=tk.Button(window,text="Add",command=update_text)   
    btn_pl_name_add.pack()
    player_name_label.pack()

player_info()

def choose(secim):
    global rounds
    rounds+=1

    code_of_game(secim)

score=0
def code_of_game(my_choice):
    global score
    global rounds
    listem=['tas','kagit','makas']
    output=random.choice(listem)
    print(f"{rounds} Round")
     
    if rounds<10:
               
        if my_choice=="tas":
            if output=="tas":
                score=score
                print(f"Berabere!Tas tasa! Total Score: {score}") 
            elif output=="makas":
                score+=50
                print(f"50 yeni puan!Tas makasi kirar! Total Score: {score}")
            else:
                score=score    
                print(f"Kaybettiniz! Kagit tasi sarar! Total Score: {score}")
        if my_choice=="kagit":
            if output=="kagit":
                score=score
                print(f"Berabere! Kagit-Kagida! Total Score: {score}") 
            elif output=="tas":
                score+=50
                print(f"50 yeni puan!Kagit tasi sarar! Total Score: {score}")
            else:
                score=score    
                print(f"Kaybettiniz! Makas kagidi keser! Total Score: {score}")
        if my_choice=="makas":
            if output=="makas":
                score=score
                print(f"Berabere! Makas-Makasa! Total Score: {score}") 
            elif output=="kagit":
                score+=50
                print(f"50 yeni puan!Makas kagidi keser! Total Score: {score}")
            else:
                score=score    
                print(f"Kaybettiniz! Tas makasi kirar! Total Score: {score}")
                 
         
    else:
        if score<500:
            print(f"10 round bitti!Yarismayi kaybettin!Puan:{score}") 
        else :
            print(f"10 round bitti!Kazandin!Puan:{score}") 
       
         
               

    label.configure(text=score)
    label.pack()    
    #label.configure(text=round)
    #label.pack()   
    
def openNewWindow():
    newWindow = tk.Toplevel(window)
    newWindow.geometry("600x650")
    frame=tk.Frame(newWindow)
    frame.pack()
    
    newWindow.title("Oyun basladi")
 
    Label(newWindow,
          text ="START").pack()
    
     
    label1=tk.Label(newWindow,                  
               image=tas,
                )                
    label1.pack()

    label2=tk.Label(newWindow,                  
               image=kagit,
                )                
    label2.pack()

    label3=tk.Label(newWindow,                  
               image=makas,
                )                
    label3.pack()
    
    label1.bind('<Button-1>', on_click1)
    label2.bind('<Button-1>', on_click2)
    label3.bind('<Button-1>', on_click3)
  
def on_click1(event=None): 
    print("1.image clicked")
    choose("tas")
def on_click2(event=None): 
    print("2.image clicked")
    choose("kagit")
def on_click3(event=None): 
    print("3.image clicked")
    choose("makas")

def how_to_quit( ):
    openNewWindow()
      
window.title("Oyun Oyna")

photo=Image.open('C:\\Users\\conko\\OneDrive\\Desktop\\vscode_python\\rock_paper_scissors_game\\intro.png')
bg = ImageTk.PhotoImage(photo)
 
label=tk.Label(window,
               text="Tas Kagit Makas Oyna",
               font=('Arial',40,'bold'),
               fg='#00FF00',
               bg='black',
               bd=10,
               padx=20,  
               image=bg,
               compound='bottom') 
label.pack()

start_ = tk.Button(frame, 
                   text="start", 
                    width=25,
                   fg="blue",
                   command = how_to_quit
                   )
start_.pack(side="top", padx=15, pady=5)


"""quit button"""
quit_ = tk.Button(window,text='Quit',fg="red", width=25, command=window.destroy)
quit_.pack( padx=5, pady=5)


window.mainloop()