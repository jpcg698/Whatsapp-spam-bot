from pickle import FALSE
import tkinter as tk
from tkinter import HORIZONTAL, ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title('Whatsapp Spam bot')
        self.spam_amount = tk.IntVar(self)
        self.spam_amount.set(1)
        self.spam_text = tk.StringVar(self)
        self.spam_text.set("Hola!! :33")
        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 4, 'pady': 3}

        # title label
        title_label = ttk.Label(self,  text='Hola, configura tu spam:')
        title_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # spam text label
        label_spam_text = ttk.Label(self,  text='Que quieres mandar?:')
        label_spam_text.grid(column=0, row=1, sticky=tk.W, **paddings)

        #spam text
        entry_spam = ttk.Entry(self, textvariable=self.spam_text)
        entry_spam.grid(column=1,row=1,sticky=tk.W, **paddings)

        # spam amount label
        label_spam_amount = ttk.Label(self,  text='Cuantas veces lo quieres mandar?:')
        label_spam_amount.grid(column=0, row=2, sticky=tk.W, **paddings)

        #spam value
        entry_spam_amount = ttk.Spinbox(
            self, from_=1, to= 500, textvariable=self.spam_amount)

        entry_spam_amount.grid(column=1, row=2, sticky=tk.W, **paddings)

        # output Button
        results_button = ttk.Button(self,text="Abrir whatsapp", command=self.openWhatsapp)
        results_button.grid(column=0,row=3,sticky=tk.W, **paddings)

        spam_button = ttk.Button(self,text="Enviar spam", command=self.sendSpam)
        spam_button.grid(column=1,row=3,sticky=tk.W, **paddings)

        quit_button = ttk.Button(self,text="Cerrar", command=self.quitDriver)
        quit_button.grid(column=0,row=4,sticky=tk.W, **paddings)

        #message boxes
        #connect with qr and select correct chat
        

    def openWhatsapp(self, *args):
        global driver
        if not driver:
            driver = webdriver.Chrome()
            driver.get("https://web.whatsapp.com")
            messagebox.showinfo(title=None, message="Logeate con tu QR y elije el chat a spamear")

        

    def sendSpam(self, *args):
        text = self.spam_text.get()
        amount = self.spam_amount.get()
        time.sleep(2)
        for i in range(amount):
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
            input_box = driver.find_element("xpath",inp_xpath)
            time.sleep(2)
            input_box.send_keys(text + Keys.ENTER)
            time.sleep(2)
    
    def quitDriver(self, *args):
        if driver:
            driver.quit()
        app.destroy()


def quitDriverMain():
        if driver:
            driver.quit()
        app.destroy()

if __name__ == "__main__":
    driver = None
    app = App()
    app.protocol("WM_DELETE_WINDOW", quitDriverMain)
    app.mainloop()