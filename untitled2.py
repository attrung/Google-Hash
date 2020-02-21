# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:16:44 2020

@author: John Nguyen
"""

import csv

# gen pop
genPopBooks = []
genPopLibraries = set()
id = -1
day = -1
currentSignup = False
queue = []

# library
class Library:
    def __init__(self, id, signup, ships, books):
        self.startProcess = False
        self.id = id
        self.signup = int(signup)
        self.ships = int(ships)
        self.books = books
        self.sent = []
        genPopLibraries.add(self)

    def itsScores(self):
        return [x for x in scores if scores.index(x) in self.books]

    def startSignup(self):
        global currentSignup, day, queue
        if self.startProcess == True and currentSignup == False:
            if (self.id, int) not in queue:
                queue.append((self.id, day))
                currentSignup = True
            for item in queue:
                if item[0] == self.id:
                    if day >= item[1] - self.signup:
                        self.sendBooks()
                        currentSignup = False


    def sendBooks(self):
        self.books = sorted(self.books, key=lambda x: self.itsScores(), reverse=True)
        while len(self.books) > 1 and day <= daysForScanning:
            for _ in range(self.ships):
                if len(self.books) > 0:
                    genPopBooks.append((self.id, int(self.books[0])))
                    self.books.pop(0)
                else:
                    pass

    def __repr__(self):
        return f"{self.id}"

# process
class Process:
    def __init__(self, genPop):
        self.genPop = genPop

    def run(self):
        self.sorter()

    def sorter(self):
        self.genPop = sorted(self.genPop, key=lambda x: (x.signup, [-int(x) for x in x.books], [-int(x) for x in x.itsScores()]), reverse=True)
        self.startTimeline()

    def startTimeline(self):
        global day, daysForScanning
        for _ in range(daysForScanning):
            for item in self.genPop:
                item.startProcess = True
                item.startSignup()
            day += 1

    def __str__(self):
        self.run()
        return f"{self.genPop}"


# file handling
with open("b_read_on.txt") as csvfile:
    file = csv.reader(csvfile, delimiter=" ")
    holder = []
    for row in file:
        holder.append(row)
    numberOfLibraries = holder[0][1]
    daysForScanning = int(holder[0][2])
    scores = holder[1]

    holder.pop(0)
    holder.pop(1)

    while len(holder) > 1:
        id += 1
        genPopLibraries.add(Library(id, holder[0][1], holder[0][2], holder[1]))
        holder.pop(0)
        holder.pop(0)

Indigo = Process(genPopLibraries)
print(Indigo)


print("Books:", genPopBooks)
print("Libraries:", genPopLibraries)
print("Day:", day)