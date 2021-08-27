
m4_include(../../setup.m4)

# Lab 01 - Setup a development environment

The first step is to build a development environment.  Most software installations are done on remote servers.
These serves do not have a GUI at all and all of this work is done at the command line.   Some systems, like
IoT systems, are too small to use a GUI - again all the work is done at the command line.

The command line has advantages.  It can be scripted so that you can re-produce your results.  It is also
easier to document.

This is going to be broken up based on the operating system you are working with.

## Windows

On Windows the command line is the Power Shell.   There are 2 different security levels that the power
shell can run under.  The first is as your login user.  The 2nd is as an administrative user.

There is an older command line, command.com, but it will not work for most of this.

It is important that you configure your system for development.

1. Setup so that PowerShell can run .ps scripts.

![powershell installation](./powershell-0.jpg)

![powershell installation](./powershell-1.jpg)

![powershell installation](./powershell-2.jpg)

2. Configure your desktop explore shows all files and shows file extensions.  The file extension
is the last few characters after the last dot (.) in a file name.   In windows 10 there is a
configuration superficially for development that will set this and a few other settings to make
your life easier.

Open file explorer and click on view on the top of the explorer and the click on view and then select details:

![Folder setup](./folder-setup.jpg)

In the same folder click on view and then go to options and then click on change folders and search options:

![Folder setup](./folder-setup-2.jpg)

Then click on Apply to folders:

![Folder setup](./folder-setup-3.jpg)

Then click yes:

![Folder setup](./folder-setup-4.jpg)


3. For a lot of stuff we will use the Linux/Unix 'bash' shell - this will be installed as a
part of our 'git' install a little bit later.  'bash' is the same shell that is used on
many Mac and most Linux systems.

###  Install Google Chrome

A number of tools depend on the Google Chrome portability library.  

1. Install Chrome (if you have not already done it) [https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGSgDDdrI4XOUKv4CPwFQfs7M2HaXiRJ-MMeszA20rC72r-9U13-8jBoCQV4QAvD_BwE&gclsrc=aw.ds](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGSgDDdrI4XOUKv4CPwFQfs7M2HaXiRJ-MMeszA20rC72r-9U13-8jBoCQV4QAvD_BwE&gclsrc=aw.ds)

![Chrome installation](./chrome-installtion.jpg)

![Chrome installation](./chrome-installtion-1.jpg)

![Chrome installation](./chrome-installtion-2.jpg)

![Chrome installation](./chrome-installtion-4.jpg)

![Chrome installation](./chrome-installtion-5.jpg)

![Chrome installation](./chrome-installtion-6.jpg)


### Source code control

