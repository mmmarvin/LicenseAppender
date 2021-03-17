################
#
# This file is part of LicenseAppender.
#
# LicenseAppender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
#
################
from liapp.runparam import *
import os

class LanguageComment:
	def __init__(self, s, c, e):
		self.starting_comment = s
		self.comment = c
		self.ending_comment = e
	
	starting_comment = ""
	comment = ""
	ending_comment = ""
	
_known_file_extension_list = \
{ \
	 "cpp": LanguageComment("/**********", " *", " **********/"), \
	 "hpp": LanguageComment("/**********", " *", " **********/"), \
	 "c": LanguageComment("/**********", " *", " **********/"), \
	 "h": LanguageComment("/**********", " *", " **********/"), \
	 "java": LanguageComment("/**********", " *", " **********/"), \
	 "cs": LanguageComment("/**********", " *", " **********/"), \
	 "js": LanguageComment("/**********", " *", " **********/"), \
	 "html": LanguageComment("<!--", "", "-->"), \
	 "lua": LanguageComment("--[[", "", "--]]"), \
	 ".py": LanguageComment("################", "#", "################") \
}
	
def check_file_extensions(extensions):
	for ext in extensions:
		if ext not in _known_file_extension_list:
			return False
	return True

def _read_license(filename, param):
	ret = []
	with open(filename, "r") as file:
		line = file.readline()
		while(len(line) > 0):
			ret.append(line.format(param.name, param.year, param.program_name))
			line = file.readline()
			
	return ret

def _read_data(filename):
	ret = []
	with open(filename, "r") as file:
		line = file.readline()
		while(len(line) > 0):
			ret.append(line)
			line = file.readline()
			
	return ret

def _load_license(license, param):
	ret = []
	
	license = license.lower()
	license_file = os.path.join("licenses",license)
	if os.path.exists(license_file):
		ret = _read_license(license_file, param)
	else:
		print("Cannot load license \"" + license + "\"! Please type --help for usage")
		raise RuntimeError("")
	
	return ret

def _add_license(full_filename, extension, license_data):
	file_data = _read_data(full_filename)
	
	with open(full_filename, "w") as f:
		starting_comment = _known_file_extension_list[extension].starting_comment
		comment = _known_file_extension_list[extension].comment
		ending_comment = _known_file_extension_list[extension].ending_comment
		
		f.write(starting_comment + "\n")
		f.write(comment + "\n")
		for line in license_data:
			f.write(comment + " " + line)
		f.write(comment + "\n")
		f.write(ending_comment + "\n")
		
		for line in file_data:
			f.write(line)
		
		print("Added license to \"" + full_filename + "\"")

def try_add_license(param):
	try:
		license_data = _load_license(param.license, param)
	except:
		return
	#print("Adding license:")
	#for line in license_data:
		#print(line)
	
	print("Traversing location \"" + param.location + "\"")
	for (dir_path, _, filenames) in os.walk(param.location):
		for filename in filenames:
			full_filename = os.path.join(dir_path, filename)
			f, ext = os.path.splitext(full_filename)
			ext = ext[1:]
			if ext in param.extensions:
				if ext in _known_file_extension_list:
 					_add_license(full_filename, ext, license_data)
	