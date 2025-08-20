check_string="omkarganpatraoranher"
dict={}
for i in check_string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for key in dict:
    print(key,"_",dict[key])