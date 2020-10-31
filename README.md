# Hard-Copy 💾
Convert your PROS Source Code into a Syntax Highlighted PDF! Great for Printing Hard Copies of your code base for your Engineering Notebook.


## Features
- Intelligent file selection
- Recursive file searching
- Cross Platform: Windows and *nix Support
- Flexible: works with a variety of code bases
- Colored code highlighting
- Project name detection
- Maintains clean project organization
- Endless custom formatting options using the Minted Tex Package
### Practicality
Print your code on standard 8.5" x 11" paper with one simple command!

## Setup
Follow these steps to add this functionality to your project:
- create a `scripts` directory in the root of your PROS project
- add the [prosToMinted.py](https://github.com/Udit8348/Hard-Copy/blob/master/scripts/prosToMinted.py) file to your `scripts` directory (*All the dependencies are installed with python3!*)

### Usage
Open the terminal on your computer and navigate to the project's root directory\
Run `python .\scripts\prosToMinted.py` for Windows:
```
FOUND PROJECT FILE ↓
project.pros | <class 'pathlib.WindowsPath'>
Success! Find your zip at: docs/output.zip
Upload the zip directly to overleaf and let it compile into a PDF!
```
Run `python3 scripts/prosToMinted.py` for *nix:
```
FOUND PROJECT FILE ↓
project.pros | <class 'pathlib.PosixPath'>
Success! Find your zip at: docs/output.zip
Upload the zip directly to overleaf and let it compile into a PDF!
```
As the final line of each output message reads, `output.zip` should be uploaded to [Overleaf](https://www.overleaf.com/) where it can easily be compiled into a pdf. (*You will have to create a free account first, if you do not already have one!*) Once you have an account you can choose `New Project > Upload Project` and choose the `output.zip` file that was just created. If you would like to view a preview before downloading it as a pdf, you can press the left facing arrow at the very right of the screen to open the preview window. When you see the green recompile button at the top you can press it to see the updated pdf.  

<details>
           <summary>output.zip</summary>
           <p>The script builds a temporary folder and adds all the relevant <code>.tex</code>, <code>*.c*</code> and <code>*.h*</code> files. Once all the file are added, the folder is zipped in the docs directory and the temp folder is deleted. The <code>*.c*</code> and <code>*.h*</code> just embedded as paths in the <code>.tex</code> files. When overleaf compiles the <code>.tex</code> files the actual formatting is done. Since you have access to all the files in the zip you can make any modifications or adjustments in Overleaf to meet your formatting requirements. If you want to make permanent changes to how the <code>.tex</code> files are built, you can edit the python script to reflect those changes. </p>
</details>

### Why are some files missing?
The script is designed to work with a wide variety of projects. However it is unrealistic to design it so that it works with *any* project structure. For that reason, it assumes your project follows two basic practices:
1) keeping all your header (.h*) files in `include/`
2) keeping all your source (.c*) files in `src/`

Subdirectories within either of those folders will work as expected. For example, `include/my_lib/drive.h` or `src/my_lib/drive.cpp` will be found and formatted.

## Results
Here is the PDF generated from an example PROS project\
![page1](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg1.jpeg)
![page2](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg2.jpeg)
![page3](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg3.jpeg)
![page4](https://github.com/Udit8348/Hard-Copy/blob/master/docs/assets/pg4.jpeg)

### Compatibility
Tested and working on: `Python 3.8.6 on macOS 10.15.7` & `Python 3.7.0 on Windows 10`
### Future Plans
- [ ] Introduce VEXCode Pro V5 Support
- [ ] Display Git Information
- [ ] Customize Margins to Fit in Notebooks
- [ ] Specify Sections Snippets to Format

### Learn More Resources
- [What is LaTex?](https://www.latex-project.org/about/)
- [What is Overleaf?](https://www.overleaf.com/learn/latex/Free_online_introduction_to_LaTeX_(part_1))
- [The Minted Tex Package](https://github.com/Udit8348/Hard-Copy/blob/master/docs/minted.pdf) 

### Objectives
- Promote project organization by using specific folders
- Promote abstraction by automating as much as possible
- Provide accessibility for novices but allow growth for experts

### Contribution
Are you having issues getting setup? Do you have a suggestion for an improvement? Would you like to add a feature? You can message me on the vexforum at: [`_Colossus`](https://www.vexforum.com/u/_colossus/) or on discord at: `Udit#4398`


### As Seen On
Official PSU VEX-U Source Code\
[Vex Forum](https://www.vexforum.com/t/release-hard-copy/85793)
### License
Pending ⏳
