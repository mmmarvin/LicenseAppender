################
#
# License Appender v.1.00
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>. 
#
################
from os import walk
from os.path import splitext, join, exists, isdir
import sys

# Comment characters for known programming languages
knownFileExtensionList = \
{ \
	".cpp": ("/**********", " *", " **********/"), \
	".hpp": ("/**********", " *", " **********/"), \
	".c": ("/**********", " *", " **********/"), \
	".h": ("/**********", " *", " **********/"), \
	".java": ("/**********", " *", " **********/"), \
	".csharp": ("/**********", " *", " **********/"), \
	".js": ("/**********", " *", " **********/"), \
	".html": ("<!--", "", "-->"), \
	".lua": ("--[[", "", "--]]"), \
	".py": ("################", "#", "################") \
}

class Param:
	def __init__(self, lo, li):
		self.location = lo
		self.licenseFile = li
	
	location = ""
	licenseFile = ""

def askLicenseFile():
	licenseData = []
	done = False
	while not done:
		licenseFilename = input("Enter filename of license file: ")
		try:
			licenseData = readFile(licenseFilename)
		except FileNotFoundError:
			print("ERROR: Invalid file \"" + licenseFilename + "\"")
			continue
		done = True
	return licenseData
	
def readLicenseFile(filename):
	licenseData = []
	try:
		licenseData = readFile(filename)
	except FileNotFoundError:
		print("ERROR: Invalid file \"" + fliename + "\"")
		
	return licenseData
	
def readFile(filename):
	ret = []
	with open(filename) as f:
		line = f.readline()
		while len(line) > 0:
			ret.append(line)
			line = f.readline()
			
	return ret
	
def checkAllAreExtension(fileExtensionList):
	newFileExtensionList = []
	for f in fileExtensionList:
		if f[0] != ".":
			f = "." + f
		newFileExtensionList.append(f)
	return newFileExtensionList
	
def isExtensionIsInFileList(fileExtension, fileExtensionList):
	for f in fileExtensionList:
		if f == fileExtension:
			return True
			
	return False
	
def addLicense(licenseData, fileData, filename, fileExtension):
	with open(filename, "w") as f:
		startingComment = knownFileExtensionList[fileExtension][0]
		middleComment = knownFileExtensionList[fileExtension][1]
		endingComment = knownFileExtensionList[fileExtension][2]
		
		f.write(startingComment + "\n")
		f.write(middleComment + "\n")
		for line in licenseData:
			f.write(middleComment + " " + line)
		f.write(middleComment + "\n")
		f.write(endingComment)
		
		f.write("\n")
			
		for line in fileData:
			f.write(line)
			
		print("Added license to \"" + filename + "\"")
	
def tryAddLicense(licenseData, fileExtensionList, location):
	print("Traversing \"" + location + "\"")
	for (dirpath, _, filenames) in walk(location):
		for f in filenames:
			realFilename = join(dirpath, f)
			filename, fileExtension = splitext(realFilename)
			if isExtensionIsInFileList(fileExtension, fileExtensionList):
				if f != sys.argv[0]:
					fileData = readFile(realFilename)
					addLicense(licenseData, fileData, realFilename, fileExtension)
				
def printUsage():
	print("Usage:", sys.argv[0], "[dir][license filename]")
	print("\tdir - Location where to add LICENSES")
	print("\tlicense filename - Filename of license to append to files")
				
def parseCommandLine():
	sysLen = len(sys.argv)
	
	if sysLen == 2 or sysLen == 3:
		location = sys.argv[1]
		licenseFilename = ""
		
		if sysLen == 3:
			licenseFilename = sys.argv[2]
					
		# Do some checking
		if not exists(location)and not isdir(location):
			return (False, Param("", ""))
			
		if sysLen == 3:
			if not exists(licenseFilename):
				return (False, Param("", ""))
			
		return (True, Param(location, licenseFilename))
	else:
		printUsage()
		
	return (False, Param("", ""))
		
def main():
	c = parseCommandLine()
	if not c[0]:
		return
	
	print("License Appender v.1.00\nby: Marvin Manese\n")
	licenseData = []
	if len(c[1].licenseFile) == 0:
		licenseData = askLicenseFile()		
	else:
		licenseData = readLicenseFile(c[1].licenseFile)
		
	if len(licenseData) == 0:
		print("ERROR: Invalid license file!")
		return
		
	fileExtension = input("Enter file extensions to include license (separate by space): ")
	fileExtensionList = fileExtension.split()
	fileExtensionList = checkAllAreExtension(fileExtensionList)
	for extension in fileExtensionList:
		if not extension in knownFileExtensionList:
			print("ERROR: Unknown file extension \"" + extension + "\"")
			return
	print("")
	tryAddLicense(licenseData, fileExtensionList, c[1].location)

if __name__ == "__main__":
	main()
