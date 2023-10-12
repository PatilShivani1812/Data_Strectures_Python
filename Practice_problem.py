# # List Duplicates remove
# li= [1,2,3,4,5,2,3,4,7,9,5]
# li1 = []
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)

# #. find the unique characters in given string 
# chart  = "bdbac353@#2c&191#"
# #uni = [b,d,a,c,3,5,3,@,#,2,&,1]
# uni_chart = []
# for i in chart:
#     if i not in uni_chart:
#         uni_chart.append(i)
# print(uni_chart)

#show only duplicates value in list
# li = [10, 20, 30, 40, 50, 10, 20, 10]
# li1 = []
# duplicates_li=[]
# n = len(li)
# for i in range(n):
#     for j in range(i+1,n):
#         if li[i] ==li[j] and li[i] not in li1:
#             duplicates_li.append(li[i])
#             li1.append(li[i])
# print("Duplicate value",duplicates_li)

# li = [10,20,30,40,50,10,20,10]
# li1= []
# for i in li:
#     count_value = li.count(i)
#     print(count_value)
#     if count_value > 1:
#         if li1.count(i) == 0:#Check if the element (i) has not been added to the li1 list before. If it hasn't, proceed to the next step.
#             li1.append(i)
# print(li1)

# #3. insertion sort
# li = [1,35,6,3,7,3,8,2,0]
# length_li = len(li)
# for i in range(length_li):
#     for j in range(i+1,length_li):
#         if li[i] < li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)

# #Bubble Sort
# li = [1,35,6,3,7,3,8,2,0]
# len_li = len(li)
# for i in range(len_li):
#     for j in range(i+1,len_li):
#         if li[i] > li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)

# #odd & even separation
# li = [3,5,4,9,8,5,7,8,12]
# odd_li = []
# even_li =[]
# for i in li:
#     if i % 2 == 0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
# print("even_li",even_li)
# print("odd_li",odd_li)

#second largest number of list 
# li = [20, 30, 40, 25, 10]
# li.sort()
# print(li)
# print(li[-2])

# li = [20, 30, 40, 25, 10]
# len_li = len(li)

# for i in range(len_li):
#     for j in range(i+1,len_li):
#         if li[i] > li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li[-2])

# # print the elements of an list:
# li = [1, 2, 3, 4, 5,6,7]
# for i in li:
#     print(i,end=" ")

# # even at front and odd at back
# li = [1,6, 2, 3, 8, 7, 4]
# even_li = []
# odd_li = []
# for i in li:
#     if i % 2 == 0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
# print(even_li+odd_li)

# # elements of an array in reverse order
# li = [1, 2, 3, 4, 5]
# rev_li = li[::-1]
# print(rev_li)



# #Merge two dictionaries
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'c': 6, 'd': 4}
# # Using update()
# dict1.update(dict2)
# print(dict1)
# # Using {**d1,**d2}
# merged_dict = {**dict1,**dict2}
# print(merged_dict)
# #Using Union
# union_dic = dict1|dict2
# print(union_dic)

# Duplicate words from sentence
s = ["I am very happy am "]
li = []
sentence = s[0]
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0)+1
    if word_count[word]>1 and word not in li:
        li.append(word)
print("duplicate words",li)
    
