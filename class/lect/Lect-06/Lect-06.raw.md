
m4_include(../../../setup.m4)

# Lecture 6 - Lists / Dictionaries 

## First let's read in a file

```
m4_include(readNameList.py.nu)
```

<div class="pagebreak"></div>

## Let's remove the punctuation

```
m4_include(removePunctuation.py.nu)
```

<div class="pagebreak"></div>

## List Example

```
m4_include(search-list.py.nu)
```


## Dictionary

A dictionary is an association between a "key" value and a set of data
that is efficient for looking thins up by the key.

let's do an "age" one...

```
>>> dd = {}
>>> dd["bob"] = 22
>>> dd["jane"] = 31
>>> dd["marry"] = 18
>>>
>>> dd["bob"]
>>> dd["jane"]
```

Now changing our phone search to use a  dictionary:

```
m4_include(search-dict.py.nu)
```



### Requirements

Prompt for a file name. 
Then read in a file of text.  
Split the file up into words.
Remove any punctuation and convert each word to lower case.
Count how many times each word occurs. 
Print out a sorted list of the words in the file with the number of occurrences of each word.  Sort from the most frequent word to the least.

### Requirements Broken Down

1. Prompt for a file name. 
2. Read in a file of text.  
3. Split the file up into words.
4. Remove any punctuation and convert each word to lower case.
5. Count how many times each word occurs. 
6. Print out a sorted list
	- Print out a sorted list of the words in the file with the number of occurrences of each word. 
	- Sort from the most frequent word to the least.


### Let's count some words

```
m4_include(word-freq.py.nu)
```
















# Copyright

Copyright (C) University of Wyoming, 2021.

