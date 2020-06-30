################################################################################
######################### User configurable parameters #########################

# This whole group of code is called a rule
# Include builddocs phony target with any pre-requisites (file that is used to create the target)
# then specify recipie which should be indented by a tab (or a specified RECIPIEPREFIX)
SCRPTDIR=./scripts
DOCSDIR = ./docs
builddocs: include/psu/constants.h
	python3 $(SCRPTDIR)/generic_parse_key_bindings.py

# make rule for converting the relevant source code to a tex file
# recipie runs a python file with a dedicated directory for all of the tex components
# expected behavior: create tex.zip in ./docs
# tex.zip should be uploaded to overleaf where it can easily be compiled into a pdf
convsrc: $(SCRPTDIR)/prosToMinted.py
	python3 $(SCRPTDIR)/prosToMinted.py $(DOCSDIR)/Tex
# filename extensions
CEXTS:=c
ASMEXTS:=s S
CXXEXTS:=cpp c++ cc

# probably shouldn't modify these, but you may need them below
ROOT=.
FWDIR:=$(ROOT)/firmware
BINDIR=$(ROOT)/bin
SRCDIR=$(ROOT)/src
INCDIR=$(ROOT)/include

WARNFLAGS+=
EXTRA_CFLAGS=
EXTRA_CXXFLAGS=

# Set to 1 to enable hot/cold linking
USE_PACKAGE:=1

# Add libraries you do not wish to include in the cold image here
# EXCLUDE_COLD_LIBRARIES:= $(FWDIR)/your_library.a
EXCLUDE_COLD_LIBRARIES:=

# Set this to 1 to add additional rules to compile your project as a PROS library template
IS_LIBRARY:=0
# TODO: CHANGE THIS!
LIBNAME:=libbest
VERSION:=1.0.0
# EXCLUDE_SRC_FROM_LIB= $(SRCDIR)/unpublishedfile.c
# this line excludes opcontrol.c and similar files
EXCLUDE_SRC_FROM_LIB+=$(foreach file, $(SRCDIR)/main,$(foreach cext,$(CEXTS),$(file).$(cext)) $(foreach cxxext,$(CXXEXTS),$(file).$(cxxext)))

# files that get distributed to every user (beyond your source archive) - add
# whatever files you want here. This line is configured to add all header files
# that are in the the include directory get exported
TEMPLATE_FILES=$(INCDIR)/**/*.h $(INCDIR)/**/*.hpp

.DEFAULT_GOAL=quick

################################################################################
################################################################################
########## Nothing below this line should be edited by typical users ###########
-include ./common.mk
