# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:08:48 2020

@author: John Nguyen
"""
import numpy as np

class Library():
    def __init__(self, time_signup, book_per_day, books):
        """
        Init the library
        """
        self.time_signup = time_signup
        self.book_per_day = book_per_day
        self.books = books

    def get_bookscore(self):
        self.bookscore = []
        for i in self.books:
            self.bookscore.append(book_val[i])

    def sort_books(self):
        self.book_list = []
        self.index_sort = list(np.argsort(self.bookscore)[::-1])
        self.bookscore = sorted(self.bookscore, reverse = True)
        for i in self.index_sort:
            self.book_list.append(self.books[i])

    def get_score(self):
        ans = sum(self.bookscore)
        self.score = ans

def main():
    lib_score = []
    lib_time = []
    lib_per_day = []
    score= []
    for library in libraries:
        library.get_bookscore()
        library.sort_books()
        library.get_score()
        lib_score.append(library.score)
        lib_time.append(library.time_signup)
        lib_per_day.append(library.book_per_day)
        score.append(library.score*5 - library.time_signup*(-1000) + library.book_per_day*100)
    lib_score_index = list(np.argsort(score)[::-1])
    return lib_score_index
        

#def main():
#    maximum = 0
#    for lib in libraries:
#        maximum = max(lib.time_signup,maximum)
#    util = []
#    for library in libraries:
#        library.get_bookscore()
#        library.sort_books()
#        library.get_score()
#        delta = maximum - library.time_signup
#        scores = library.bookscore
#        num = delta*library.book_per_day
#        if num < len(scores):
#            maxutil = sum(scores[:num])
#        else:
#            maxutil = sum(scores[:len(scores)])
#        util.append(maxutil)
#    lib_score_index = list(np.argsort(util)[::-1])
#    return lib_score_index


def output(libraries, lib_index):
    """
    Take a list of libraries, calculate output time, and list of books.
    Books are stored already in libraries, from high -> low.

    list of books in libraries can be accessed as lib.book_list
    """
    fh = open("submit/" + file_save, "w+")
    temp_activate = 0
    for i in lib_index:
        lib = libraries[i]
        temp_activate += float(lib.time_signup)
        if int(num_day) - temp_activate < 0:
            fh.write(str(lib_index.index(i)))
            break
        elif lib_index.index(i) == len(lib_index) - 1 and int(num_day) > temp_activate:
            fh.write(str(len(lib_index)))
            
    
    activation = 0
    for i in lib_index:
        lib = libraries[i]
        activation += float(lib.time_signup)   
        if int(num_day) - activation < 0:
            break
        total_book = int(min(lib.book_per_day*(int(num_day) - activation) + 1, len(lib.books)))
        fh.write("\n")          
        fh.write(' '.join([str(i), str(total_book)]))  
        book_list = lib.book_list[:total_book]
        for k in range(len(book_list)):
            book_list[k] = str(book_list[k])
        fh.write("\n")
        fh.write(' '.join(book_list))  
    fh.close()
    

file_open = "f.txt"
file_save = "f_submit.txt"

#importing the data
org = open(file_open,"r")
org = org.read()
org = org.split("\n")
org = org[:-1]
libraries = []
for i in range(len(org)):
    if i == 0:
        org[i] = org[i].split()
        num_books = org[i][0]
        num_lib = org[i][1]
        num_day = org[i][2]
    if i == 1:
        book_val = org[i].split()
        for i in range(len(book_val)):
            book_val[i] = int(book_val[i])
    elif i %2 == 0 and i!= 0 and i < len(org) -1:
        org[i] = org[i].split()
        org[i + 1] = org[i+1].split()
        books = org[i+1]
        for j in range(len(books)):
            books[j] = int(books[j])
        libraries.append(Library(int(org[i][1]), int(org[i][2]), books))

#running everything and get output
lib_index = main()
output(libraries, lib_index)
#save file
