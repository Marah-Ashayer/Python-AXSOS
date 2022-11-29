# # Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # 1- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # 2- Change the last_name of the first student from 'Jordan' to 'Bryant'
# # 3- In the sports_directory, change 'Messi' to 'Andres'
# # 4- Change the value 20 in z to 30

x[1][0]=15
print (x)

students[0]['last_name']='Bryant'
print (students)

sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

z[0]['y']=30
print(z)


#-----------------------------------------------------------------------

# Iterate Through a List of Dictionarie

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(0,len(students),1):
        print(students[i])
iterateDictionary(students)

#----------------------------------------------------------------------------

# Get Values From a List of Dictionaries

def iterateDictionary2(key_name, list):
    for i in range(0,len(list),1):
        print(list[i][key_name])
iterateDictionary2('first_name', students)

#-------------------------------------------------------------------------

#Iterate Through a Dictionary with List Values

def  printInfo(some_dict):
    for key , value in some_dict.items():
        print(len(value),key)
        for item in value:
            print(item)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

