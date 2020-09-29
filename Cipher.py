# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:28:20 2020

@author: Jack.Neville

Caesar Cipher

Create a dictionary where key is number, and value is alphabet char?
Similar setup is the str.maketrans()
Function will take two values; a string, and a number

original: 
    for i in range(0,26):
    dict1[i] = list1[i]
"""
import string

def cipher1(StringValue, ShiftValue):
    ShiftValue # Could create exception to only allow numbers, all other input becomes a zero
    NewString = str() # Need to write a block for handling whitespace
    for x in StringValue:
        CurrentIndex = dict1.get(x)
        NewIndex = (CurrentIndex + ShiftValue) % 26 # 26 = 0 = no shift
        for letter,index in dict1.items():
            if index == NewIndex:
                NewString += letter
    return NewString
list1 = list(string.ascii_lowercase)
dict1 = {list1[i]: i for i in range(0,26)}

def cipher2(text,shift):
    letters = string.ascii_lowercase
    mask = letters[shift:] + letters[:shift]
    trantab = str.maketrans(letters,mask)
    return text.translate(trantab)