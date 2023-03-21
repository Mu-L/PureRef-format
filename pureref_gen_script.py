import os
import pureref_gen
import sys

####################################################################################################
# Just run this with "python pureref_gen_script.py" in your command line inside the PureRef-format
# folder. It will generate a folder for input (Artists) and output (Purs) for you.
# Then you can put folders with images in the Artists folder and run "python pureref_gen_script.py"
# again to generate the Purs.
####################################################################################################

imagefolder_path = os.getcwd() + "/Artists"

purfolder_path = os.getcwd() + "/Purs"

# if you give the script two arguments, it will use these for the imagefolder and purfolder
if len(sys.argv) > 1:
    imagefolder_path = os.path.abspath(sys.argv[1])
    purfolder_path = os.path.abspath(sys.argv[2])

# This is where you put folders with JPG or PNG images
if not os.path.exists(imagefolder_path):
    os.mkdir(imagefolder_path)

# This is where PureRef files come out
if not os.path.exists(purfolder_path):
    os.mkdir(purfolder_path)

# Turn all folders with images in Artists/ into .pur files in Purs/
# Unless the .pur already exists, so you can edit it
# If you want to regenerate it, you need to delete the .pur file
# only if it is a dir
folders = next(os.walk(imagefolder_path))[1]

# if there are no folders, use the root folder since the images might be there instead
if len(folders) == 0:
    # current directory name
    folders = [os.path.basename(imagefolder_path)]
    # subtract last directory
    imagefolder_path = "/".join(imagefolder_path.split("/")[:-1])

for folder in folders:
    if not os.path.exists(purfolder_path + "/" + folder + ".pur"):
        print("Creating " + folder + ".pur")
        pureref_gen.generate(imagefolder_path + "/" + folder, purfolder_path + "/" + folder + ".pur")
    else:
        print("File already exists, skipping " + folder)

# The file will say it has a "load error", just press "Open Anyway (Unsafe)"
# This is only because the checksum to check for corruption is not generated correctly
# Which is not a problem, I simply don't know how this checksum is generated
# Save the file once and the error will be gone
