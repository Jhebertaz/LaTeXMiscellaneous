from tkinter import *
import tkinter.simpledialog
import sys
import csv
import os
import datetime
def unclicked():
    global i
    i = i - 1
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
        Address2.set(rowss[i-1][5])
        City2.set(rowss[i-1][6])
        Object.set(rowss[i-1][7])
        Day.set(rowss[i-1][8].split(' ')[0])
        Month.set(rowss[i-1][8].split(' ')[1])
        Year.set(rowss[i-1][8].split(' ')[2])
        Row1.set(rowss[i-1][9])
        Row11.set(rowss[i-1][10])
        Row2.set(rowss[i-1][11])
        Row12.set(rowss[i-1][12])
        Row3.set(rowss[i-1][13])
        Row13.set(rowss[i-1][14])
        Row4.set(rowss[i-1][15])
        Row14.set(rowss[i-1][16])
        Row5.set(rowss[i-1][17])
        Row15.set(rowss[i-1][18])
        Row6.set(rowss[i-1][19])
        Row16.set(rowss[i-1][20])
        Row7.set(rowss[i-1][21])
        Row17.set(rowss[i-1][22])
        csvfile.close()
