#Note:-1. list.copy() is method of object 
#      2. list.copy.copy() is function of model 
#      3. list.copy.deepcopy() is function of model
# import copy 
import copy


#################-----------------------------This is shallow copy ----------------------------------#######################


lis=[1,4,6,8,9]
print("this is list",lis)
lis1=lis.copy()                         # we can use copy.copy(lis) also 
print("this is lis ",lis,"id is ",id(lis))
print("this is lis1",lis1,"id is ",id(lis1))
lis1.append(33)
print("after append value ",lis)


                           #########################--dictionary without using shallow copy -----------#################

newlis={'om':'java','raj':'python','akshay':'c++'}
newlis2=newlis
print("newlis id ",id(newlis))
print("newlis2 is ",id(newlis2))
newlis2['omkar']='c'
print(newlis2)
print(newlis)

                       #########################--dictionary using shallow copy -----------#################

newlis={'om':'java','raj':'python','akshay':'c++'}
newlis2=copy.copy(newlis)
print("newlis id ",id(newlis))
print("newlis2 is ",id(newlis2))
newlis2['omkar']='c'
print(newlis2)
print(newlis)


                           

#######################------------------------This is shallow copy but we cant copy inside list that's why we are using deepcopy -----------------------------###################################

new=[[13,4,6],[24,67,22],[90,87,89]]
newlist22=new.copy()
new[0].append('new tab')
print("this is new list",new)
print("this is newlist22",newlist22)












