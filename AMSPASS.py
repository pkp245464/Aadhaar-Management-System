from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import sqlite3


root=Tk()
root.geometry('800x790')
root.title("AMS")
root.iconbitmap('asd.ico')

def create():
    conn=sqlite3.connect('PKPDatabase.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement,Firstname TEXT,Lastname TEXT,Fathername TEXT,Mothername TEXT,Dateofbirth TEXT,Villagename TEXT,Statename TEXT,Countryname TEXT,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()
create()


#Title of Project
Title=Label(text="      ADHAR MANAGEMENT SYSTEM       ",bd=16,fg="#000000",font=('arial',35,'bold'),bg="OliveDrab1",relief='raise',width=32,height=1)
Title.pack()
SmallTitle=Label(text="Basic Details Form",bd=3,bg="Cyan",width=32,height=1,font=('arial',10,'bold'),relief=SUNKEN)
SmallTitle.place(x=270,y=100)

#Basic Informations

First_Name=Label(root, text="First Name:-", width=20, font=("bold"),fg="Cornflowerblue")
First_Name.place(x=50,y=200)
FNR=StringVar()
First_Name_Box=Entry(root,width=40,bg="honeydew2",textvariable=FNR)
First_Name_Box.place(x=300, y=200)

Last_Name=Label(root, text="Last Name:-  ", width=20, font=("bold"),fg="Cornflowerblue")
Last_Name.place(x=50,y=250)
LNR=StringVar()
Last_Name_Box=Entry(root,width=40,bg="honeydew2",textvariable=LNR)
Last_Name_Box.place(x=300, y=250)

Father_Name=Label(root, text="Father Name:-", width=20, font=("bold"),fg="Cornflowerblue")
Father_Name.place(x=50,y=300)
FFNR=StringVar()
Father_Name_Box=Entry(root,width=40,bg="honeydew2",textvariable=FFNR)
Father_Name_Box.place(x=300, y=300)

Mother_Name=Label(root, text="Mother Name:-", width=20, font=("bold"),fg="Cornflowerblue")
Mother_Name.place(x=50,y=350)
MMNR=StringVar()
Mother_Name_Box=Entry(root,width=40,bg="honeydew2",textvariable=MMNR)
Mother_Name_Box.place(x=300, y=350)

DOB=Label(root, text="Date Of Birth:-", width=20, font=("bold"),fg="Cornflowerblue")
DOB.place(x=50,y=400)
DOBR=StringVar()
DOB_Box=Entry(root,width=40,bg="honeydew2",textvariable=DOBR)
DOB_Box.place(x=300, y=400)

Religion=Label(root, text="Religion:-", width=20, font=("bold"),fg="Cornflowerblue")
Religion.place(x=50,y=450)
var=IntVar()
Radiobutton(root,text="Hindu",variable=var,value=1,bg="green yellow").place(x=300,y=450)
Radiobutton(root,text="Muslim",variable=var,value=2,bg="green yellow").place(x=370,y=450)
Radiobutton(root,text="Sikhs",variable=var,value=3,bg="green yellow").place(x=440,y=450)
Radiobutton(root,text="Christian",variable=var,value=4,bg="green yellow").place(x=500,y=450)

Gender=Label(root, text="Gender:-", width=20, font=("bold"),fg="Cornflowerblue")
Gender.place(x=50,y=500)
GenderList=['Male','Female','Other']
c=StringVar()
d=OptionMenu(root,c,*GenderList)
c.set("Select Gender")
d.place(x=300,y=500)

Language=Label(root, text="Language:-", width=20, font=("bold"),fg="Cornflowerblue")
Language.place(x=50,y=550)
v1=IntVar()
Checkbutton(root, text="Hindi", variable=v1,bg="pale green1").place(x=300,y=550)
v2=IntVar()
Checkbutton(root, text="English", variable=v2,bg="pale green1").place(x=370,y=550)
v3=IntVar()
Checkbutton(root, text="Sanskrit", variable=v3,bg="pale green1").place(x=440,y=550)
v4=IntVar()
Checkbutton(root, text="Urdu", variable=v4,bg="pale green1").place(x=520,y=550)

Village=Label(root, text="Village Name:-", width=20, font=("bold"),fg="Cornflowerblue")
Village.place(x=50,y=600)
VNBR=StringVar()
Village_Box=Entry(root,width=40,bg="wheat1",textvariable=VNBR)
Village_Box.place(x=300, y=600)

State=Label(root, text="State Name:-", width=20, font=("bold"),fg="Cornflowerblue")
State.place(x=50,y=650)
SNBR=StringVar()
State_Box=Entry(root,width=40,bg="wheat1",textvariable=SNBR)
State_Box.place(x=300, y=650)

Country=Label(root, text="Country Name:-", width=20, font=("bold"),fg="Cornflowerblue")
Country.place(x=50,y=700)
CNBR=StringVar()
Country_Box=Entry(root,width=40,bg="wheat1",textvariable=CNBR)
Country_Box.place(x=300, y=700)

#First Windows-------------------------------------------------------------------------------------------
def ImageWindows():
    top1=Toplevel()
    top1.geometry('500x500')
    top1.title("Image Windows")
    PassportSI = Label(top1, text="Passport Size Image:-", width=20, font=("bold"), fg="Cornflowerblue")
    PassportSI.place(x=5, y=5)
    def OpenImage():
        global my_image
        top1.filename = filedialog.askopenfilename(initialdir="D:\Tkinter\Python\TkinterPFiles", title="Select A Image",
        filetypes=(("PNG Image", "*.png"), ("All Image", "*.*")))

        my_image = ImageTk.PhotoImage(Image.open(top1.filename))
        my_image_label = Label(top1,image=my_image).place(x=100,y=70)
    my_btn = Button(top1,text="Select Image", command=OpenImage).place(x=250, y=7)

    btnC=Button(top1,text="Close Windows",bg="firebrick1",fg="Black",command=top1.destroy).place(x=200,y=470)
btn1=Button(root,text="Image Section",bg="dark orange",fg="Black",command=ImageWindows).place(x=10,y=750)


#Second Windows-------------------------------------------------------------------------------------------
def DevelopersWindows():
    top2=Toplevel()
    top2.title("Developers Windows")
    global my_img
    my_img = ImageTk.PhotoImage(Image.open("madeby.png"))
    my_label = Label(top2,image=my_img).pack()

    btnC=Button(top2,text="Close Windows",bg="firebrick1",fg="Black",command=top2.destroy).place(x=520,y=620)
btn2=Button(root,text="Developers Details",bg="dark orange",fg="Black",command=DevelopersWindows).place(x=690,y=750)


#Third Windows-------------------------------------------------------------------------------------------
def BMICheck():
    top3=Toplevel()
    top3.geometry("1350x650+0+0")
    top3.resizable(0, 0)
    top3.title("BMI")

    def BMI_Cal():
        BHeight = float(var2.get())
        BWeight = float(var1.get())
        BMI = str('%.2f' % (BWeight / (BHeight * BHeight)))
        lblBMIResult.config(text=BMI)

    var1 = DoubleVar()
    var2 = DoubleVar()

    Tops = Frame(top3, width=1350, height=50, bd=8, relief="raise")
    Tops.pack(side=TOP)
    f1 = Frame(top3, width=600, height=600, bd=8, relief="raise")
    f1.pack(side=LEFT)
    f2 = Frame(top3, width=300, height=700, bd=8, relief="raise")
    f2.pack(side=RIGHT)

    f1a = Frame(f1, width=600, height=200, bd=20, relief="raise")
    f1a.pack(side=TOP)
    f1b = Frame(f1, width=600, height=600, bd=20, relief="raise")
    f1b.pack(side=TOP)

    lblTitle = Label(Tops, text="          Body Mass Index        ", padx=16, pady=16, bd=16,
                     fg="#000000", font=('arial', 54, 'bold'),
                     bg="spring green", relief='raise', width=32, height=1)
    lblTitle.pack()

    lblWeight = Label(f1a, text="Select Weight in Kilograms ", font=('arial', 20, 'bold'), bd=20).grid(row=0, column=0)
    Bodyweight = Scale(f1a, variable=var1, from_=1, to=500, length=880, tickinterval=30, orient=HORIZONTAL)
    Bodyweight.grid(row=1, column=0)

    lblheight = Label(f1b, text="Enter Height in Meters Square", font=('arial', 20, 'bold'), bd=20).grid(row=0,
                                                                                                         column=0)
    txtheight = Entry(f1b, textvariable=var2, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
    txtheight.grid(row=1, column=0)

    lblBMIResult = Label(f1b, padx=16, pady=16, bd=16,
                         fg="#000000", font=('arial', 30, 'bold'),
                         bg="hot pink", relief='sunk', width=34, height=1)
    lblBMIResult.grid(row=2, column=0)

    lblBMITable = Label(f2, font=('arial', 20, 'bold'), text="BMI Table").grid(row=0, column=0)
    txtlblBMITable = Text(f2, height=12, width=38, bd=16, font=('arial', 12, 'bold'))
    txtlblBMITable.grid(row=1, column=0)

    txtlblBMITable.insert(END, 'Under weight \t\t' + "<19\n\n")
    txtlblBMITable.insert(END, 'Normal weight \t\t' + "19-24,9\n\n")
    txtlblBMITable.insert(END, 'Overweight \t\t' + "25-29,9\n\n")
    txtlblBMITable.insert(END, 'Obesity level I \t\t' + "30-34,9\n\n")
    txtlblBMITable.insert(END, 'Obesity level II\t\t' + "35-39,9\n\n")
    txtlblBMITable.insert(END, 'Obesity level III \t\t' + ">=40\n\n")

    btnBMI = Button(f2, text="Click to \nCheck Your \nBMI", padx=8, pady=8, bd=12, width=21,
                    font=('arial', 20, 'bold'), height=3, command=BMI_Cal)
    btnBMI.grid(row=2, column=0)

    btnC=Button(top3,text="Close Windows",bg="firebrick1",fg="Black",command=top3.destroy).place(x=520,y=620)
btn3=Button(root,text="Check BMI",bg="dark orange",fg="Black",command=BMICheck).place(x=100,y=750)


#Fourth Windows-------------------------------------------------------------------------------------------
def HelpWindows():
    top4=Toplevel()
    top4.geometry('500x500')
    top4.title("Help Desk Windows")

    SYQ= Label(top4, text="---Submit Your Query---", width=20,font=('arial',25,"bold"),bg="black",fg="White")
    SYQ.place(x=45,y=10)

    First_Name= Label(top4, text="First Name:-",font=('arial',15,'bold'),fg="lawn green")
    First_Name.place(x=10,y=100)
    First_Name_Box =Entry(top4,width=40,bg="aquamarine")
    First_Name_Box.place(x=200,y=100)

    Last_Name= Label(top4, text="Last Name:-", font=('arial', 15, 'bold'), fg="lawn green")
    Last_Name.place(x=10, y=130)
    Last_Name_Box = Entry(top4,width=40,bg="aquamarine")
    Last_Name_Box.place(x=200,y=130)

    Mobile_Number = Label(top4, text="Mobile Number:-", font=('arial', 15, 'bold'), fg="lawn green")
    Mobile_Number.place(x=10, y=160)
    Mobile_Number_Box = Entry(top4, width=40,bg="aquamarine")
    Mobile_Number_Box.place(x=200, y=160)

    Email_Id = Label(top4, text="Email Id:-", font=('arial', 15, 'bold'), fg="lawn green")
    Email_Id.place(x=10, y=190)
    Email_Id_Box = Entry(top4, width=40,bg="aquamarine")
    Email_Id_Box.place(x=200, y=190)

    AgeH = Label(top4, text="Age:-", font=('arial', 15, 'bold'), fg="lawn green")
    AgeH.place(x=10, y=220)
    v = IntVar()
    v.set(9)
    Age_Box=Spinbox(top4,from_=9,to=150, width=10, textvariable=v,bg="dark orange",bd=1)
    Age_Box.place(x=200, y=220)

    Query1 = Label(top4, text="Query:-", font=('arial', 15, 'bold'), fg="lawn green")
    Query1.place(x=10, y=250)
    Query_Box= Text(top4, height=9, width=30,bd=3,bg="misty rose")
    Query_Box.place(x=200, y=250)

    def SubmitPopPup():
        response = messagebox.askokcancel("Final Submissions!", "Confirm")
        Label(top4,text=response).pack()
    SubmitButton=Button(top4, text="Submit", font=('arial', 17, 'bold'), fg="maroon3",bg="snow3",command=SubmitPopPup)
    SubmitButton.place(x=200, y=420)

    btnC=Button(top4,text="Close Windows",bg="firebrick1",fg="Black",command=top4.destroy).place(x=400,y=470)
btn4=Button(root,text="Help Desk",bg="dark orange",fg="Black",command=HelpWindows).place(x=623,y=750)


#Fifth Windows-------------------------------------------------------------------------------------------
def AboutAC():
    top5=Toplevel()
    top5.geometry('350x500')
    top5.title("Aadhaar Card")

    ADCT= Label(top5, text="About Aadhaar Card", width=20, font=('arial', 18, "bold"), bg="Salmon", fg="White")
    ADCT.place(x=20, y=10)

    global my_imga
    my_imga = ImageTk.PhotoImage(Image.open("Aadhaarcard.png"))
    my_label = Label(top5,image=my_imga).place(x=20,y=50)

    ACDIWF=Text(top5,height=10,width=40, bg="light yellow")
    ACDIWF.insert(INSERT,"Aadhaar is a 12 digit individual identification number issued by the Unique Identification Authority of of India on behalf of the Government of India.The number serves as a proof of identity and address, anywhere in India.")
    ACDIWF.place(x=10,y=270)

    btnC=Button(top5,text="Close Windows",bg="firebrick1",fg="Black",command=top5.destroy).place(x=130,y=470)
btn5=Button(root,text="About Aadhaar Card",bg="dark orange",fg="Black",command=AboutAC).place(x=500,y=750)


#Sixth Windows-------------------------------------------------------------------------------------------
def PaymentSystem():
    top6=Toplevel()
    top6.geometry('500x400')
    top6.title("Payment System")

    PaymentH= Label(top6, text="Payment System", width=20, font=('arial', 23, "bold"), bg="green yellow", fg="White")
    PaymentH.place(x=55,y=10)

    Choose_Card = Label(top6, text="Choose Card:-", font=('arial', 15, 'bold'), fg="Blue")
    Choose_Card.place(x=10, y=100)
    var1=IntVar()
    Radiobutton(top6, text="Debit Card", variable=var1, value=1, bg="DarkGoldenrod1").place(x=180, y=100)
    Radiobutton(top6, text="Credit Card", variable=var1, value=2, bg="DarkGoldenrod1").place(x=270, y=100)
    Radiobutton(top6, text="Master Card", variable=var1, value=3, bg="DarkGoldenrod1").place(x=365, y=100)

    Card_Number = Label(top6, text="Card Number:-", font=('arial', 15, 'bold'), fg="Blue")
    Card_Number.place(x=10, y=135)
    RBFCN=StringVar()
    Card_Number_Box = Entry(top6, width=40, bg="Azure",textvariable=RBFCN)
    Card_Number_Box.place(x=200, y=140)

    Account_Number = Label(top6, text="Account Number:-", font=('arial', 15, 'bold'), fg="Blue")
    Account_Number.place(x=10, y=170)
    RBFAN=StringVar()
    Account_Number_Box = Entry(top6, width=40, bg="Azure",textvariable=RBFAN)
    Account_Number_Box.place(x=200, y=175)

    Account_Holder = Label(top6, text="Account Holder:-", font=('arial', 15, 'bold'), fg="Blue")
    Account_Holder.place(x=10, y=205)
    RBFAHN=StringVar()
    Account_Holder_Box = Entry(top6, width=40, bg="Azure",textvariable=RBFAHN)
    Account_Holder_Box.place(x=200, y=210)

    ExpireD= Label(top6, text="Expiration Date:-", font=('arial', 15, 'bold'), fg="Blue")
    ExpireD.place(x=10, y=240)
    RBFEN=StringVar()
    ExpireD_Box = Entry(top6, width=40, bg="Azure",textvariable=RBFEN)
    ExpireD_Box.place(x=200, y=245)

    CVC = Label(top6, text="CVC Code:-", font=('arial', 15, 'bold'), fg="Blue")
    CVC.place(x=10, y=275)
    RBFCVC=StringVar()
    CVC_Box = Entry(top6, width=40, bg="Azure",textvariable=RBFCVC)
    CVC_Box.place(x=200, y=280)
    def resetBF():
        RBFCN.set("")
        RBFAN.set("")
        RBFAHN.set("")
        RBFEN.set("")
        RBFCVC.set("")
        return

    SubmitPB = Button(top6, text="Submit", font=('arial', 15, 'bold'), fg="Red",bg="Bisque",command=resetBF)
    SubmitPB.place(x=200, y=330)

    btnC=Button(top6,text="Close Windows",bg="firebrick1",fg="Black",command=top6.destroy).place(x=400,y=370)
btn6=Button(root,text="Payment Method",bg="dark orange",fg="Black",command=PaymentSystem).place(x=172,y=750)

def savedata():
    conn=sqlite3.connect('PKPDatabase.db')
    c=conn.cursor()
    c.execute('INSERT INTO users(Firstname,Lastname,Fathername,Mothername,Dateofbirth,Villagename,Statename,Countryname) VALUES (?,?,?,?,?,?,?,?)',(FNR.get(),LNR.get(),FFNR.get(),MMNR.get(),DOBR.get(),VNBR.get(),SNBR.get(),CNBR.get()))
    conn.commit()
    print("Data Save Successfully")

SubmitButtonF1=Button(root,text="Submit",bg="yellow",fg="Black",bd=3,relief=RAISED,font=('arial',15,'bold'),command=savedata)
SubmitButtonF1.place(x=345,y=730)

root.mainloop()


