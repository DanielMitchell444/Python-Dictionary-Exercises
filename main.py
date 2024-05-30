'''
The next thing we will be learning about is dictionaries
The definition of a dictionary is that they are used to store data
values in key:value pairs
dictionaries are ordered, changable, but do not allow duplicates
Dictionaries, unlike lists, are written with curly brackets
that represet key value pairs
the syntax is as follows
'''
dictionary = {
 "Name": "Daniel",
 "Age": "26",
 "Gender": "Male",
 "Occupation": "Teacher"
}

'''
And if you print it, you will notice that they come out as key-value
pairs.
Typically, dictionaries are used to make the order of items more appealing. But
you can do other cool things with dictionaries as well
'''

'''
PRACTICE:
Below this comment, make a dictionary with whatever keys and values you want
'''

'''
Remember, dictionaries are ordered, changable, and do not allow duplicates
dictionaries can be referred to by its key name, for example, if we wanted
to get the key name gender we could do that like so
'''

print(dictionary["Gender"])

'''
And this would print out the gender, which would be male.
Dictionaries can also use any value type as well
also remember that dictionaries are objects.
The definition of an object is that they are variables
that contain data and functions that can be used to manipulate data. Objects
can be of any variable type(IE BOOLEAN, INT, STRING).
'''

'''
PRACTICE:
Below this comment, i want you to select and print one of the keys
using the syntax above.
'''

'''
The Keys method
The keys method is used to return a list of all keys
in a dictionary. The syntax is as follows
'''

x = dictionary.keys()

'''
This essentially gets all the keys AKA Name, age, gender, Occupation.
You can also change values inside the dictionary by
using the following syntax
'''

dictionary["Age"] = "27"


'''
This would change the age value in the dictionary from 26 to 27.
'''

'''
PRACTICE:
Using the syntax above, change a value of one part of your dictionary.
'''

'''
We know that they are called key value pairs. You might be asking yourself,
is there a way to return a list of all the values in a dictionary?
Well, this is where the values method comes in
The values method essentially retusn a list of all values in a dictionary
The syntax is as follows
'''

y = dictionary.values()

'''
And this would return Daniel, 26, male, and teacher
'''

'''
PRACTICE:
Using the values method, i want you to get the values of the dictionary, 
then i want you to print out the values.
'''


'''
THE UPDATE METHOD
the update method is used to update the dictionary with new items, you can change
both the key and the value pairs inside the update argument. The syntax
is as follows
'''

dictionary.update({"age": "27"})

'''
PRACTICE:
Below this comment, i want you to update a key and value inside your dictionary.
'''


'''
REMOVING ITEMS FROM A DICTIONARY.
similar to lists, dictionaries have some similar methods. One of those similar
methods is the pop method.
The pop method removes the items with the specified key name. The pop method
removes both the key and the value pair compleyely from the dictionary
Lets say we want to remove the name key value pair, we could do this
like so
'''

dictionary.pop("name")

'''
And this would essentially remove both the key and the value inside the 
dictionary
'''

'''
PRACTICE:
Below this comment, i want you to remove a key and value pair using the 
syntax above.
'''

'''
THE POP ITEM METHOD
the popitem method removes the last inserted item in a dictionary. In this
instance, if we used the popitem method, it would remove occupation.
The syntax is as follows
'''

dictionary.popitem()

'''
PRACTICE:
Using the syntax above, i want you to remove the last item inside your dictionary
please post this code below this comment.
'''

'''
The clear method

Similar to lists, you can also used the clear method. This method 
empties a dictionary.
The syntax is as follows
'''

dictionary.clear()


'''
LOOPING THROUGH A DICTIONARY
similar to lists, we can also loop through a dictionary using a for loop.
When looping through a dictionary, initially, you will initially get the keys
but there are ways to return the value. Which is something we will learn later
the syntax is similar to using for loops in lists, like so
'''

for x in dictionary:
    print(x)

'''
Remember that x is a completely made up term that stores the keys.
'''

'''
PRACTICE:
Below this comment, i want you to make a loop that prints all the
key names in your dictionary using the syntax above.
'''

'''
We talked previously that you can also access the values inside a dictionary,
to do this, we would have to print out the values one by one
the syntax is as follows
'''

for y in dictionary:
    print(dictionary[y])


'''
PRACTICE:
Below this comment, i want you to loop through your dictionary and then
print out only the values of your dictionary.
'''

'''
To get only the keys or only the values of a dictionary, we can use
syntax that we learned earlier in order to do so. In order for you
to select the keys from a dictionary, we would have to do something like
so
'''

for z in dictionary.keys():
    print(z)


'''
The syntax is similar with values, it is like so
'''

for p in dictionary.values():
    print(p)


'''
COPYING A DICTIONARY:
In python, you simply can not copy a dictionary by setting one
dictionary equal to another. That is where the copy method
comes in
The copy method makes a copy of a dictionary.
The syntax is as follows
'''

dictionary2 = dictionary.copy()

'''
And if you print this out, you will notice that this made a copy of
the other dictionary.
'''

'''
PRACTICE:
Below this comment, i wnat you to copy your existing dictionary into
a new variable.
'''


'''
NESTED DICTIONARIES:
A dictionry can contain other dictionaries with different values.
The syntax is like so.
'''

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

'''
PRACTICE:
Below this comment, i want you to create a nested dictionary
similar to the one above. You can choose what the key and value
pairs are, please post the code below this comment.
'''

'''
ACCESSING ITEMS IN A NESTED DICTIONARY:
in order to access an item in a nested dictionary, we would have to 
first use the name of the dictionary, followed by the key you want to select
inside the dictionary.
For example, inside the newly created dictionary, lets say we want select
the 2nd dictionary, and inside the 2nd dictionary, child2, we want to select
the name key. We could do this like so.
'''

print(myfamily["child2"]["name"])

'''
This would print out the value tobias
When you do this, remember that you are accessing the value inside the key.

'''

'''
PRACTICE: 
Below this comment, i want you to select one of your dictionaries, followed
by the key that you want to select. HINT: Its similar to the syntax above.
'''



'''
With nested dictionaries, you can also loop through nested dictionaries. I 
will show you the syntax first, and then explain each part.
The syntax is as follows
'''
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])


'''
Before you get confused, let me explain the code step by step
So first, the x and the obj are items that you can name whatever you want,
but i would recommend you name them something that makes sense to you.
The x in this instance are the names of each dictionary. In this instance,
the values in x would be
child1
child2
child3

Secondly, the value obj stores all the keys and values inside each
dictionary. For example, if we went print(obj) it would print

{'name': 'Emil', 'year': 2004}
{'name': 'Tobias', 'year': 2007}
{'name': 'Linus', 'year': 2011}

The next part is a bit confusing because we have not learned about
tuples, but the next part of it is
myFamily.items()
We are essentially just looping through keys and values of a nested
dictionary. That is what myFamily.items() does.

Next, we print out x, x is essentially just the names of each
nested dictionary. So in this instance, it would be
child1
child2
child3
'''

'''
The next part, in short terms, we are essentially just printing out
each key value pair in a specific order that we choose. In this instance,
here is the output of all this code.
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011

So, the first loop essentially just prints out child1, child2, and child3

After that, the next loop happens.

In this instance, the y can be anything you want it to be, y is the key
so for example, the keys are name and year.
After that, we do something like obj[y]
obj[y] is essentially just the values associated with the keys.
'''



