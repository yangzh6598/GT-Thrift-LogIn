#Name:yang zhang
#sectin:A1
#GT email:yzhang3026@gatech.edu

from tkinter import *
import pymysql
class point:
    def __init__(self,mainwin):
        #the login GUI window
        self.mainwin=mainwin
        frame1=Frame(self.mainwin)
        frame1.pack()
        frame1.configure(background='blue')
        frame2=Frame(self.mainwin)
        frame2.pack()

        photo=PhotoImage(file='GT thrift shop.gif')
        
        l=Label(frame1,image=photo)
        l.photo=photo
        l.grid(row=0,column=1)
        
        self.name=Label(frame1,text='Username' )
        self.name.grid(row=1,column=0,sticky=E)
        self.name.configure(background='pink')
        
        self.passwd=Label(frame1,text='Password' )
        self.passwd.grid(row=2,column=0,sticky=E)
        self.passwd.configure(background='pink')

        self.v1=StringVar()
        self.v2=StringVar()

        self.e1=Entry(frame1,width=30,state='normal',textvariable=self.v1)
        self.e1.grid(row=1,column=1,pady=5,sticky=W)
        

        self.e2=Entry(frame1,width=30,state='normal',textvariable=self.v2)
        self.e2.grid(row=2,column=1,sticky=W)

        b1=Button(frame2,text='Cancel',width=6,command=self.existwindow).pack(side=LEFT)
        b2=Button(frame2,text='Login',width=8,command=self.LoginCheck).pack(side=LEFT)
        b3=Button(frame2,text='Register',width=8,command=self.showregister).pack(side=RIGHT)


        #The register GUI window
        self.register=Toplevel()
        self.register.title('GT Therift Shop Registration')

        frametot1=Frame(self.register)
        frametot1.pack()

        frametot1.configure(background='orange')
        
        frametot2=Frame(self.register)
        frametot2.pack()
        
        frame11=Frame(frametot1)
        frame11.pack(side=LEFT)

        frame22=Frame(frametot1)
        frame22.pack(side=LEFT)

        frame22.configure(background='orange')
        
        
        frame33=Frame(frametot2)
        frame33.pack(side=BOTTOM)
        Button(frame33,text='Cancel',command=self.goback).pack(side=LEFT)
        Button(frame33,text='Register',command=self.RegisterNew).pack(side=RIGHT)

       

        
        photo2=PhotoImage(file='GT thrift shop.gif')
        l2=Label(frame11,image=photo)
        l2.photo=photo
        l2.pack()

        ful=Label(frame22,text='Full Name')
        ful.grid(row=0,column=0,padx=5,pady=5,sticky=E)
        ful.configure(background='yellow')
        
        user=Label(frame22,text='User Name')
        user.grid(row=1,column=0,padx=5,pady=5,sticky=E)
        user.configure(background='yellow')

        passwd=Label(frame22,text='Password')
        passwd.grid(row=2,column=0,padx=5,pady=5,sticky=E)
        passwd.configure(background='yellow')

        confirmpass=Label(frame22,text='Confirm Password')
        confirmpass.grid(row=3,column=0,padx=5,pady=5,sticky=E)
        confirmpass.configure(background='yellow')




        
        self.v3=StringVar()
        self.v4=StringVar()
        self.v5=StringVar()
        self.v6=StringVar()

        self.e3=Entry(frame22,width=30,state='normal',textvariable=self.v3)
        self.e3.grid(row=0,column=1,sticky=W)

        

        self.e4=Entry(frame22,width=30,state='normal',textvariable=self.v4)
        self.e4.grid(row=1,column=1,sticky=W)

        
        self.e5=Entry(frame22,width=30,state='normal',textvariable=self.v5)
        self.e5.grid(row=2,column=1,sticky=W)
        
        self.e6=Entry(frame22,width=30,state='normal',textvariable=self.v6)
        self.e6.grid(row=3,column=1,sticky=W)
        
        #hide register GUI window
        self.register.iconify()



    #show register GUI window
    def showregister(self):
        self.register.deiconify()
        self.mainwin.withdraw()


    def RegisterNew(self):
        fullname=self.e3.get()
        try:
            spa=fullname.index(' ')
            fullname=fullname[0:spa]
            
        except:
            fullname=fullname

        username=self.e4.get()
        password=self.e5.get()
        confirmpass=self.e6.get()

        space1=password.find(' ')

        if username=='' or password=='':
            messagebox.showerror('Exceuse me!','username and password cannot be empty!')
            import sys
            sys.exit()
            self.RegisterNew()

        elif space1!=-1:
            messagebox.showerror('Exceuse me!','password can not include space character')
            import sys
            sys.exit()
            self.RegisterNew()


        elif password!=confirmpass:
            messagebox.showerror('Exceuse me!','password and confirm passwpord should be same!')
            import sys
            sys.exit()
            self.RegisterNew()
  
        else:
            
            
            db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
            c=db.cursor()
            sql='SELECT Username FROM user'
            c.execute(sql)
            usernamevalue=c.fetchall()
            t=0
            for f in range(len(usernamevalue)):
                if username==usernamevalue[f][0]:
                    t=t+1
                
            if t!=0:
               messagebox.showerror('Exceuse me!','username already exist!') 
                
            else:
                result=c.execute('INSERT INTO user(Username,FirstName,Password) VALUES(%s,%s,%s)',(username,fullname,password))
                messagebox.showinfo('Done','you have registered')
                self.register.withdraw()
                self.mainwin.deiconify()

                
            db.commit()
            c.close()
            db.close()


            
            


    def LoginCheck(self):
        self.mainwin.deiconify()
        username=self.e1.get()
        passwd=self.e2.get()


       
        db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
        c=db.cursor()

        sql='SELECT Username, Password FROM user'
        c.execute(sql)
        usepass=c.fetchall()
    
        
        p=0
        h=0
        q=0
        w=0
        for x in range(len(usepass)):
            if usepass[x][0]==username and usepass[x][1]==passwd:
                p=p+1

            if usepass[x][0]==username and usepass[x][1]!=passwd:
                h=h+1
                
            if usepass[x][0]!=username and usepass[x][1]!=passwd:
                q=q+1

            if usepass[x][0]!=username and usepass[x][1]==passwd:
                w=w+1



        space=passwd.find(' ')
        
        
        if username=='' or passwd=='':
            messagebox.showerror('Exceuse me!','Username and password can not be empty!')
        #password can not include space character
        elif space!=-1:
            messagebox.showerror('Exceuse me!','password can not include space')
            



        else:
            
            if p!=0:
                messagebox.showinfo('Done','you have logged in successfully')
                self.mainwin.withdraw()
                import sys
                sys.exit()

                

            if h!=0:
                messagebox.showerror('Exceuse me!','Your passwd is not right,try again!')
            if q==len(usepass):
                messagebox.showerror('Exceuse me!','username and password both are not right, try register first')
            if w!=0:
                messagebox.showerror('Exceuse me!','your username is not right,if you have registered before,try again.Otherwise, try register')
                
        
            
                    
            
        db.commit()
        c.close()
        db.close()








#login GUI window click 'cancel' to exist
    def existwindow(self):
        self.mainwin.destroy()
        #self.mainwin.withdraw()
        #import sys
        #sys.exit()



#register GUI window click 'cancel' to return to login GUI
    def goback(self):
        self.register.iconify()
        self.mainwin.deiconify()
            
        
        
           

root=Tk()
root.title('GT Thrift Shop')
p=point(root)
root.mainloop()
