

m4_include(../../../setup.m4)


# Git

Basics - git is a way to keep a set of files and all the changes to those files.
It lets you get back to any previous set of changes.
You can control who changes the files and share files between people.

## You can create your own local repository.

```
$ git init
```

Then edit a file called test.txt

Find out what is not in the repository.

```
$ git status
```

Add the file to it.  Create the file test.txt


```
$ git add test.txt
$ git status
$ git commit -m "A Test of Git"
```

## You can get copies of other poles repositories

For this class:

```
$ mkdir class1010
$ cd class1010
$ git clone git@github.com:Univ-Wyo-Education/F21-1010.git
$ cd F21-1010
```

## You can create remote repositories and share files

1. Create a repository on github.com
2. It will give you instructions on how to "clone" it locally
3. Add a file
4. Commit the file
5. Push your local copy to github.com
```
$ git push
```

## You can get changes 


```
$ git pull
```

## An article for beginners with Git

[https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

