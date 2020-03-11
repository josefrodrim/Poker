#---------------------------------------
# AUTOR: JOSEF RENATO RODRIGUEZ MALLMA
# LIMA - PERU 
#---------------------------------------


#---------------------------------------
# VALUES OF CARDS 
#---------------------------------------
kind = ['S', 'C', 'D', 'H']
order = ['2', '3', '4', '5', '6', '7',
         '8', '9', 'T', 'J', 'Q', 'K', 'A']



#---------------------------------------
# ORDERING ALGORITH
#---------------------------------------

def ordering(list, order):

    return [x for x in order for y in list if y == x]

#---------------------------------------
# FOR COMPARE HANDS WHEN EXIST SAME PLAY
#---------------------------------------
    

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
  
#---------------------------------------
# RETURN VALUE CARD OF HIGH 
#---------------------------------------      
        
def isConsec(list):

    ordered = ordering(list, order)
    count = len(list)
    for i in range(0, 13):
        if ordered == ordering((order + order)[i:i+count], order):
            return [True, ordered[-1]]

    return [False]

#---------------------------------------
# CLASS POKER HAND CONSTRUCTOR AND FUNCTIONS OF HANDS
#---------------------------------------   
    
class pokerHand:
    
    def __init__(self,card):
                    
        self.card = [ [ x[0] for x in card.split() ], [ x[1] for x in card.split() ]]
        self.what_has()
    
    grade = 0
    highest = ''

#---------------------------------------
# GRADE 10 AND ROYAL STRAIGHT FLUSH
#---------------------------------------   
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

#---------------------------------------
# GRADE 9 AND STRAIGHT FLUSH
#---------------------------------------  
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

#---------------------------------------
# GRADE 8  AND FOUR OF A KIND
#---------------------------------------  
    def four_cards(self):

        for x in order:
            if self.card[0].count(x) == 4:
                self.grade = 8
                self.highest = x
                return True

        return False

#---------------------------------------
# GRADE 7  FULL HOUSE
#---------------------------------------  
    def full_house(self):

        for x in order:
            if self.card[0].count(x) == 3:
                for y in order:
                    if y != x and self.card[0].count(y) == 2:
                        self.grade = 7
                        self.highest = x
                        return True

        return False

#---------------------------------------
# GRADE 6  FLUSH/COLOR
#---------------------------------------  
    def flush(self):

        for x in kind:
            if self.card[1].count(x) == 5:
                self.grade = 6
                self.highest = ordering(self.card[0], order)
                return True

        return False

#---------------------------------------
# GRADE 5  STRAIGHT
#---------------------------------------  
    def straight(self):

        result = isConsec(self.card[0])
        if result[0] == True:
            self.grade = 5
            self.highest = ordering(self.card[0], order)
            return True

        return False

#---------------------------------------
# GRADE 4  TRIPLE
#---------------------------------------  
    def triple(self):

        for x in order:
            if self.card[0].count(x) == 3:
                self.grade = 4
                self.highest = x
                return True

        return False


#---------------------------------------
# GRADE 3  TWO PAIR
#---------------------------------------  
    def two_pair(self):

        for x in order:
            if self.card[0].count(x) == 2:
                for y in order:
                    if self.card[0].count(y) == 2 and y != x:
                        self.grade = 3
                        self.highest = ordering([x,y], order)
                        return True

        return False


#---------------------------------------
# GRADE 2  PAIR
#---------------------------------------  
    def one_pair(self):

        for x in order:
            if self.card[0].count(x) == 2:
                self.grade = 2
                self.highest = x
                return True

        return False

#---------------------------------------
# GRADE 1  HIGH CARD
#---------------------------------------  
    def high_card(self):

        self.grade = 1
        self.highest = ordering(self.card[0],order)

        return True
#---------------------------------------
# FUNCTIONS FOR EACH PLAY
#---------------------------------------  
    functions = [ ro_str_flu, str_flu, four_cards,
                  full_house, flush, straight,
                  triple, two_pair, one_pair, high_card ]
#---------------------------------------
# GRADE OF PLAY
#---------------------------------------  
    Grade = [ '', 'High Card', 'Pair', 'Two Pair', 'Triple', 'Straight', 'Flush',
              'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Straight Flush']

    
#---------------------------------------
# FUNCTION FOR COMPARE 2 HANDS
#---------------------------------------  
    def compare_with(self, other):

        if self.grade > other.grade:
           return "WIN"
        elif self.grade < other.grade:
            return "LOSE"
        else :
            if len(self.highest) == 1:
                if order.index(self.highest) > order.index(other.highest):
                    return "WIN"
                    
                elif order.index(self.highest) < order.index(other.highest):
                        
                        return "LOSE"
                        
                else :
                        
                        return  "WIN" 
                         
            else :
                result = compare_pop(self.highest, other.highest)
                if result == 1:
                    return 'LOSE'
                elif result == 0:
                    
                    return 'WIN'
                    
                else :
                      return  "WIN"

