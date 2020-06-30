import os
import sys
import glob
import zipfile
from shutil import copy, rmtree

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


    try:
        rmtree(dest) #removes folder and all contained items
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))

if __name__ == "__main__":
    main(sys.argv[1])
