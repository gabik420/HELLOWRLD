from tkinter import *
from  tkinter import ttk 
import json
import requests


resJSON=(requests.get('https://www.cbr-xml-daily.ru/daily_json.js')) 
"""                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ хуйня курсы"""
res = json.loads(resJSON.text)

def selection1(event):
    selected = box1.get()
def selection2(event):
    selected = box2.get()
def convertion():
    label.config(text=f"1 {box1.get()} = {1000*res["Valute"][box1.get()]['Value']/res["Valute"][box2.get()]["Value"]} {box2.get()}")
    """                                    ^   MAGIC                 I DONT KNOW WHY BUT DIFF VALUTES GET WRONG CONVERSATION                                          """
#MAIN WIDGET
root = Tk()
root.title('combobox testin')
root.config(bg='black')
root.geometry("250x200")


assetz = ['AUD', 'AZN', 'DZD', 'GBP', 'AMD', 'BHD', 'BYN', 'BGN', 'BOB', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', 'EUR', 'EGP', 'INR', 'IDR', 'IRR', 'KZT', 'CAD', 'QAR', 'KGS', 'CNY', 'CUP', 'MDL', 'MNT', 'NGN', 'NZD', 'NOK', 'OMR', 'PLN', 'SAR', 'RON', 'XDR', 'SGD', 'TJS', 'THB', 'BDT', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'ETB', 'RSD', 'ZAR', 'KRW', 'JPY', 'MMK']
#DEFINITIONS
box1 = ttk.Combobox(root,height=len(assetz),justify='left',values=assetz)
box2 = ttk.Combobox(root,height=len(assetz),justify='left',values=assetz)
button = ttk.Button(text='Convert',command=convertion)
label = ttk.Label(text='',foreground='white',background='black',font='4')
#BINDS
box1.bind("<<ComboboxSelected>>", selection1)
box2.bind("<<ComboboxSelected>>", selection2)

box1.set(assetz[0])
box2.set(assetz[0])

label.place(x=30,y=120)
button.place(relx=0.7, rely=0.8, width=55)
box1.place(relx=0.1,rely=0.1,width=70)
box2.place(relx=0.6,rely=0.1,width=70)

root.mainloop()