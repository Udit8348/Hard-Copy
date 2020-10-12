# Hard-Copy 💾
Convert your PROS Source Code into a Syntax Highlighted PDF! Great for Printing Hard Copies of your Project for your Engineering Notebook.


## Features
- Convert the relevant header and source code from your PROS project into a syntax highlighted PDF
- Command Line Access
- Will work with nested folders
- Flexibility to work with a variety of code bases
## Practicality
- Print your code!

## Setup
Follow these steps to add this functionality to your project:
- create a `scripts` directory in root of the project directory
- copy the scripts/prosToMinted.py file into your `scripts` directory (all the dependencies should already be installed with python3)
- modify `Makefile` to add the following code:
```
# Make File Rule for Converting Code to Tex
SCRPTDIR=./scripts
DOCSDIR = ./docs
conv2tex: $(SCRPTDIR)/prosToMinted.py
	python3 $(SCRPTDIR)/prosToMinted.py $(DOCSDIR)/Tex
```

## Usage
- Run `prosv5 make conv2tex`
- navigate to docs/Tex.zip
- tex.zip should be uploaded to overleaf where it can easily be compiled into a pdf

## Project Output
![page1](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg1.jpeg)
![page2](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg2.jpeg)
![page3](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg3.jpeg)
![page4](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg4.jpeg)

## Compatibility
Tested and working on PROS Kernel 3.2.1 and Okapi Lib 4.0.3 using python 3.7.7 on macOS 10.15.5
## Future Plans
- [ ] Introduce VEXCode Pro V5 Support
- [ ] Open Functionality Beyond VEX Projects
- [ ] Display Git Information
- [ ] Customize Margins to Fit in Notebooks
- [ ] Specify Sections Snippets to Format

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
