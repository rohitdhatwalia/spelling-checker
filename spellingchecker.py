from textblob import TextBlob
n = int(input("enter a number: "))
mylist = []
for i in range(1 , n+1):
    e = input("enter word : ")
    mylist.append(e)
corrected_list = []
for word in mylist:
    corrected_list.append(TextBlob(word))
print("corrected list words are:")
for word in corrected_list:
    print(word.correct(),end=" ")