#---------------------------------------
# FUNCTION FOR ACTIVATE ALL FUNCTIONS-PLAY 
#---------------------------------------          
        
        
    def what_has(self):
        for function in self.functions:
            result = function(self)
            if result == True:
                return



#---------------------------------------
# TEST UNIT  
#---------------------------------------   
                
import unittest


class TestStringMethods(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue(pokerHand("TC TH 5C 5H KH").compare_with(pokerHand("9C 9H 5C 5H AC")) == 'WIN') 
        self.assertTrue(pokerHand("TS TD KC JC 7C").compare_with(pokerHand("JS JC AS KC TD")) == 'LOSE') 
        self.assertTrue(pokerHand("7H 7C QC JS TS").compare_with(pokerHand("7D 7C JS TS 6D")) == 'WIN') 
        self.assertTrue(pokerHand("5S 5D 8C 7S 6H").compare_with(pokerHand("7D 7S 5S 5D JS")) == 'LOSE') 
        #self.assertTrue(pokerHand("AS AD KD 7C 3D").compare_with(pokerHand("AD AH KD 7C 4S")) == 'LOSE') 
        self.assertTrue(pokerHand("TS JS QS KS AS").compare_with(pokerHand("AC AH AS AS KS")) == 'WIN') 
        self.assertTrue(pokerHand("TS JS QS KS AS").compare_with(pokerHand("TC JS QC KS AC")) == 'WIN') 
        self.assertTrue(pokerHand("TS JS QS KS AS").compare_with(pokerHand("QH QS QC AS 8H")) == 'WIN') 
        self.assertTrue(pokerHand("AC AH AS AS KS").compare_with(pokerHand("TC JS QC KS AC")) == 'WIN') 
        self.assertTrue(pokerHand("AC AH AS AS KS").compare_with(pokerHand("QH QS QC AS 8H")) == 'WIN') 
        self.assertTrue(pokerHand("TC JS QC KS AC").compare_with(pokerHand("QH QS QC AS 8H")) == 'WIN') 
        self.assertTrue(pokerHand("7H 8H 9H TH JH").compare_with(pokerHand("JH JC JS JD TH")) == 'WIN') 
        self.assertTrue(pokerHand("7H 8H 9H TH JH").compare_with(pokerHand("4H 5H 9H TH JH")) == 'WIN') 
        self.assertTrue(pokerHand("7H 8H 9H TH JH").compare_with(pokerHand("7C 8S 9H TH JH")) == 'WIN') 
        self.assertTrue(pokerHand("7H 8H 9H TH JH").compare_with(pokerHand("TS TH TD JH JD")) == 'WIN') 
        self.assertTrue(pokerHand("7H 8H 9H TH JH").compare_with(pokerHand("JH JD TH TC 4C")) == 'WIN') 
        self.assertTrue(pokerHand("JH JC JS JD TH").compare_with(pokerHand("4H 5H 9H TH JH")) == 'WIN') 
        self.assertTrue(pokerHand("JH JC JS JD TH").compare_with(pokerHand("7C 8S 9H TH JH")) == 'WIN') 
        self.assertTrue(pokerHand("JH JC JS JD TH").compare_with(pokerHand("TS TH TD JH JD")) == 'WIN') 
        self.assertTrue(pokerHand("JH JC JS JD TH").compare_with(pokerHand("JH JD TH TC 4C")) == 'WIN') 
        self.assertTrue(pokerHand("4H 5H 9H TH JH").compare_with(pokerHand("7C 8S 9H TH JH")) == 'WIN') 
        self.assertTrue(pokerHand("4H 5H 9H TH JH").compare_with(pokerHand("TS TH TD JH JD")) == 'LOSE') 
        self.assertTrue(pokerHand("4H 5H 9H TH JH").compare_with(pokerHand("JH JD TH TC 4C")) == 'WIN') 
        self.assertTrue(pokerHand("7C 8S 9H TH JH").compare_with(pokerHand("TS TH TD JH JD")) == 'LOSE') 
        self.assertTrue(pokerHand("7C 8S 9H TH JH").compare_with(pokerHand("JH JD TH TC 4C")) == 'WIN') 
        self.assertTrue(pokerHand("TS TH TD JH JD").compare_with(pokerHand("JH JD TH TC 4C")) == 'WIN')

if __name__ == '__main__':
    unittest.main()
    
