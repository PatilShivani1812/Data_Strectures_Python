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


# str1 = "i like this program very much"
# # output =much very program this like i
# split_str = str1.split()
# # print(split_str)
# rever_split_str = split_str[::-1]
# # print(rever_split_str)
# reverse_str = " ".join(rever_split_str)
# print(reverse_str)

# str1 = ["geeeeksforgeeks", "geeeeks", "geeeek", "geeeezer"]
# # str1= []
# if not str1:
#     print("Empty Li")
# str1.sort()
# first_str1 = str1[0]
# end_str1 = str1[-1]
# li = []
# for i in range(len(first_str1)):
#     if i <len(end_str1) and first_str1[i] ==end_str1[i]:
#         li.append(first_str1[i])
        
#     else:
#         break
# print("".join(li))
#Write a Python program to count the number of vowels in a string.
# str1 = "Hellio, World!"
# vowels = "aeiouAEIOU"
# total = 0
# for i in str1:
#     if i in vowels:
#         total= total+1
# print(total)
# Write a Python program to find the most frequent character in a string.
# str1 = "Heeello, World!"  
# dic ={}
# for i in str1:
#     dic[i] = dic.get(i , 0 )+1

# print(dic)
# most_freq = max(dic,key = dic.get)
# print(most_freq)
# Write a Python program to remove all duplicates from a string and return the result.
# s = "Heeello, World!"
# str1 = ""
# for i in s:
#     if i not in str1:
#         str1 = str1+i
# print(str1) #Helo, Wrd!
# Write a Python program to check if a string contains only digits.
# str1 = "12345"
# digit_str = str1.isdigit()
# print(digit_str)

# # Write a Python program to count the occurrences of each word in a sentence.
# stan = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# new_stan = stan.split()
# # print(new_stan)
# dic = {}
# for word in new_stan:
#     clean_word = word.strip(".,!?;:'/")
#     clean_word_low = clean_word.lower()
#     dic[clean_word_low] = dic.get(clean_word_low,0)+1
# print(dic)

# Write a Python program to capitalize the first letter of each word in a sentence.
# stanse = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# new_stanse = stanse.split()
# # print(new_stanse)
# li = []
# for word in new_stanse:
#     capi = word[0:].capitalize()
#     li.append(capi)
# print(li)
# Write a Python program to find the longest word in a sentence.
# stanse = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# new_sta = stanse.split()
# long_word = ""
# for word in new_sta:
#     if len(word) > len(long_word):
#         long_word = word
# print(long_word) 
#Write a Python program to check if two strings are anagrams.
# str1 = "abcd"
# str2 = "dafc"
# if len(str1) != len(str2):
#     print("False")
# dic1 = {}
# dic2 = {}
# for i in str1:
#     dic1[i] = dic1.get(i,0)+1
# for j in str2:
#     dic2[j] = dic2.get(j,0)+1
# if dic1 == dic2:
#     print("True")
# else:
#     print("False")
#Write a Python program to count the number of occurrences of a specific substring in a string.
# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# # sub_str = "sample"
# total = 0
# start_index = 0
# while start_index < len(main_str):
#     ind = main_str.find(sub_str,start_index)
#     if ind == -1:
#         break
#     total = total +1
#     start_index = ind +1
# print(total)

# Write a Python program to find the index of the first occurrence of a substring in a string.

# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# sub_str = "sample"
# indx_of_str = main_str.find(sub_str)
# print(indx_of_str)

# Write a Python program to replace all occurrences of a substring with another substring.
# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# sub_str = "sample"
# new_str = main_str.replace(sub_str,"Ram")
# print(new_str)
# Write a Python program to find the length of the last word in a sentence.
# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# last_word = main_str.split()[-1]
# # print(last_word)
# print(len(last_word))
# last = main_str.split()
# if last:
#     print(len(last[-1]))

# Write a Python program to reverse the order of words in a sentence.
# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# li = main_str.split()[::-1]
# # print(li)
# print(" ".join(li))

# Write a Python program to find the first non-repeated character in a string.
# str1 = "afbaccdde"
# dic = {}
# for i in str1:
#     dic[i] = dic.get(i,0)+1
# # print(dic)
# for j in str1:
#     if dic[j] == 1:
#         print(j)
#         break
# else:
#     print("No repeted character")
# # Write a Python program to remove all leading and trailing whitespaces from a string.
# main_str = "            This is a sample sentence. This sentence contains           sample words, and it is just a sample."
# new_str = main_str.strip()
# print(new_str)

# Write a Python program to find the common characters between two strings.
# str1 = "shivani"
# str2 = "ram"
# for i in str1:
#     if i in str2:
#         print(i)

# Write a Python program to find the second most frequent character in a string.
# main_str = "This is a sample sentence. This sentence contains sample words, and it is just a sample."
# new_str = main_str.split()
# # print(new_str)
# # print(new_str)
# dic ={}
# for i in new_str:
#     dic[i] = dic.get(i,0)+1
# # print(dic)
# most_freq = max(dic,key = dic.get)
# # print(most_freq)
# print(dic.pop(most_freq,None))
# sec_most_freq = max(dic,key = dic.get,default=None)
# print(sec_most_freq)

# Write a Python program to check if a string contains only unique characters.
# str1 = "shivani"
# new = set()
# for i in str1:
#     if i in new:
#         print("False")
#         break
#     new.add(i)
# else:
#     print("True")

    
