##rr##
## Nouvelle ligne
## Vérifier l'unicité du numéro de facture
from tkinter import *
import tkinter.simpledialog
import sys
import csv
import os
import datetime
#############
## Counter ##
#############
i = 1
def clicked():
    global i
    i = i + 1
def unclicked():
    global i
    i = i - 1
def delextrafile():
    os.system('rm *.synctex.gz')
    os.system('rm *.aux')
    os.system('rm *.log')
##################
## Set Up Frame ##
##################
root = Tk()
root.config(background = "light grey")
###############
## Variables ##
###############
BillNumber  = StringVar()
FirstName   = StringVar()
Surname     = StringVar()
Address1    = StringVar()
City1       = StringVar()
Enterprise  = StringVar()
Address2    = StringVar()
City2       = StringVar()
Object      = StringVar()
Day         = StringVar()
Month       = StringVar()
Year        = StringVar()
Row1        = StringVar()
Row11       = StringVar()
Row2        = StringVar()
Row12       = StringVar()
Row3        = StringVar()
Row13       = StringVar()
Row4        = StringVar()
Row14       = StringVar()
Row5        = StringVar()
Row15       = StringVar()
Row6        = StringVar()
Row16       = StringVar()
Row7        = StringVar()
Row17       = StringVar()
#############################
## Function ##
##############
def getmember():
    aBillNumber     = BillNumber.get()
    aFirstName      = FirstName.get()
    aSurname        = Surname.get()
    aAddress1       = Address1.get()
    aCity1          = City1.get()
    aEnterprise     = Enterprise.get()
    aAddress2       = Address2.get()
    aCity2          = City2.get()
    aObject         = Object.get()
    aDay            = Day.get()
    aMonth          = Month.get()
    aYear           = Year.get()
    aRow1           = Row1.get()
    aRow11          = Row11.get()
    aRow2           = Row2.get()
    aRow12          = Row12.get()
    aRow3           = Row3.get()
    aRow13          = Row13.get()
    aRow4           = Row4.get()
    aRow14          = Row14.get()
    aRow5           = Row5.get()
    aRow15          = Row15.get()
    aRow6           = Row6.get()
    aRow16          = Row16.get()
    aRow7           = Row7.get()
    aRow17          = Row17.get()
    aDate           = aDay+" "+aMonth+" "+aYear
    return [aBillNumber,aFirstName,aSurname,aAddress1,aCity1,aEnterprise,\
            aAddress2,aCity2,aObject,aDate,aRow1,aRow11,aRow2,aRow12,aRow3,\
            aRow13,aRow4,aRow14,aRow5,aRow15,aRow6,aRow16,aRow7,aRow17]

def temporary_line1():
    global temporary_line
    temporary_line = getmember()
