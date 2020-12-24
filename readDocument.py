# -*- coding: utf-8 -*-

f = open("musteriler2.txt","r")
# print(f.read())
print("************")
print(f.readline())
print(f.readline())

for l in f:
    print(l)
    
fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("\n")
fileToAppend.write("Akin")
fileToAppend.write("\n")
fileToAppend.write("Berk")
fileToAppend.write("Mehmet")
fileToAppend.close()

import os

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("Dosya yok")


os.rmdir("empty")
