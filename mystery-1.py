#Author:Yoshiki Hoshinaga
#Date: May 26 2022

#problem 1
def mystery(a,b):
    if a==b:
        return a
    else:
        myst_rest = mystery(a + 1, b- 2)
        return b + myst_rest


#Testing function
print('mystery(0,9) is',mystery(0,9))
