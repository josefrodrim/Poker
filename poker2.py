# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:53:02 2020

@author: josel
"""

import os
import sys
import re

#
# Kind of Cards and Order of Values
#
kind = ['S', 'C', 'D', 'H']
order = ['2', '3', '4', '5', '6', '7',
         '8', '9', 'T', 'J', 'Q', 'K', 'A']

#
# Ordering Algorithm
#
def ordering(list, order):

    return [x for x in order for y in list if y == x]

#
# Checking Consecutive Number Algorithm
#
def isConsec(list):

    ordered = ordering(list, order)
    count = len(list)
    for i in range(0, 13):
        if ordered == ordering((order + order)[i:i+count], order):
            # Return True and Value of highest card
            return [True, ordered[-1]]

    return [False]


#
# Gamer Class
#
class Gamer():

    card = []
    grade = 0
    highest = ''

    def __init__(self, name):
        self.name = name

    #
    # Check Royal Straight Flush (Grade 10)
    # Return True or False
    #
    def ro_str_flu(self):

        for kin in kind:
            if self.card[1].count(kin) == 5:
                place = [i for i, x in enumerate(self.card[1]) if x == kin]
                get_val = [ self.card[0][x] for x in place ]

                if ordering(get_val, order) == ['T', 'J', 'Q', 'K', 'A']:
                    self.grade = 10
                    self.highest = 'A'
                    return True

        return False

    #
    # Check Straight Flush (Grade 9)
    # Return True or False
    #
    def str_flu(self):

        for kin in kind:
            if self.card[1].count(kin) == 5:
                place = [i for i, x in enumerate(self.card[1]) if x == kin]
                get_val = [ self.card[0][x] for x in place ]
                result = isConsec(get_val)

                if result[0]:
                    self.grade = 9
                    self.highest = result[1]
                    return True

        return False

    #
    # Check Four Cards (Grade 8)
    # Return True or False
    #
    def four_cards(self):

        for x in order:
            if self.card[0].count(x) == 4:
                self.grade = 8
                self.highest = x
                return True

        return False

    #
    # Check Full House (Grade 7)
    # Return True or False
    #
    def full_house(self):

        for x in order:
            if self.card[0].count(x) == 3:
                for y in order:
                    if y != x and self.card[0].count(y) == 2:
                        self.grade = 7
                        self.highest = x
                        return True

        return False

    #
    # Check Flush (Grade 6)
    # Return True or False
    #
    def flush(self):

        for x in kind:
            if self.card[1].count(x) == 5:
                self.grade = 6
                self.highest = ordering(self.card[0], order)
                return True

        return False

    #
    # Check Straight (Grade 5)
    # Return True or False
    #
    def straight(self):

        result = isConsec(self.card[0])
        if result[0] == True:
            self.grade = 5
            self.highest = ordering(self.card[0], order)
            return True

        return False

    #
    # Check Triple (Grade 4)
    # Return True or False
    #
    def triple(self):

        for x in order:
            if self.card[0].count(x) == 3:
                self.grade = 4
                self.highest = x
                return True

        return False


    #
    # Check Two Pairs (Grade 3)
    # Return True or False
    #
    def two_pair(self):

        for x in order:
            if self.card[0].count(x) == 2:
                for y in order:
                    if self.card[0].count(y) == 2 and y != x:
                        self.grade = 3
                        self.highest = ordering([x,y], order)
                        return True

        return False


    #
    # Check One Pair (Grade 2)
    # Return True or False
    #
    def one_pair(self):

        for x in order:
            if self.card[0].count(x) == 2:
                self.grade = 2
                self.highest = x
                return True

        return False

    #
    # Check High Card (Grade 1)
    # Return name who have higher card
    #
    def high_card(self):

        self.grade = 1
        self.highest = ordering(self.card[0],order)

        return True

    functions = [ ro_str_flu, str_flu, four_cards,
                  full_house, flush, straight,
                  triple, two_pair, one_pair, high_card ]

    Grade = [ '', 'High Card', 'Pair', 'Two Pair', 'Triple', 'Straight', 'Flush',
              'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Straight Flush']

    #
    # Check out what Gamer has
    #
    def what_has(self):

        for function in self.functions:
            result = function(self)
            if result == True:
                return

#
# Compare with Pop
#
def compare_pop(list1, list2):

    while True:
        try :
            temp_1 = list1.pop()
            temp_2 = list2.pop()
        except IndexError : return -1

        if order.index(temp_1) > order.index(temp_2):
            return 0
        elif order.index(temp_1) < order.index(temp_2):
            return 1
