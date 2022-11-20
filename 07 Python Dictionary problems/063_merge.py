#063.	Python Program to Merge two Dictionaries
def merge_twoDict(a, b): 
    return (a.update(b)) 
a = {'USA' : 'New York',  
      'Germany' : 'Jakarta',  
      'England' : 'London' }  
b = {  
    'India' : 'Delhi',  
    'Russia' : 'Russian',  
    'Australia' : 'Sydney'  
}            
merge_twoDict(a, b) 
print("Merged Dictionaries is : ")  
print(a) 