import argparse
import os


path = os.getcwd()
storeInFile = False
filepath = "structure.txt"
f = ""

def out(str):
	global storeInFile
	if storeInFile:
		f.write(str+"\n")
	else:
		print(str)




def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        out('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            out('{}{}'.format(subindent, f))


parser = argparse.ArgumentParser()
parser.add_argument('--path', help='Path of the folder (Default current folder)', type=str,required=False)
parser.add_argument('--o', help='Output file to store the result', type=str,required=False)

args = parser.parse_args()

if args.path:
	path = args.path

if args.o:
	storeInFile = True
	f = open(args.o,'w')


list_files(path)

if f:
	f.close()
