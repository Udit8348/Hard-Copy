#!/usr/bin/env python3
# Directions:
# Add this file to the main directory of the project
# Open terminal to the directoy containing this script
# use the following cmd to create the .tex file
# python3 prosToMinted.py (@param: "name of a directory where main.tex will be created")
# open this directory from finder and open main.tex (Requires LaTex and another package)
# use typeset to generate the tex file
# print and change target to save as PDF
# Done!

#The first recursive is false and the second is true?? Try a different directory if the one you choose doesn't work
#ignore the errno 17 in the terminal
import os
import sys
import glob
import zipfile
from shutil import copy, rmtree
#import shutil #this just means that we need to say shutil before all the modules
# instead we can just import the two needed modules relative to shutil
# this means that we do not need to prefix it with shutil.*
# the interpreter will actually not let you use the prefix anyway

# function that zips a selected directory
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        print("root is ", root)
        print("dirs is ", dirs)
        print("files is ", files)
        for file in files:
            ziph.write(os.path.join(root, file))

def main(dest):
    try:
        os.mkdir(dest)
    except OSError as e:
        print(e)
    try:
        os.mkdir(dest)
    except OSError as e:
        print(e)
    with open("codeToLaTeX.tex", "w+") as f:
        f.write("%%-----------------------------------------\n")
        f.write("\\section{Header Files}\n\n")
        for header in glob.glob('**/*.h*', recursive=True):
            if "api.h" in header or "/display/" in header or "/Eigen/" in header or "/okapi/" in header or "/pros/" in header:
                continue
            f.write("\\subsection{" + header + "}\n")
            # the default breakpoints are set to anywhere so everything is preserved
            # if there is a specific case that needs to be formatted differently
            # you can manually set the break point in the tex file
            # reference the minted user guide pdf
            f.write("\\inputminted[linenos,tabsize=2,breaklines, breakanywhere]{c}{" + header + "}\n")
            f.write("\\pagebreak\n\n")
            head, tail = os.path.split(header)
            print("This is the head: ", head)
            path = dest + "/" + head
            try:
                os.mkdir(path)
                print(path)
            except OSError as e:
                print(e)
            copy(header, path)

        f.write("%%-----------------------------------------\n")
        f.write("\\section{Source Files}\n\n")

        for source in glob.glob('**/*.c*', recursive=True):
            if ".o" in source or ".csv" in source:
                continue
            f.write("\\subsection{" + source + "}\n")
            f.write("\\inputminted[linenos,tabsize=2,breaklines, breakanywhere]{c}{" + source + "}\n")
            f.write("\\pagebreak\n\n")
            head, tail = os.path.split(source)
            print("This is head: ", head)
            path = dest + "/" + head
            print("This is path: ", path)
            try:
                os.mkdir(path)
            except OSError as e:
                print(e)
            copy(source, path)

    copy("codeToLaTeX.tex", dest)
    os.remove("codeToLaTeX.tex")
    with open("main.tex", "w+") as f:
        print("Reached Conversion")
        f.write("\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\title{PSU Unified Source Code}\n\\author{subramanyau}\n\\date{June 2020}\n\\usepackage{minted}\n\\begin{document}\n\\input{codeToLaTeX.tex}\n\n\\end{document}")
    copy("main.tex", dest)
    os.remove("main.tex")

    # zip the tex folder so it can be uploaded to overleaf
    zipf = zipfile.ZipFile("docs/Tex.zip", 'w', zipfile.ZIP_DEFLATED)
    zipdir(dest, zipf)
    zipf.close()

    # delete tex folder once we have a zip copy of it
    # https://linuxize.com/post/python-delete-files-and-directories/#:~:text=strerror))-,Deleting%20Directories%20(Folders),an%20empty%20directory%20and%20shutil.
    try:
        rmtree(dest) #removes folder and all contained items
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))

if __name__ == "__main__":
    main(sys.argv[1])
