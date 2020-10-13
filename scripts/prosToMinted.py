import os
import sys
import glob
import zipfile
from shutil import copy, rmtree

# Function which zips the given 'path' to the 'ziph'
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def main(dest):
    try:
        os.mkdir(dest)
    except OSError as e:
        print(e)

    # Create a 'Code.tex' LaTeX file
    # This is responsible for reading a copy of the valid files
    # then, formatting their contents
    with open("code.tex", "w+") as f:
        # Recursively search the entire project for any Header Files
        f.write("%%-----------------------------------------\n")
        f.write("\\section{Header Files}\n\n")
        for header in glob.glob('**/*.h*', recursive=True):
            # Exclude PROS API headers
            if ("api.h" in header) or ("/display/" in header) or ("/okapi/" in header) or ("/pros/" in header):
                continue

            # Generate LaTeX code for any valid header
            # Write it to the 'Code' LaTeX file
            f.write("\\subsection{" + header + "}\n")
            f.write("\\inputminted[linenos,tabsize=2,breaklines, breakanywhere]{c}{" + header + "}\n")
            f.write("\\pagebreak\n\n")

            # Copy the file's tree into the destination
            head, tail = os.path.split(header)
            path = dest + "/" + head
            try:
                os.mkdir(path)
                print(path)
            except OSError as e:
                print(e)
            copy(header, path)

        # Recursively search the entire project for any Source Files
        f.write("%%-----------------------------------------\n")
        f.write("\\section{Source Files}\n\n")
        for source in glob.glob('**/*.c*', recursive=True):
            # Exlude any object files or csv files
            if ".o" in source or ".csv" in source:
                continue

            # Generate LaTeX code for any valid source file
            # Write it to the 'Code' LaTeX file
            # See docs/minted.pdf for all the line break options
            f.write("\\subsection{" + source + "}\n")
            f.write("\\inputminted[linenos,tabsize=2,breaklines, breakanywhere]{c}{" + source + "}\n")
            f.write("\\pagebreak\n\n")

            # Copy the file's tree into the destination
            head, tail = os.path.split(source)
            path = dest + "/" + head
            try:
                os.mkdir(path)
            except OSError as e:
                print(e)
            copy(source, path)

    # The 'Code' LaTeX file is completely written now
    # Save a copy of it to the destination and remove the original
    copy("code.tex", dest)
    os.remove("code.tex")

    # Create the 'Main' LaTeX file
    # This is the container for the 'Code' LaTeX file
    # It contains document specific formatting and information
    with open("main.tex", "w+") as f:
        f.write("\\documentclass{article}\n"
                 + "\\usepackage[utf8]{inputenc}\n"
                 + "\\usepackage[margin=1in]{geometry}\n"
                 + "\\title{PROJECT_TITLE}\n"
                 + "\\author{LAST_FIRST}\n"
                 + "\\date{MONTH_YEAR}\n"
                 + "\\usepackage{minted}\n"
                 + "\\begin{document}\n"
                 + "\\input{code.tex}\n\n"
                 + "\\end{document}")

    # The 'Main' LaTeX file is completely written now
    # Save a copy of it to the destination and remove the original
    copy("main.tex", dest)
    os.remove("main.tex")

    # Zip the contents found at the destination
    # A Zip file can be directly uploaded to overleaf
    # @TODO might need to use regex to strip the name from the dest to create the path name for the zip
    zipf = zipfile.ZipFile("docs/Tex.zip", 'w', zipfile.ZIP_DEFLATED)
    zipdir(dest, zipf)
    zipf.close()

    # Recursively delete tex folder once we have a zip copy of it in the destination folder
    # https://linuxize.com/post/python-delete-files-and-directories/#:~:text=strerror
    try:
        rmtree(dest)
    except OSError as e:
        print(e)

    print(">>> Success! Find your zip at:", dest)

if __name__ == "__main__":
    main(sys.argv[1])
