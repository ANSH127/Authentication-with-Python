from tkinter import *
import requests
import smtplib 
import random

t=0
lst1=[]
lst=[]
z=0


def last():
    global lst1,lst,z,l2
    if len(passentry.get())>=8:
        if passentry.get()==copassentry.get():
            if z==1:
                l2.destroy()
                
            Label(root3,text='Sucessful',font='papyrue 15 bold',bg='coral1',fg='yellow').place(x=95,y=170)
            lst+=a,
            lst1+=passentry.get(),
            #print(lst)
            #print(lst1)

    else:
        l2=Label(root3,text='Length Must be Atleast 8 Character',font='papyrue 12 bold',bg='coral1',fg='yellow')
        l2.place(x=50,y=170)
        z+=1





def chotp():
    global passentry,copassentry,root3
    
    
    x=otpentry.get()
    if int(x)==ot:
        #print('verified')
        root3=Tk()
        root3.geometry('300x300')
        root3.configure(bg='coral1')
        Label(root3,text='Password',font='papyrue 10 bold',bg='coral1',fg='black').place(x=40,y=80)
        Label(root3,text='Confirm Password',font='papyrue 10 bold',bg='coral1',fg='black').place(x=10,y=100)
       
        passentry=Entry(root3)
        passentry.place(x=140,y=80)
        copassentry=Entry(root3)
        copassentry.place(x=140,y=100)
        Button(root3,text='Submit',fg='black',bg='green',padx=25,pady=10,command=last).place(x=100,y=200)
        root3.mainloop()
        






def otp():
    global otpentry
    root2=Tk()
    root2.geometry('300x300')
    root2.configure(bg='coral1')
    Label(root2,text='ENTER YOUR OTP',font='papyrue 15 bold',bg='coral1',fg='black').place(x=50,y=80)
    otpentry=Entry(root2,font=2)
    otpentry.place(x=40,y=140)
    Button(root2,text='Submit',fg='black',bg='green',padx=25,pady=10,command=chotp).place(x=100,y=200)
    
    root2.mainloop()
    



def check():
    global l1,t,ot,a
    a=mailentry.get()
    #print(a)
    email_address = a
    response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params = {'email': email_address})

    status = response.json()['status']
    if status == "valid":
        #print("email is valid")
        if t==1:
            l1.destroy()
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("your email", " your password") 
        ot=random.randint(10000,99999)
        message = "Your Otp is "+str(ot)
        s.sendmail("your email", a, message) 
        s.quit() 
        otp()
        
    
    else:
        #print("email was invalid")
        l1=Label(root,text='Invalid',font='papyrue 15 bold',bg='cyan',fg='red')
        l1.place(x=120,y=270)
        t+=1









def up():
    global mailentry,root
    root=Tk()
    root.title('Signup Page')
    root.configure(bg='cyan')
    root.geometry('300x300')
    Label(root,text='Sign Up',font='papyrue 20 bold',bg='cyan',fg='black').place(x=90,y=50)
    Label(root,text='Enter Your Email Id',font='papyrue 12 bold',bg='cyan',fg='red').place(x=70,y=150)
    mailentry=Entry(root,font=1)
    mailentry.place(x=40,y=180)
    b=Button(root,text='Send Otp',fg='black',bg='orange',padx=25,pady=10,command=check)
    b.place(x=95,y=220)
    root.mainloop()     
    


def log1():
    if e1.get() in lst and e2.get() in lst1:
        #print('true')
        L3=Label(root1,text='Login Sucessful ',font='papyrue 12 bold',bg='green',fg='yellow')
        L3.place(x=150,y=250)
    else:
        if e1.get() not in lst:
            L1=Label(root1,text='User Not Exist',font='papyrue 10 bold',bg='green',fg='yellow')
            L1.place(x=150,y=250)
        else:
            L2=Label(root1,text='Incorrect Password',font='papyrue 10 bold',bg='green',fg='yellow')
            L2.place(x=150,y=250)
            
        #print('false')
        
















def log():
    global e1,e2,root1
    
    root1=Tk()
    root1.title('Login page')
    root1.configure(bg='green')
    root1.geometry('400x400')
    root1.maxsize(400,400)
    root1.minsize(400,400)
    L1=Label(root1,text='Login',font='papyrue 25 bold',bg='green',fg='yellow')
    L1.place(x=150,y=80)
    L2=Label(root1,text='Email Id',font='papyrue 15 bold',bg='green',fg='black')
    L2.place(x=50,y=170)
    e1=Entry(root1,font=1)
    e1.place(x=150,y=170)
    L3=Label(root1,text='Password',font='papyrue 15 bold',bg='green',fg='black')
    L3.place(x=40,y=210)
    e2=Entry(root1,font=1)
    e2.place(x=150,y=210)
    b=Button(root1,text='Login',fg='black',bg='green',padx=25,pady=10,command=log1)
    b.place(x=240,y=280)
    b1=Button(root1,text='Sign Up',fg='black',bg='green',padx=25,pady=10,command=up)
    b1.place(x=100,y=280)
    L4=Label(root1,text='Copright(Ansh Agarwal)',font='papyrue 15 bold',bg='green',fg='red')
    L4.place(x=100,y=350)
    root1.mainloop()
    
    

log()