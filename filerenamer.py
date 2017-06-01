import os
import argparse 

def rightStrip(fileName):
	return fileName

renameFunctions = []
renameFunctions.append(rightStrip)


def calculateFiles(path): 
	filesInHierarchy = []
	for root, dirs, files in os.walk(path):
		filesInHierarchy.append((root,files));
	print filesInHierarchy
	return filesInHierarchy


def renameResult(fileName):
	return renameFunctions[0](fileName)

def run(fileNames,deepness):
	for entry in fileNames[:deepness]:
		folder = entry[0]
		for fileName in entry[1]:
			os.rename(os.path.join(folder,fileName),os.path.join(folder,renameResult(fileName)))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Rename files in bulk")
	parser.add_argument('-f',default=".")
	parser.add_argument('-r','-R',action='store_true',dest="recursive")
	args = parser.parse_args()
	print args.recursive;
	#run(calculateFiles(args.f),2)
