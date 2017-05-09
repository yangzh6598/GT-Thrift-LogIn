#Name:yang zhang
#sectin:A1
#GT email:yzhang3026@gatech.edu
#I work on the homework assignment alone,using this semester"s course materials


########There are two GUI window images in c:/python34
########The images used in database are in c:/Python34/images, a folder is called images
from tkinter import *
import pymysql
import os

from collections import Counter

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
                #self.mainwin.withdraw()
                #import sys
                #sys.exit()
                self.register.withdraw()
                self.HomePage()
                self.mainwin.withdraw()

                

            elif h!=0:
                messagebox.showerror('Exceuse me!','Your passwd is not right,try again!')


            elif w!=0:
                messagebox.showerror('Exceuse me!','your username is not right,if you have registered before,try again.Otherwise, try register')

            if q==len(usepass):
                messagebox.showerror('Exceuse me!','username and password both are not right, try register first')
            
                
                        
            
        db.commit()
        c.close()
        db.close()








#login GUI window click 'cancel' to exist
    def existwindow(self):
        #test HomePage window
        self.mainwin.destroy()


        
        #self.mainwin.withdraw()
        import sys
        sys.exit()



#register GUI window click 'cancel' to return to login GUI
    def goback(self):
        self.register.iconify()
        self.mainwin.deiconify()


        



        


