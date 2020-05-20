from tkinter import *
import tkinter.simpledialog
import sys
import csv
import os
import datetime
def modify_member():
##################################################
    aBillNumber=BillNumber.get()
    aFirstName=FirstName.get()
    aSurname=Surname.get()
    aAddress1=Address1.get()
    aCity1=City1.get()
    aAddress2=Address2.get()
    aCity2=City2.get()
    aObject=Object.get()
    aDay=Day.get()
    aMonth=Month.get()
    aYear=Year.get()
    aRow1=Row1.get()
    aRow11=Row11.get()
    aRow2=Row2.get()
    aRow12=Row12.get()
    aRow3=Row3.get()
    aRow13=Row13.get()
    aRow4=Row4.get()
    aRow14=Row14.get()
    aRow5=Row5.get()
    aRow15=Row15.get()
    aRow6=Row6.get()
    aRow16=Row16.get()
    aRow7=Row7.get()
    aRow17=Row17.get()
    aDate= aDay+" "+aMonth+" "+aYear
    anotherBillNum = "\def \querry{"+aBillNumber+"}"
####################################################
    bottle_list = []
    with open('database.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        bottle_list.extend(reader)
        csvfile.close()
    line_to_override = {int(i)-1:[aBillNumber,aFirstName,aSurname,aAddress1,aCity1,aAddress2,aCity2,aObject,aDate,\
                        aRow1,aRow11,aRow2,aRow12,aRow3,aRow13,aRow4,aRow14,aRow5,aRow15,aRow6,aRow16,aRow7,aRow17] }
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
    with open('backup_database.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),aBillNumber,aFirstName,aSurname,aAddress1,aCity1,aAddress2,aCity2,aObject,aDate,\
                        aRow1,aRow11,aRow2,aRow12,aRow3,aRow13,aRow4,aRow14,aRow5,aRow15,aRow6,aRow16,aRow7,aRow17])
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
    os.system('rm *.synctex.gz')
    os.system('rm *.aux')
    os.system('rm *.log')  
    return;
