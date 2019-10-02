Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Creating a List 
List = [] 
print("Intial blank List: ") 
print(List) 
  
# Addition of Elements  
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 
  
# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
