#!/usr/bin/env python3

class Coffee:
    
    def __init(self, size, price):
        self.size = size
        self.price = price

    size = input("Please enter what size coffee (small, medium or large): ")
    if( size != Small or    Medium or Large):
       size = input("Please enter what size coffee (small, medium or large): ") 
    
   
    price = input("Please enter tip amount: ")

    def tip(self):
        print("This coffee is great! here's  a tip!")
        self.price+=1
        


