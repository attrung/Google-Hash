# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:08:48 2020

@author: John Nguyen
"""
import numpy as np

def normalize(a):
    mean = np.mean(a)
    std = np.std(a)
    for i in range(len(a)):
        m = (a[i] - mean)/std
        a[i] = m
    return a

class Library():
    def __init__(self, time_signup, book_per_day, books):
        """
        Init the library
        """
        self.time_signup = time_signup
        self.book_per_day = book_per_day
        self.books = books

    def get_bookscore(self):
        """
        Get book score for the books in library
        """
        self.bookscore = []
        for i in self.books:
            self.bookscore.append(book_val[i])

    def sort_books(self):
        """
        Sort the books by value. 
        Return self.book_list as list of book with decending order.
        """
        self.book_list = []
        self.index_sort = list(np.argsort(self.bookscore)[::-1])
        self.bookscore = sorted(self.bookscore, reverse = True)
        for i in self.index_sort:
            self.book_list.append(self.books[i])

    def get_score(self, n):
        """
        Return score of book (library)
        """
        self.score = []
        for i in range(n):
            if i < self.time_signup:
                self.score.append(0)
            else:
                try:
                    self.score.append(sum(self.bookscore[:(i-self.time_signup)*self.book_per_day]))
                except IndexError:
                    self.score.append(sum(self.bookscore))
        self.score = self.score[::-1]
        self.day_left = 0
        for j in range(1, len(self.score)):
            if self.score[j] == self.score[j-1]:
                self.day_left += 1
            else:
                break
            
def main():
    lib_score_index = []
    lib_signup = []
    for lib in range(len(libraries)):
        libraries[lib].get_bookscore()
        libraries[lib].sort_books()
        libraries[lib].get_score(num_day)
        lib_signup.append(libraries[lib].time_signup)
        
    activation = min(lib_signup)
    a = num_day - activation
    while a > 0:
        print(a)
        temp = []
        time_spare = []
        for i in range(len(libraries)):
            temp.append(libraries[i].score[int(activation)])
            time_spare.append(libraries[i].day_left)
        temp = normalize(temp)
        time_spare = normalize(time_spare)
        lib_signup = normalize(lib_signup)
        score = []
        for i in range(len(libraries)):
            score.append(temp[i] - time_spare[i]*2 - lib_signup[i]*2)        
        sort_list = list(np.argsort(score))[::-1]        
        for i in sort_list:
            if i not in lib_score_index:
                lib_score_index.append(i)
                activation += float(libraries[i].time_signup)
                break
        a = num_day - activation            
    return lib_score_index
        
#
#def main():
#    """
#    This algorithm aims to sort library in terms of best -> worst. Most important one.
#    The list that this gives determines the score. 
#    If list is [0,1], then library 0 is processed first, then library 1
#    """
#    maximum = 0
#    for lib in libraries:
#        maximum = max(lib.time_signup,maximum)
#    util = []
#    for library in libraries:
#        library.get_bookscore()
#        library.sort_books()
#        delta = maximum - library.time_signup
#        scores = library.bookscore
#        num = delta*library.book_per_day 
#        if num < len(scores):
#            maxutil = sum(scores[:num])
#        else:
#            maxutil = sum(scores)
#        util.append(maxutil)
#    lib_score_index = list(np.argsort(util)[::-1])
#    return lib_score_index


def output(libraries, lib_index):
    """
    Print everything (accroding  to required output)
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
    
file_open = "c.txt"
file_save = "c_submit.txt"

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
        num_day = int(org[i][2])
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
