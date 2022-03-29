# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:48:35 2022

@author: Javohir_T
"""
print('buyurtmalarni tanlang')
buyurtmalar=[]
n=1
while True:
    savol=f"{n}-buyurtmani tanlang"
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    takrorlash=input("yana qoshasizmi ha\yoq")
    n+=1
    if takrorlash=='yoq':
        break
print("buyurtmalar royxati")
for buyurtma in buyurtmalar:
    print(buyurtma.title())    
    

