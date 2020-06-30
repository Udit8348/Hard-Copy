# Hard-Copy 💾
Convert your PROS Source Code into a Syntax Highlighted PDF! Great for Printing Hard Copies of your Project for your Engineering Notebook.


## Features
- Convert the relevant header and source code from your PROS project into a syntax highlighted PDF
- Command Line Access
## Practicality
- Print your code!
## Installation Guide
*Draft*
**Note these are just ripped comments being used as boiler plate**
- !/usr/bin/env python3
- Directions:
- Add this file to the main directory of the project
- Open terminal to the directoy containing this script
- use the following cmd to create the .tex file
- python3 prosToMinted.py (@param: "name of a directory where main.tex will be created")
- open this directory from finder and open main.tex (Requires LaTex and another package)
- use typeset to generate the tex file
- print and change target to save as PDF
- Done!

The first recursive is false and the second is true?? Try a different directory if the one you choose doesn't work
ignore the errno 17 in the terminal

- import shutil #this just means that we need to say shutil before all the modules
- instead we can just import the two needed modules relative to shutil
- this means that we do not need to prefix it with shutil.*
- the interpreter will actually not let you use the prefix anyway

- the default breakpoints are set to anywhere so everything is preserved
- if there is a specific case that needs to be formatted differently
- you can manually set the break point in the tex file
- reference the minted user guide pdf

- delete tex folder once we have a zip copy of it

- make rule for converting the relevant source code to a tex file
- recipie runs a python file with a dedicated directory for all of the tex components
- expected behavior: create tex.zip in ./docs
- tex.zip should be uploaded to overleaf where it can easily be compiled into a pdf
*Draft*


# Contribute
Read Below and see how you can help contribute! Remember this is an open source project and I appreciate any feedback or help.
## Compatibility
Tested and working on PROS Kernel 3.2.1 and Okapi Lib 4.0.3 using python 3.7.7 on macOS 10.15.5
## Future Plans
- [ ] Introduce VEXCode Pro V5 Support
- [ ] Open Functionality Beyond VEX Projects
- [ ] Display Git Information
- [ ] Customize Margins to Fit in Notebooks
- [ ] Specify Sections Snippets to Format
## Motivation
At first thought, printing code may seem unnecessary when you can readily view it on nearly all of todays devices. I couldn't give you a better answer than when I was struggling to learn the PID feedback loop. No matter who explained it to me, it made no sense. It was only until I printed a PID library and annotated it by hand, that it clicked in my head. More frequently, I find myself rushing to print my team's latest complete source code for our notebook. I have tried at many word processing tools and add-ons before, but nothing offers a fully customizable way to print code while maintaining formatting and organization. I was really interested in taking on this project when I saw a BLRS' TP code release. Out of the box, I had some issues getting it to work, but eventually with some modifications, I got it working. I was also interested in the controller mapping project done by * Understanding how it worked made me think about how I could implement my own make file recipe in a pros project. It reminded me of the latex project I had been working on early, so I decided to merge both ideas and came up with this. I am aware that there are tools like Doxygen that can format your code like professional documentation, yet the issue still becomes converting it to a printer format. Notepad++ is one of the few common text editors that actually let you print your code, however I am not aware of a straightforward way to group format and print an entire project. In an attempt to create a VRC/VEXU competitor friendly tool, I elected to take inspiration from the aforementioned projects and create Hard-Copy.

## Learn More Resources
- https://www.gnu.org/software/make/manual/html_node/Introduction.html
- https://www.overleaf.com/learn/latex/Free_online_introduction_to_LaTeX_(part_1)

### Objectives
- promote project organization by using specific folders
- promote simplicity by automating as much as possible
- provide accessibility for novices but allow growth for experts

### As Seen On
Official PSU VEX-U Source Code\
Vex Forum
### License
Pending ⏳
