#Author: Yoshiki Hoshinaga
#Date: May 26 2020

#part 1
def copy(s,n):
    if n<1:
        return ''
    else:
        return s + copy(s, n-1)
#part2
def compare(list1, list2):
    if len(list1)==0 or len(list2)==0:
        return 0
    else:
        c = 0
        if list1[0] < list2[0]:
            c =1
        return c + compare(list1[1:], list2[1:])
#part 3
def double(s):
    if(s==''):
        return s
    else:
        return s[0]+s[0]+double(s[1:])
        
    

    
#Test
if __name__ == '__main__':
    
#test for part 1
    print(copy('da',2))
    print(copy('Go BU!',4))
    print(copy('hello',0))
    print(copy('hello',-7))

#test for part 2
    print('compare([5,3,7,9,1],[2,4,7,8,3]',compare([5,3,7,9,1],[2,4,7,8,3]))
    print('compare([4, 2, 3, 7], [1, 5]) ', compare([4, 2, 3, 7], [1, 5]))
    print('compare([4, 2, 3], [6, 5, 0, 8])',compare([4, 2, 3], [6, 5, 0, 8]))
    print('compare([5, 3], [])',compare([5, 3], []))
    print('compare([], [5, 3, 7])',compare([], [5, 3, 7]))

#test for part 3
    print(double('hello'))
    print(double('python'))
