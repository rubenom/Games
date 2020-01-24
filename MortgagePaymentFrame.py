# -*- coding: utf-8 -*-
"""
Mortgage Payment Frame

Created on Wed Nov  6 12:23:45 2019

@author: Ruben
"""
class Mortgage():
    def __init__(self):
        self.loanAmount = 0
        self.yearlyInterestRate = 0
        self.years = 0
        self.paymentsPerYear = 0
        
    def calculateMortgagePayment(self):
        # Calculate interest rate for each payment (pit)
        pit = self.yearlyInterestRate / self.paymentsPerYear / 100
        tp = self.years * self.paymentsPerYear     # Total number of payments 
        mortgagePayment = 0
        mortgagePayment = self.loanAmount*(pit*(1+pit)**tp)/(((1+pit)**tp)-1)  
    
        return mortgagePayment    


import tkinter as tk
from tkinter import ttk
import locale
#import Investment

class MortgagePaymentFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="12 10 12 10")
        self.parent = parent
        self.mortgage = Mortgage()
        result = locale.setlocale(locale.LC_ALL, '')
        if result == "C":
            locale.setlocale(locale.LC_ALL, 'en_US')
        # DEfine string variables for text entry fields
        self.loanAmount = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.paymentsPerYear = tk.StringVar()
        self.mortgagePayment = tk.StringVar()
        self.initComponents()
        
    def initComponents(self):
        self.pack()
        ttk.Label(self, text="Loan Amount:").grid(
                column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, 
                  textvariable=self.loanAmount).grid(
                      column=1, row=0)
        ttk.Label(self, text="Yearly Interest Rate").grid(
                column=0, row=1)
        ttk.Entry(self, width=25, 
                  textvariable=self.yearlyInterestRate).grid(
                          column=1, row=1)
        ttk.Label(self, text="Years").grid(
                column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
                      column=1, row=2)
        ttk.Label(self, text="Payments per Year").grid(
                column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.paymentsPerYear).grid(
                      column=1, row=3)
        
        ttk.Label(self, text="Mortgage Payment").grid(
                    column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.mortgagePayment,
                  state="readonly").grid(column=1, row=4)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=6, pady=3)
        
    def makeButtons(self):
        # create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=5, columnspan=2, sticky=tk.E)
        ttk.Button(buttonFrame, text="Calculate", 
                   command=self.calculate).grid(column=0, row=0, padx=6)
        ttk.Button(buttonFrame, text="Exit", 
                   command=self.parent.destroy).grid(column=1, row=0)
    
    def calculate(self):
        self.mortgage.loanAmount = float(
                self.loanAmount.get())
        self.mortgage.yearlyInterestRate = float(
                self.yearlyInterestRate.get())
        self.mortgage.years = int(self.years.get())
        self.mortgage.paymentsPerYear = int(self.paymentsPerYear.get())
        self.mortgagePayment.set(locale.currency(
                self.mortgage.calculateMortgagePayment(), grouping=True))
    
if __name__ == "__main__":
    root = tk.Tk() 
    root.title("Mortgage Payment Calculator")
    MortgagePaymentFrame(root)
    root.mainloop()
                        
    