1. We will be using 'https://github.com' for class handouts and for turning working with files
through the semester.  The underlying system that github uses is 'git'.    You will need to
to to 'https://github.com' and create a free account on the site.
2. Bring up this page in the "chrome" browser with [.)
3. Determine what version of windows you have, the 32 bit or 64 bit version.  [https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808) has an explanation.
4.  You will also need the windows 'git' tools installed.  [https://git-scm.com/download/win](https://git-scm.com/download/win)
in chrome will start the download as soon as you go to the page.  Run the installer.  You should end up with a MinGW Bash
shell icon on your desktop.

After downloading the git tools setup file, double click on it:

![git installation](./git-tools.jpg)

![git installation](./git-tools-1.jpg)

![git installation](./git-tools-2.jpg)

![git installation](./git-tools-3.jpg)

![git installation](./git-tools-4.jpg)

![git installation](./git-tools-5.jpg)

![git installation](./git-tools-6.jpg)

![git installation](./git-tools-7.jpg)

![git installation](./git-tools-8.jpg)

5. Install VS Code [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

Download vs code and double click on the setup file:

![vscode installation](./vscode-1.png)

![vscode installation](./vscode-2.png)

![vscode installation](./vscode-3.png)

![vscode installation](./vscode-4.png)

![vscode installation](./vscode-5.png)

![vscode installation](./vscode-6.png)

![vscode installation](./vscode-7.png)

![vscode installation](./vscode-8.png)

7. Install Anaconda Python  [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

![anaconda installation](./anaconda-1.png)

![anaconda installation](./anaconda-2.png)

![anaconda installation](./anaconda-3.png)

![anaconda installation](./anaconda-4.png)

![anaconda installation](./anaconda-5.png)

![anaconda installation](./anaconda-6.png)

![anaconda installation](./anaconda-7.png)

![anaconda installation](./anaconda-8.png)

![anaconda installation](./anaconda-9.png)

![anaconda installation](./anaconda-10.png)

![anaconda installation](./anaconda-11.png)

9. Install "vim", [https://www.vim.org/download.php#pc](https://www.vim.org/download.php#pc)
A good guide to vim on windows [https://www.freecodecamp.org/news/vim-windows-install-powershell/](https://www.freecodecamp.org/news/vim-windows-install-powershell/)
An interactive tutorial on using vim [https://www.openvim.com/](https://www.openvim.com/)

![vim installation](./vim-1.png)

![vim installation](./vim-2.png)

![vim installation](./vim-3.png)

![vim installation](./vim-4.png)

![vim installation](./vim-5.png)

![vim installation](./vim-6.png)

![vim installation](./vim-7.png)

![vim installation](./vim-8.png)




## Installation on a Mac

We will be using 'https://github.com' for class handouts and for turning working with files
through the semester.  The underlying system that github uses is 'git'.    You will need to
to to 'https://github.com' and create a free account on the site.

1. Install XCode (Apple Store)  On your Apple Mac bring up the Apple Store.  Search for "XCode" - it is free. Install.  Once you install XCode you need to start it
and accept the license terms for XCode.  XCode is free but it requires the "Accept" before it will allow you to run software.   Open the finder in /Applications/Utilities
and click on Terminal.  The enter: `xcode-select —install` to install the command line tools.

![xcode installation](./xcode-1.png)

![xcode installation](./xcode-2.png)

![xcode installation](./xcode-3.png)

![xcode installation](./xcode-4.png)

![xcode installation](./xcode-5.png)

![xcode installation](./xcode-6.png)

![xcode installation](./xcode-7.png)

2. Install brew.  Search for "mac brew".  Cut and paste the line.  Bring up a "terminal" - In the finder brows to your /Applications, then in the Utilities you will find a terminal.  Paste the "brew" install line into that.  Run.

![brew installation](./brew-1.png)

![brew installation](./brew-2.png)

![brew installation](./brew-3.png)

![brew installation](./brew-4.png)

![brew installation](./brew-5.png)

![brew installation](./brew-6.png)

![brew installation](./brew-7.png)
  
4. Now at the command line (in Terminal) do `$ brew install git`. [https://brew.sh/](https://brew.sh/)

![git installation](./git-1.png)

![git installation](./git-2.png)

6. Install "iTerm 2.x" [https://iterm2.com/](https://iterm2.com/)   Since this terminal will be used during the semester please configure it to be in you tool bar.  
7. Install Chrome (if you have not already done it)  (Search for "Download Chrome" - follow googles instructions) [https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGSgDDdrI4XOUKv4CPwFQfs7M2HaXiRJ-MMeszA20rC72r-9U13-8jBoCQV4QAvD_BwE&gclsrc=aw.ds](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGSgDDdrI4XOUKv4CPwFQfs7M2HaXiRJ-MMeszA20rC72r-9U13-8jBoCQV4QAvD_BwE&gclsrc=aw.ds)
8. Bring up this page in the "chrome" browser with [.)   Navigate around in the site - this is where all the lectures, assignments and lab handouts are built.
9. Install VS Code. Search for "Visual Studio Code" Install.  The add the "Python Package to it".  I also installed the "Python Lint" package.  [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
10. Install Anaconda Python.  Search for  "Mac Install Anaconda Python" - install the anaconda package (Takes a while).  [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
11. Install "vim" [https://github.com/macvim-dev/macvim/releases/tag/snapshot-171](https://github.com/macvim-dev/macvim/releases/tag/snapshot-171)





### Linux Installs.

This depends on the kind of Linux Ubuntu, RedHat, CentOs, Arch etc, that you have.  Let's get together and figure out hat detail and work on it one-on-one.



## Correct Version of Python

First check that you have the correct version of Python!   Your system may have an old 
version of python already on it.  All Mac's do.

```
$ python --version
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

You should see "Python 3.8.3" at the top.   If you don't then we need to fix your
path so that when you run python you are getting to the version that we just 
installed.

On a Mac (assuming that you have the latest version of the OS installed)
you need to set the "PATH" in the `~/.zshrc` file and then re-start iTerm2.
If you installed Anaconda python in `/Users/pschlmp/Anaconda3` (note my
username in this - use your own username) then the path will need to be
set to:

```
export PATH="/home/pschlump/anaconda3/bin:$PATH"
```

On Windows the path is set as a global system environment variable in
the System Variables.   
See [https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)




## Install Packages in Python (Both Windows and Mac)


The installation manager for Python is "pip".  There are 2 ways to run "pip".
In the terminal:

On Mac:

```
$  pip --install <package>
```

or:

```
$ python -m pip --install <package>
```

On Windows:


```
C:\>  pip --install <package>
```

or:

```
C:\> python -m pip --install <package>
```

Most of our installs of python packages will use "pip".

The exception is installing TensorFlow.  It requires more steps to install and
we will use the "conda" installer that came with the Anaconda version of Python.


On Mac/Linux:
```
$ conda install -c conda-forge tensorflow 
```

On Windows:

```
C:\> conda install -c conda-forge tensorflow 
```


The set of things to install with pip :

```
pip --install pandas
pip --install numpy
pip --install bottle
pip --install sqlite3
pip --install matplotlib
pip --install bs4 
```

Then

```
$ conda install -c conda-forge tensorflow 
```


## Configure and Demo of Using Debugger

1. Configure VS Code (common) (Note on Windows the path (if you have to enter it) is `C:\anaconda3\python.exe`  Usually VS Code will give you a drop down menu to pick from.
2. Use VS Code debugger (common)




# Simple Hello world Program

Edit a file called `hello-world.py` and put the following in it:

```
import sys
print ( "hello world" )
print ( sys.version )
```

At the command line:

```
$ python hello-world.py
```

Modify the file to be:

```
m4_include(hello-world.py)
```

Run it again.

Use a '#' pound-sign to create a line with your name on it.

```

# Author: Jagadish Bapanapally
# Author: Philip Schlump

m4_include(hello-world.py)
```

Run it again.

If it works the turn this in as a part of your lab.

# Lab Questions

Use the editor and write up an answer to:

1. Your name?   Did you put it in the comments at the top of your code.  That is important if you want to get credit for the assignment!
2. What part of software installation causes the most frustration?

Save the file and upload this as a part of your lab work.




# Copyright

Copyright (C) University of Wyoming, 2021.

