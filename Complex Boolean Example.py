# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:48:52 2019

@author: Lawrence
"""
Team=input("Enter your favourite Team;").upper()
Sport=input("Enter yout Sport:").upper()

sportisHockey=False
if Sport== "HOCKEY":
    sportisHockey=True
teamiscorrect=False
if Team== "SENATORS" or Team== "LEAFS":
    teamiscorrect==True
if sportisHockey and teamiscorrect:
    print("Goodluck for the cup this year")
    