#############
def previous_line():
    with open('database.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rowss = list(reader)
        unclicked()
        print(str(i))
        BillNumber.set(rowss[i-1][0])
        FirstName.set(rowss[i-1][1])
        Surname.set(rowss[i-1][2])
        Address1.set(rowss[i-1][3])
        City1.set(rowss[i-1][4])
        Enterprise.set(rowss[i-1][5])
        Address2.set(rowss[i-1][6])
        City2.set(rowss[i-1][7])
        Object.set(rowss[i-1][8])
        Day.set(rowss[i-1][9].split(' ')[0])
        Month.set(rowss[i-1][9].split(' ')[1])
        Year.set(rowss[i-1][9].split(' ')[2])
        Row1.set(rowss[i-1][10])
        Row11.set(rowss[i-1][11])
        Row2.set(rowss[i-1][12])
        Row12.set(rowss[i-1][13])
        Row3.set(rowss[i-1][14])
        Row13.set(rowss[i-1][15])
        Row4.set(rowss[i-1][16])
        Row14.set(rowss[i-1][17])
        Row5.set(rowss[i-1][18])
        Row15.set(rowss[i-1][19])
        Row6.set(rowss[i-1][20])
        Row16.set(rowss[i-1][21])
        Row7.set(rowss[i-1][22])
        Row17.set(rowss[i-1][23])
        temporary_line1()
        csvfile.close()
    return;
def next_line():
    with open('database.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rowss = list(reader)
        clicked()
        print(str(i))
        BillNumber.set(rowss[i-1][0])
        FirstName.set(rowss[i-1][1])
        Surname.set(rowss[i-1][2])
        Address1.set(rowss[i-1][3])
        City1.set(rowss[i-1][4])
        Enterprise.set(rowss[i-1][5])
        Address2.set(rowss[i-1][6])
        City2.set(rowss[i-1][7])
        Object.set(rowss[i-1][8])
        Day.set(rowss[i-1][9].split(' ')[0])
        Month.set(rowss[i-1][9].split(' ')[1])
        Year.set(rowss[i-1][9].split(' ')[2])
        Row1.set(rowss[i-1][10])
        Row11.set(rowss[i-1][11])
        Row2.set(rowss[i-1][12])
        Row12.set(rowss[i-1][13])
        Row3.set(rowss[i-1][14])
        Row13.set(rowss[i-1][15])
        Row4.set(rowss[i-1][16])
        Row14.set(rowss[i-1][17])
        Row5.set(rowss[i-1][18])
        Row15.set(rowss[i-1][19])
        Row6.set(rowss[i-1][20])
        Row16.set(rowss[i-1][21])
        Row7.set(rowss[i-1][22])
        Row17.set(rowss[i-1][23])
        temporary_line1()
        csvfile.close()
    return;
###################
## Modify Member ##
###################
def modify_member():
##################################################
    aBillNumber     = BillNumber.get()
    aSurname        = Surname.get()
    aFirstName      = FirstName.get()
    anotherBillNum  = "\def \querry{"+aBillNumber+"}"
####################################################
    bottle_list = []
    with open('database.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        bottle_list.extend(reader)
        csvfile.close()
    line_to_override = {int(i)-1:getmember()}
# Write data to the csv file and replace the lines in the line_to_override dict.
    with open('database.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line, row in enumerate(bottle_list):
             data = line_to_override.get(line, row)
             writer.writerow(data)
        csvfile.close()
#############
## Back up ##
#############
    temps  = [datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")]
    union2 = temps+temporary_line+["0=0=0=0"]+getmember()    
    with open('backup_database.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(union2)
        csvfile.close()
#############
## BillNum ##
#############        
    with open('BillNum.txt','w',newline='') as BillNum:
        writer=csv.writer(BillNum)
        writer.writerow([anotherBillNum])
        BillNum.close()
## LaTeX Compile And Rename ##       
    os.system('pdflatex --jobname="Facture_'+aBillNumber+'_'+aSurname+'_'+aFirstName+'" facture.tex')
## For Windows replace rm by del
    delextrafile()  
    return;
##################
## Store Member ##
##################
def store_member():
    aBillNumber     = BillNumber.get()
    aSurname        = Surname.get()
    aFirstName      = FirstName.get()
    anotherBillNum  = "\def \querry{"+aBillNumber+"}"
    line_to_write   = getmember()
##########################################################
    with open('database.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(line_to_write)
        csvfile.close()
#############
## Back up ##
#############
    temps  = [datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")]
    union2 = temps+temporary_line+["+=+=+=+"]+getmember()   
    with open('backup_database.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(union2)
        csvfile.close()
#############
## BillNum ##
#############         
    with open('BillNum.txt','w',newline = '') as BillNum:
        writer=csv.writer(BillNum)
        writer.writerow([anotherBillNum])
        BillNum.close()
## LaTeX Compile And Rename ##
    os.system('pdflatex --jobname="Facture_'+aBillNumber+'_'+aSurname+'_'+aFirstName+'" facture.tex')
## For Windows replace rm by del
    delextrafile()
    return;
########################
## Clear Enter Screen ##
########################
def clear_enter_screen():
    BillNumber.set("")
    FirstName.set("")
    Surname.set("")
    Address1.set("")
    City1.set("")
    Enterprise.set("")
    Address2.set("")
    City2.set("")
    Object.set("")
    Day.set("")
    Month.set("")
    Year.set("")
    Row1.set("")
    Row11.set("0")
    Row2.set("")
    Row12.set("0")
    Row3.set("")
    Row13.set("0")
    Row4.set("")
    Row14.set("0")
    Row5.set("")
    Row15.set("0")
    Row6.set("")
    Row16.set("0")
    Row7.set("")
    Row17.set("0")
    return;
##########
## List ##
##########
dayList     = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",\
                 "16","17","18","19","20","21","22","23","24","25","26","27","28",\
                 "29","30","31"]
monthList   = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet",\
                 "Août","Septembre","Octobre","Novembre","Décembre"]
yearList    = ["2020","2021","2022","2023","2024","2025","2026","2027","2028","2029"]

## ---------------- ##
# Gui Components For Each Row
lblHeading = Label(root, text = "Bill Information", font = ('Arial', 24,"bold")).\
             grid(row = 0,column = 0, columnspan = 4,padx = 20, pady=10)
################
## BillNumber ##
################
lblBillNumber   = Label(root,text="BillNumber",font=('Arial',14,"bold")).grid(row = 1,column = 0)
entryBillNumber = Entry(root, textvariable =BillNumber, width = 10).grid(row =1, column = 1)
################
## Surname ##
################
lblSurname      = Label(root,text="Surname",font=('Arial',14,"bold")).grid(row = 3,column = 0)
entrySurname    = Entry(root, textvariable =Surname, width = 10).grid(row =3, column = 1)
################
## FirstName ##
################
lblFirstName    = Label(root,text="FirstName",font=('Arial',14,"bold")).grid(row = 2,column = 2)
entryFirstName  = Entry(root, textvariable =FirstName, width = 10).grid(row =3, column = 2)
################
## Enterprise ##
################
lblEmail        = Label(root, text="Enterprise",font=('Arial',14,"bold")).grid(row = 4,column = 0)
entryEmail      = Entry(root, textvariable = Enterprise, width = 21).grid(row = 4,column=1 ,columnspan = 2)
################
## Address1 ##
################
lblAddress1     = Label(root,text="Address1",font=('Arial',14,"bold")).grid(row = 6,column = 0)
entryAddress1   = Entry(root, textvariable =Address1, width = 30).grid(row =6, column = 1,columnspan=2)
################
## City1 ##
################
lblCity1        = Label(root,text="City1",font=('Arial',14,"bold")).grid(row = 5,column = 3)
entryCity1      = Entry(root, textvariable =City1, width = 20).grid(row = 6, column = 3,columnspan =2)
################
## Address2 ##
################
lblAddress2     = Label(root,text="Address2",font=('Arial',14,"bold")).grid(row = 8,column = 0)
entryAddress2   = Entry(root, textvariable =Address2, width = 30).grid(row =8,  column = 1,columnspan=2)
################
## City2 ##
################
lblCity2        = Label(root,text="City2",font=('Arial',14,"bold")).grid(row = 7,column = 3)
entryCity2      = Entry(root, textvariable =City2, width = 20).grid(row =8, column = 3, columnspan =2)
################
## Object ##
################
lblObject       = Label(root,text="Object",font=('Arial',14,"bold")).grid(row = 10,column = 0)
entryObject     = Entry(root, textvariable =Object, width = 30).grid(row =10, column = 1, columnspan =2)
################
## Date ##
################
## DropList##
# Day #
lblDay          = Label(root,text="Date",font=('Arial',14,"bold")).grid(row = 11,column = 0)
entryDay        = Entry(root, textvariable =Day, width = 10).grid(row =11, column = 1)
#
droplist        = OptionMenu(root,Day,*dayList)
droplist.config(width=5)
Day.set('1')
droplist.grid(row=11,column=1)
## DropList##
# Month #
entryMonth      = Entry(root, textvariable =Month, width = 10).grid(row =11, column = 2)
#
droplist        = OptionMenu(root,Month,*monthList)
droplist.config(width=5)
Month.set('Janvier')
droplist.grid(row=11,column=2)
## DropList##
# Year #
entryYear       = Entry(root, textvariable = Year, width = 10).grid(row = 11, column = 3)
#
droplist        = OptionMenu(root,Year,*yearList)
droplist.config(width=5)
Year.set('2020')
droplist.grid(row=11,column=3)
################
## Service ##
################
lblService      = Label(root,text="Service",font=('Arial',14,"bold")).grid(row = 12,column = 1)
lblPrix         = Label(root,text="Montant",font=('Arial',14,"bold")).grid(row = 12,column = 3)
#
entryRow1   = Entry(root, textvariable =Row1, width = 30).grid(row =13, column =0,columnspan = 3 )
entryRow11  = Entry(root, textvariable =Row11, width = 10).grid(row =13, column = 3)
entryRow2   = Entry(root, textvariable =Row2, width = 30).grid(row =14, column =0,columnspan = 3 )
entryRow12  = Entry(root, textvariable =Row12, width = 10).grid(row =14, column = 3)
entryRow3   = Entry(root, textvariable =Row3, width = 30).grid(row =15, column =0,columnspan = 3 )
entryRow13  = Entry(root, textvariable =Row13, width = 10).grid(row =15, column = 3)

entryRow4   = Entry(root, textvariable =Row4, width = 30).grid(row =16, column =0,columnspan = 3 )
entryRow14  = Entry(root, textvariable =Row14, width = 10).grid(row =16, column = 3)
entryRow5   = Entry(root, textvariable =Row5, width = 30).grid(row =17, column =0,columnspan = 3 )
entryRow15  = Entry(root, textvariable =Row15, width = 10).grid(row =17, column = 3)
entryRow6   = Entry(root, textvariable =Row6, width = 30).grid(row =18, column =0,columnspan = 3 )
entryRow16  = Entry(root, textvariable =Row16, width = 10).grid(row =18, column = 3)
entryRow7   = Entry(root, textvariable =Row7, width = 30).grid(row =19, column =0,columnspan = 3 )
entryRow17  = Entry(root, textvariable =Row17, width = 10).grid(row =19, column = 3)

#
modify_button       = Button(root,text="Modifier", command=modify_member, bg='orange',fg='white').\
                        grid(row=22,column=3,sticky=E,padx=20,pady=10)
append_button       = Button(root,text="Ajouter", command=store_member, bg='orange',fg='white').\
                        grid(row=22,column=1,sticky=E,padx=20,pady=10)
previous_line_button= Button(root,text="<<", command=previous_line, bg='orange',fg='white').\
                       grid(row=22,column=0,sticky=E,padx=20,pady=10) 
next_line_button    = Button(root,text=">>", command=next_line, bg='orange',fg='white').\
                       grid(row=22,column=2,sticky=E,padx=20,pady=10) 
clear_button        = Button(root,text="clear", command= clear_enter_screen,bg='orange',fg='white').\
                        grid(row=22,column=5,sticky=E,padx=20,pady=10)
root.mainloop()
delextrafile()
