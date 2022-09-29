
#
#Author:Yoshiki Hoshinaga
#Date: May 26 2020
#Title: Problem set 3 part 4

#Part 1
def letter_score(letter):
    if (letter in ['a','e','i','l','n','o','r','s','t','u']):
        return 1
    elif(letter in ['d','g']):
        return 2
    elif(letter in ['b','c','m','p']):
        return 3
    elif(letter in ['f','h','v','w','y']):
        return 4
    elif(letter in['k']):
        return 5
    elif(letter in['j','x']):
        return 8
    elif(letter in['q','z']):
        return 10
    else:
        return 0
#Part 2
def scrabble_score(word):
    if len(word)==0:
        return 0
    
    return letter_score(word[0]) + scrabble_score(word[1:])
#test 3
def add(vals1, vals2):
    if (len(vals1)==0):
        return []
    else:
        x = vals1[0] + vals2[0];
        return [x] + add(vals1[1:],vals2[1:])
#test 4
def weave(s1, s2):
    if s1 and s2:
        return s1[0] + s2[0] + weave(s1[1:],s2[1:])
    elif s1:
        return s1
    else:
        return s2

#test
if __name__ == '__main__':

#test for part 1    
    print(letter_score('w'))
    print(letter_score('q'))
    print(letter_score('%'))
    print(letter_score('A'))
#test for part 2
    print(scrabble_score('python'))
    print(scrabble_score('a'))
    print(scrabble_score('quetzal'))
#test for part 3
    print(add([1, 2, 3], [3, 5, 8]))
    print(add([2, 3, 4, 5], [-3, -2, -1, 0]))
    print(add([], []))
#test for part 4
    print(weave('aaaaaa', 'bbbbbb'))
    print(weave('abcde', 'VWXYZ'))
    print(weave('aaaaaa', 'bb'))
    print(weave('aaaa', 'bbbbbb'))
    print(weave('aaaa', ''))
    print(weave('', 'bbbb'))
    print(weave('', ''))
