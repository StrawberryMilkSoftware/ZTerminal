# ZTerminal can be confusing at times, so here is a guide.


### How to use files with the ZTerminal Shell Script/ZTSS language:
Find the `zthandler.py` file and drag your file over it. If it has no errors, the file will run.


## print
prints to the console.
Syntax
print-<text>

## ver
prints the version of zterminal.
syntax
ver
version

## wv 
opens winver to show your windows version
syntax
wv

## ndir 
makes a new folder/directory
syntax
ndir-<name>

## tofile
puts content into a file
syntax
tofile-<path>\<filename>-<content>

## time
tells time
syntax
time

## oscmd 
run commands using your operating systems default terminal (WCP, bash, etc.)
syntax
oscmd-<cmd> <arg>(if cmd needs it)

## clear 
clears the screen
syntax
clear

## pause 
pauses until a key is pressed
syntax
pause

## exit 
closes ZTerminal
syntax
exit


## ping
pings an ip address or website
syntax
ping-<ip/url>


## title
changes the window title
syntax
title-<text>

## call 
calls a .zt file
syntax
call-<file>

## delf 
deletes a file
syntax
delf-<path>\<file>

## deldir 
deletes a directory
syntax
deldir-<path>

## start 
starts a program
syntax
start-<program>

## choco 
edits with ChocoEdit
syntax
choco-<path>\<file>

## dir 
lists contents of a dir
syntax
dir-<path>

## tree 
lists contents of a dir with a graphic
syntax
tree-<path>

## cd
change current directory
syntax
cd-<path>

## printcd
print the current directory
syntax
printcd
