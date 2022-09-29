#Author: Yoshiki Hoshinaga
#Date: May 26 2020

#part 1
def flipside(s):
    mid = len(s)//2
    new_string = s[:mid]
    new_string2 = s[mid:]
    return new_string2 + new_string

    
#part 2    
def adjust(s, length):
    output = ''
    new_length = (length - len(s))
    return output * new_length + s

    
    
    
# test code below, do not modify!
if __name__ == '__main__':
    
     print("flipside('homework')",flipside('homework') )
     print("flipside('carpets')", flipside('carpets'))
#part 2
     print("adjust('alien',6)",adjust('alien',6))
     print("adjust('compute',10)",adjust('compute',10))
