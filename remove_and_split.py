def remove_and_split(string,word):
    newstr= string.replace(word," ")
    return newstr.strip()
this = (" rahul is a good boy")
n =remove_and_split(this,"rahul")
print(n)
#print(this)
#print(this.strip)
