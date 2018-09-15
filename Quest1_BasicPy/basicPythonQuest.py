# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__  = "47781855"     # replace with your 8 digit student id
__CODING_NAME__ = "Renascence"        # replace with your coding name -

import re
def isSorted(list):
    """ return boolean depending on if list sorted
    >>> isSorted([2,4,7,7,99,122]) -> True
    >>> isSorted(['a','b','c'])  -> True
    >>> isSorted(['a','z','b','c'])  -> False
    constraint: MAY NOT USE: sorted( ) function or sort library
    """
    for i in range(0, len(list) - 1):
        if ((list[i]) > (list[i + 1])):
            return False
    return True



def isSortedAndUnique(list):
    """ return boolean depending on if list sorted
    >>> isSortedAndUnique([2,4,7,7,99,122]) -> False
    >>> isSortedAndUnique(['a','b','c'])  -> True
    >>> isSortedAndUnique(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    for i in range(0, len(list) - 1):
        if ((list[i]) >= (list[i + 1])):
            return False
    return True


def hasUniqueValues(list):
    """ return boolean depending on if list has unique values
    >>> hasUniqueValues([2,4,7,99,122,7]) -> False
    >>> hasUniqueValues(['a','b','c'])  -> True
    >>> hasUniqueValues(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    list2 = list
    list2.sort()
    for i in range(0, len(list) - 1):
        if ((list[i]) == (list[i + 1])):
            return False
    return True


def genSortedArrayUniqueValues(list):
    """ return sorted version of list without duplicates
    >>> genSortedArrayUniqueValues([2,4,7,7,122,99]) -> [2,4,7,99,122]
    >>> genSortedArrayUniqueValues(['a','b','z','c', 'a'])  -> ['a','b','c','z']
    constraint: MAY NOT USE: set
    """
    list2 = list
    list2.sort()
    list3 = []
    for i in range(0, len(list2)):
        if list2[i] not in list3:
            list3.append(list2[i])
    return list3


def listToMapTwoByTwo(list):
    """ return a map based on the order of list elements.
    >>> listToMapTwoByTwo(['foo','bar'])     ->  {"foo":"bar"}
    >>> listToMapTwoByTwo(['a',2, 3,'foo'])  ->  {"a":2,3:'foo'}
    >>> listToMapTwoByTwo([])  -> {}
    """
    dic = {}
    for i in range(0, len(list), 2):
        dic[list[i]] = list[i + 1]
    return dic

def wordsInStringToDictWordCount(s):
    """ return a dict of words in string and count
    >>> wordsInStringToDictWordCount('foo bar   bar') -> {'foo':1, 'bar':2}
    >>> wordsInStringToDictWordCount('') -> {}
    constraint: MAY NOT USE: Counter
    """
    dic = {}
    if s == '':
        return dic
    WordList = re.split(' +',s)
    for i in WordList:
        if i not in dic:
            dic[i] = 0
        dic[i] = dic[i] + 1
    return dic


def reverseWordsInString(string):
    """ return a string with words reversed with one space separators
    >>> reverseWordsInString('foo bar bar baz') -> 'baz bar bar foo'
    constraint: MAY NOT USE: list.reverse()
    """
    ReversedString = ""
    WordList = re.split(' +', string)
    ReversedString = WordList[len(WordList) - 1]
    for i in range(len(WordList) - 2, -1,-1):
        ReversedString = ReversedString + " " + WordList[i]
    return ReversedString



def genListOfOverlaps(list1, list2):
    """ return list of values appearing in both lists
    >>> genListOfOverlaps([2,4,6,8],[6,2,2,9,7]) -> [2,6]
    >>> genListOfOverlaps([2,4,6,8],[2,4,6,8]) -> [2,4,6,8]
    >>> genListOfOverlaps([2,4,6,8],[1,1,9,7]) -> []
    """
    OverLapList = []
    for i in list1:
        if i in list2:
            if i not in OverLapList:
                OverLapList.append(i)
    return OverLapList


def removeDupsNoSet(list):
    """ remove duplicates in the list without using Python Set
    >>> removeDupsNoSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MAY NOT USE: set
    """
    NoDupsList = []
    for i in list:
        if i not in NoDupsList:
            NoDupsList.append(i)
    return NoDupsList


def removeDupsUseSet(list):
    """ remove duplicates in the list  using Python Set
    >>> removeDupsUseSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MUST USE: set
    """
    Set = set()
    for i in list:
        Set.add(i)
    NoDupList = []
    for i in Set:
        NoDupList.append(i)
    return NoDupList

if __name__ == '__main__':
    #write your own test code here
    print ('ready to go')