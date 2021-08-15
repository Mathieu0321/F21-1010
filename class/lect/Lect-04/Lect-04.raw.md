
m4_include(../../../setup.m4)

# Lecture 4 - Lists, Files, Modules, Input Output.

Lists.  Chapter 3 in the book.

Life would be very boring if all we could do was to work on one thin at once.  That would be
like what you are stuck in in most GUI applications - one document, one image.  There are very
good tools for each of these.   For example Adobe Photoshop - part of the creative suite -
is fantastic and working on 1 image at once.  I use it.

A couple of years ago a business hear in town was adding water marks to images.  They had an
intern, being payed $15 an hour, open an image, drag the watermark onto the image in the bottom
right, save the image.   They had 2,500,000 images to process.  At my best estimate this person
would finish this task in 3.4 years working full time.  Long before that time his break would
turn to goo and he would get mouse shoulder and fall off of his chair in total abject boredom.

I used a 20 line Python program to open the image file, open the water mark file, position it,
paint the watermark onto the image, save the file.    It started out with a list of files,
2.5 million of them, and in about 35 minutes it has a perfectly positioned watermark on every one.

One of the super-powers of computers is to work at scale.  Amazon's authentication service
performs 400,000,000 requests a second.  That is scale.

A list in python.

```
m4_include(cars.py)
```

An important note about upper/lower case characters.

```
m4_include(cars2.py)
```

## What are lists - syntax for them.

Use square for lists, round for tuples.

```
m4_include(a-list.py)
```

## Accessing the elements in a list.

```
m4_include(list-mod.py)
```

The value inside the `list1[0]` - in the square brackets is often referred to as the subscript.

## List Comprehensions

```
m4_include(list-comp.py)
```

## Let's build a list program.

1. Let's create a directory for the program to be in.
2. An input file to read from.
3. The code -- open the file, read the file, return the list.
4. Let's test this chunk.
5. Let's print out all the even numbers in the list.

```
$ mkdir ex1
$ cd ex1
```

```
$ vi data1.txt
```

## Let's build a string - list processor.

Strings are list.

1. Switch directories.
1. Let's create a directory for the program to be in.
2. An input file to read from.
3. The code -- open the file, read the file, return the list of strings.
4. Let's test this chunk.
5. Let's count the characters on each line.

## Let's build a matrix add.

You can have lists inside lists.

1. Switch directories.
1. Let's create a directory for the program to be in.
3. Read in a matrix.
3. Read in a 2nd matrix (same code)
3. See if an appropriate size.
4. A function to add matrices.
4. Output a matrix.



# Copyright

Copyright (C) University of Wyoming, 2021.


