###########################################----------------------deepcopy-------------###########################################################
import copy

lis=[[1,2,3,4],[6,78],[34]]# this is imutable
new_lis=copy.deepcopy(lis)                                     #this is deepcopy which create another value with new id 
print("this is data from lis",lis," and id is ",id(lis) )
print("this is data from new_lis",new_lis," and id is ",id(new_lis) )

lis[0].append('new value')
print("new_lis is ",new_lis)
print("lis after append",lis)
