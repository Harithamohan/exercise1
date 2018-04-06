#! /usr/bin/python

#this is the  program to print vowels and consonant letters from gnulinux

list1 = [ ]

list2 = [ ]

for c in "gnulinux":

  if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
                                                                
    list1.append (c)

  else:

    list2.append (c) 

print("the vowles are",list1)

print("the consonants are",list2)


  