######################          homework 9 b       ############################################

    def HomePage(self):
        self.home=Toplevel()
        self.home.title('GT Therift Shop Home Page')

        frameh1=Frame(self.home)
        frameh1.pack()

        frameh2=Frame(self.home)
        frameh2.pack(side=RIGHT)
        
        frame11=Frame(frameh1)
        frame11.pack(side=LEFT)

        frame22=Frame(frameh1)
        frame22.pack(side=LEFT)

        frame22.configure(background='green')
        
        
        bbuy=Button(frame22,text='Buy',width=30,height=3,relief=FLAT,command=self.Buy)
        bbuy.grid(row=0,column=1,padx=4,pady=4)
        
        bsell=Button(frame22,text='Sell',width=30,height=3,relief=FLAT,command=self.sell)
        bsell.grid(row=1,column=1,padx=4,pady=4)

        
        bstats=Button(frame22,text='Stats',width=30,height=3,relief=FLAT,command=self.stats)
        bstats.grid(row=2,column=1,padx=4,pady=4)

       

        
        photo=PhotoImage(file='GT thrift shop3.gif')
        l2=Label(frame22,image=photo)
        l2.photo=photo
        l2.grid(row=0,column=0,rowspan=3)

        Button(frameh2,text='Cancel',width=30,command=self.cancel1).pack(side=RIGHT)

    def cancel1(self):
        self.home.destroy()
        import sys
        sys.exit()



    def sell(self):
        self.home.withdraw()
        
        self.sell=Toplevel()
        self.sell.title('GT Therift Shop Sell Something')

        frames1=Frame(self.sell)
        frames1.pack()

        frames1.configure(background='blue')

        frames11=Frame(frames1)
        frames11.pack(side=LEFT)

        frames12=Frame(frames1)
        frames12.pack(side=RIGHT)

        frames21=Frame(frames12)
        frames21.pack()

        
        

        frames3=Frame(self.sell)
        frames3.pack()
        


        frames21.configure(background='blue')
        
        
        
        
        frames3.pack(side=BOTTOM)
        Button(frames3,text='Cancel',command=self.cancel2).pack(side=LEFT)
        Button(frames3,text='Sell Item',command=self.SellInsert).pack(side=LEFT)

       

        
        photo=PhotoImage(file='GT thrift shop3.gif')
        l6=Label(frames11,image=photo)
        l6.photo=photo
        l6.pack()

        itemname=Label(frames21,text='Item Name')
        itemname.grid(row=0,column=0,padx=5,pady=5,sticky=E)
        itemname.configure(background='yellow')
        
        desc=Label(frames21,text='Description')
        desc.grid(row=1,column=0,padx=5,pady=5,sticky=E)
        desc.configure(background='yellow')

        price=Label(frames21,text='Price')
        price.grid(row=2,column=0,padx=5,pady=5,sticky=E)
        price.configure(background='yellow')

        imagename=Label(frames21,text='Image Name')
        imagename.grid(row=3,column=0,padx=5,pady=5,sticky=E)
        imagename.configure(background='yellow')

        condition=Label(frames21,text='Condition')
        condition.grid(row=4,column=0,padx=5,pady=5)
        condition.configure(background='yellow')


        self.s3=StringVar()
        self.s4=StringVar()
        self.s5=StringVar()
        self.s6=StringVar()

        self.ee3=Entry(frames21,width=30,state='normal',textvariable=self.s3)
        self.ee3.grid(row=0,column=1,columnspan=2,sticky=W)

        

        self.ee4=Entry(frames21,width=30,state='normal',textvariable=self.s4)
        self.ee4.grid(row=1,column=1,columnspan=2,sticky=W)

        
        self.ee5=Entry(frames21,width=30,state='normal',textvariable=self.s5)
        self.ee5.grid(row=2,column=1,columnspan=2,sticky=W)
        
        self.ee6=Entry(frames21,width=30,state='normal',textvariable=self.s6)
        self.ee6.grid(row=3,column=1,columnspan=2,sticky=W)


        self.s7=IntVar()
        self.used=Radiobutton(frames21,text='used',variable=self.s7,value=1)
        self.used.grid(row=4,column=1)

        self.used.configure(background='yellow')

        self.new=Radiobutton(frames21,text='new',variable=self.s7,value=2)
        self.new.grid(row=4,column=2)

        self.new.configure(background='yellow')

    def cancel2(self):
        self.home.deiconify()
        self.sell.withdraw()
       




    def SellInsert(self):
        direct=os.getcwd()
        imagesplace=os.chdir('c:/Python34/images')
        imagelist = os.listdir()

        getusername=self.e1.get()
        getpasswd=self.e2.get()

        itemname=self.ee3.get()
        description=self.ee4.get()
        price=self.ee5.get()
        imagename=self.ee6.get()
        
        decimalplace=price.find('.')
        if decimalplace==-1:
            bedeci=price
            afdeci=''
            
        else:
            bedeci=price[0:decimalplace]

            afdeci=price[decimalplace+1:]

        
        if self.s7.get()==1:
            usedvalue='1'
        if self.s7.get()==2:
            usedvalue='0'        
        #print(self.s7.get())
        
        purchasedvalue='0'

        if itemname=='' or price=='' or imagename=='':
            messagebox.showerror('Missing information','item name,description,price,and image name can not be empty')
            
        elif len(description)>50:
            messagebox.showerror('Exceuse me!','description is limited to 50 characters')
        elif len(bedeci)>4 or len(afdeci)>2:
            messagebox.showerror('Exceuse me!','price can only be up to 4 digits before the decimal and 2 after the decimal')

        elif imagename not in imagelist:
            messagebox.showerror('exceuse me!','the inputted image name is not in your image folder')
        else:
            db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
            c=db.cursor()
            
            result=c.execute('INSERT INTO GTThrift(username,itemname,description,price,used,purchased,image) VALUES(\
                             %s,%s,%s,%s,%s,%s,%s)',(getusername,itemname,description,price,usedvalue,purchasedvalue,imagename))
    
            db.commit()
            c.close()
            db.close()
            messagebox.showinfo('yes','sell successfully')
            self.sell.withdraw()
            self.home.deiconify()

        direct=os.getcwd()
        imagesplace=os.chdir('c:/Python34')
        imagelist = os.listdir()


    def Buy(self):
        self.home.iconify()
        self.buy=Toplevel()
        
        self.buy.title('GT Therift Shop Buy Something')

        frameb1=Frame(self.buy)
        frameb1.pack(side=TOP,fill=BOTH)
        frameb1.configure(background='blue')
        
        self.frameb2=Frame(self.buy)
        self.frameb2.pack(side=TOP,fill=BOTH)
        self.frameb2.configure(background='blue')
        
        Label(self.frameb2,text='Image').grid(row=0,column=1)
        Label(self.frameb2,text='Item Name').grid(row=0,column=2)
        Label(self.frameb2,text='Description').grid(row=0,column=3)
        Label(self.frameb2,text='price').grid(row=0,column=4)
        Label(self.frameb2,text='used').grid(row=0,column=5)
        Label(self.frameb2,text='Listing Username').grid(row=0,column=6)
        
        frameb3=Frame(self.buy)
        frameb3.pack(side=RIGHT)

        Label(frameb1,text='Sort By').pack(side=LEFT)
        
        self.var = StringVar()
        
        self.var.set("Price: High to Low") 
        option = OptionMenu(frameb1,self.var,"Price: High to Low",\
                            "Price: Low to High", "New", "Old","A-Z","Z-A",command=self.ppget)
        
        option.pack()


        #######show things in buy-window############
        db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
        c=db.cursor()
        c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY Price DESC')
        self.result1=c.fetchall()

        for i in range(len(self.result1[0:5])):
        
            #image
            #Label(frameb2,text=result[i][-2]).grid(row=i+1,column=1)

            photo=PhotoImage(file=self.result1[i][-2])
            
        
            l=Label(self.frameb2,image=photo,height=120)
            l.photo=photo
            l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)
            
            

            if self.result1[i][5]==0:
                condition='New'
            else:
                condition='Used'
                
            #ItemName
            Label(self.frameb2,text=self.result1[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
        
            #Description
            Label(self.frameb2,text=self.result1[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
            #Price
            Label(self.frameb2,text=self.result1[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
            #used
            Label(self.frameb2,text='condition: %s'%(condition),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
            #listing username
            Label(self.frameb2,text=self.result1[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)

        db.commit()
        c.close()
        db.close()
     
        
            
       



        Button(frameb3,text='Cancel',command=self.cancel3).grid(row=0,column=8,sticky=E)
        Button(frameb3,text='Clear',command=self.desele).grid(row=0,column=12,sticky=E)
        Button(frameb3,text='Place Order',command=self.BuyUpdate).grid(row=0,column=16,sticky=E)



        #######set radiobuttons
        self.rr1=IntVar()
        for w in range(len(self.result1[0:5])):
            
       
        
            Radiobutton(self.frameb2,variable=self.rr1,value=self.result1[w][0]).grid(row=w+1,column=0)
        

        
        
    def cancel3(self):
        self.buy.destroy()
        self.home.deiconify()

    def desele(self):
        self.rr1.set(None)
        

        
        
    def ppget(self,para):

        #print(self.var.get())
        db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
        c=db.cursor()

        if self.var.get()=='Price: Low to High':
                

            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY Price ASC')
            result=c.fetchall()
            

            for i in range(len(result[0:5])):
                
                #image
                #Label(frameb2,text=result[i][-2]).grid(row=i+1,column=1)

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)

                if result[i][5]==0:
                    condition1='New'
                else:
                    condition1='Used'
            

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition1),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)




        if self.var.get()=='Price: High to Low':
            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY Price DESC')
            result=c.fetchall()
            for i in range(len(result[0:5])):
                
                #image
                #Label(frameb2,text=result[i][-2]).grid(row=i+1,column=1)

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)

                
                if result[i][5]==0:
                    condition2='New'
                else:
                    condition2='Used'

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition2),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)



        if self.var.get()=='New':
            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY ID ASC')
            result=c.fetchall()
            for i in range(len(result[0:5])):

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)
                if result[i][5]==0:
                    condition3='New'
                else:
                    condition3='Used'
            

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition3),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)



        if self.var.get()=='Old':
            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY ID DESC')
            result=c.fetchall()
            for i in range(len(result[0:5])):

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)
                if result[i][5]==0:
                    condition4='New'
                else:
                    condition4='Used'
            
            

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition4),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)




        if self.var.get()=='A-Z':
            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY ItemName ASC')
            result=c.fetchall()
            for i in range(len(result[0:5])):

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)

                if result[i][5]==0:
                    condition5='New'
                else:
                    condition5='Used'
            

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition5),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)



        if self.var.get()=='Z-A':
            c.execute('SELECT * FROM GTThrift WHERE Purchased="0" ORDER BY ItemName DESC')
            result=c.fetchall()
            for i in range(len(result[0:5])):

                photo=PhotoImage(file=result[i][-2])
                
            
                l=Label(self.frameb2,image=photo,height=120)
                l.photo=photo
                l.grid(row=i+1,column=1,padx=5,pady=5,sticky=E+W)
                
                if result[i][5]==0:
                    condition6='New'
                else:
                    condition6='Used'
            

                
                #ItemName
                Label(self.frameb2,text=result[i][2],width=20,bg='sky blue').grid(row=i+1,column=2,padx=5,pady=5,sticky=N+S)
            
                #Description
                Label(self.frameb2,text=result[i][3],width=20,bg='sky blue').grid(row=i+1,column=3,padx=5,pady=5,sticky=N+S)
                #Price
                Label(self.frameb2,text=result[i][4],width=20,bg='sky blue').grid(row=i+1,column=4,padx=5,pady=5,sticky=N+S)
                #used
                Label(self.frameb2,text='condition: %s'%(condition6),width=20,bg='sky blue').grid(row=i+1,column=5,padx=5,pady=5,sticky=N+S)
                #listing username
                Label(self.frameb2,text=result[i][1],width=20,bg='sky blue').grid(row=i+1,column=6,padx=5,pady=5,sticky=N+S)

                            
        
        db.commit()
        c.close()
        db.close()




        #######set radiobuttons
        self.rr1=IntVar()
        for w in range(len(result[0:5])):
            
       
        
            Radiobutton(self.frameb2,variable=self.rr1,value=result[w][0]).grid(row=w+1,column=0)
        



    def BuyUpdate(self):

        buyuse=self.e1.get()
               
        radiovalue=self.rr1.get()

        if radiovalue==0:
            messagebox.showerror('Woops!','Plese select an item to purchase!')
        else:
             db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
             c=db.cursor()
             c.execute('UPDATE GTThrift SET Purchased="1" WHERE ID=%s',(radiovalue))
             c.execute('UPDATE GTThrift SET BuyerUsername=%s WHERE ID=%s',(buyuse,radiovalue))

             c.execute('SELECT ItemName, price, Username FROM GTThrift WHERE ID=%s',(radiovalue))

             ipu=c.fetchall()
 
             db.commit()
             c.close()
             db.close()

             
             messagebox.showinfo('successful Purchased','Congratulations you have purchased %s for %s from %s!'%(ipu[0][0],ipu[0][1],ipu[0][2]))
             self.buy.withdraw()
             self.home.deiconify()
    


 
            
    def stats(self):
        self.home.withdraw()
        self.stats=Toplevel()     
        self.stats.title('GT Therift Shop Stats')

        self.bigframe=Frame(self.stats)
        self.bigframe.pack()

        framest1=Frame(self.bigframe)
        framest1.pack(side=LEFT)

        framest2=Frame(self.bigframe)
        framest2.pack(side=RIGHT)

        framest3=Frame(self.stats)
        framest3.pack(side=RIGHT)

        Button(framest3,text='Cancel',command=self.cancel8).pack(side=RIGHT)
        

        framest2.configure(background='purple')
        
        photo=PhotoImage(file='GT thrift shop3.gif')        
        l5=Label(framest1,image=photo)
        l5.photo=photo
        l5.grid(row=0,column=0,rowspan=3)

        Label(framest2,text='Most Active User').grid(row=0,column=0,padx=5,pady=5,sticky=E)
        Label(framest2,text='Most Active Purchaser').grid(row=1,column=0,padx=5,pady=5,sticky=E)
        Label(framest2,text='Most Active Seller').grid(row=2,column=0,padx=5,pady=5,sticky=E)
        Label(framest2,text='Most Expensive Item on the Market').grid(row=3,column=0,padx=5,pady=5,sticky=E)
        Label(framest2,text='Most Expensive Item sold').grid(row=4,column=0,padx=5,pady=5,sticky=E)
        

    
        
        
        db=pymysql.connect(host='us-cdbr-azure-east-c.cloudapp.net',user='bcbc107704f5ca',passwd='879e7d38',db='acsm_fa25daff4117b25')
        c=db.cursor()
        c.execute('SELECT Username FROM GTThrift ')
        
        username=c.fetchall()

        c.execute('SELECT BuyerUsername FROM GTThrift ')
        buyername=c.fetchall()

            

        ###get most active user########
        
        allname=username+buyername
        alist=[]
        for i in range(len(allname)):
            if allname[i][0]!=None:
                alist.append(allname[i][0])
            

        dictname=Counter(alist)   

        mostactiveuser=max(dictname, key=dictname.get)
       
       

        

        ###get most active purchaser
        alist1=[]
        for j in range(len(buyername)):
            if buyername[j][0]!=None:
                alist1.append(buyername[j][0])

        if alist1==[]:
            mostactivepurchaser='No items have been purchased yet'
        else:
        
            dicpurchase=Counter(alist1)
         
            mostactivepurchaser=max(dicpurchase, key=dicpurchase.get)
            
            c.execute('SELECT SUM(Price) FROM GTThrift WHERE BuyerUsername=%s',(mostactivepurchaser))
            
            spendmoney=c.fetchall()

        ###get most active seller#####

        alist2=[]
        for k in range(len(username)):
            if username[k][0]!=None:
                alist2.append(username[k][0])
        dicuser=Counter(alist2)
        mostactiveseller=max(dicuser,key=dicuser.get)
        c.execute('SELECT AVG(Price) FROM GTThrift WHERE Username=%s',(mostactiveseller))
        avgprice=c.fetchall()

        ######most expensive item
        c.execute('SELECT MAX(price) FROM GTThrift WHERE Purchased="0"')
        hprice=c.fetchall()
                
        c.execute('SELECT ItemName FROM GTThrift WHERE Price=(SELECT MAX(Price) FROM GTThrift WHERE Purchased=0)')
        hitem=c.fetchall()
        
      
        #####most expensive item sold
        c.execute('SELECT MAX(price) FROM GTThrift WHERE Purchased="1"')
        hprice2=c.fetchall()
        
        c.execute('SELECT ItemName FROM GTThrift WHERE Price=(SELECT MAX(Price) FROM GTThrift WHERE Purchased="1")')
        hitem2=c.fetchall()


        #####current user buy and sale
        currentuser=self.e1.get()

        Label(framest2,text="%s's Item(s) for sale"%(currentuser)).grid(row=5,column=0,padx=5,pady=5,sticky=E)
        Label(framest2,text="%s's Item(s) for Purchased"%(currentuser)).grid(row=6,column=0,padx=5,pady=5,sticky=E) 

        c.execute('SELECT ItemName FROM GTThrift WHERE UserName=%s',(currentuser))
        currsale=c.fetchall()
        currsale2=''
        if len(currsale)==0:
            currsale2='None'
        else:
            for n in range(len(currsale)):
                currsale2=currsale2+', '+currsale[n][0]
            currsale2=currsale2[1:]
                
    

        c.execute('SELECT ItemName FROM GTThrift WHERE BuyerUsername=%s',(currentuser))
        currbuy=c.fetchall()
        currbuy2=''
        
        if len(currbuy)==0:
            currbuy2='None'
        else:
            for m in range(len(currbuy)):
                currbuy2=currbuy2+', '+currbuy[m][0]
            currbuy2=currbuy2[1:]


               
        
        db.commit()
        c.close()
        db.close()



        ############set values####
        Label(framest2,text=mostactiveuser).grid(row=0,column=1,sticky=E+W)
        if alist1==[]:
            Label(framest2,text='No items have been purchased yet').grid(row=1,column=1,sticky=E+W)
            
        else:
            Label(framest2,text='%s spent a total of a $%0.2f'%(mostactivepurchaser,spendmoney[0][0])).grid(row=1,column=1,sticky=E+W)
        Label(framest2,text='%s average price per item is $%0.2f'%(mostactiveseller,avgprice[0][0])).grid(row=2,column=1,sticky=E+W)
        Label(framest2,text='%s cost $%s'%(hitem[0][0],hprice[0][0])).grid(row=3,column=1,sticky=E+W)

        if hprice2[0][0]==None:
            Label(framest2,text='No items have been purchased yet').grid(row=4,column=1,sticky=E+W)
        else:
            Label(framest2,text='%s cost $%s'%(hitem2[0][0],hprice2[0][0])).grid(row=4,column=1,sticky=E+W)
            
        
        Label(framest2,text='%s'%(currsale2)).grid(row=5,column=1,sticky=E+W)
        Label(framest2,text='%s'%(currbuy2)).grid(row=6,column=1,sticky=E+W)


    def cancel8(self):
        self.stats.withdraw()
        self.home.deiconify()
        

               

root=Tk()
root.title('GT Thrift Shop')
p=point(root)
root.mainloop()
