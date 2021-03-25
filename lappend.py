################
#
# This file is part of LicenseAppender.
#
# LicenseAppender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# LicenseAppender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with LicenseAppender.  If not, see <https://www.gnu.org/licenses/>.
#
################
from liapp.runparam import *
from liapp.append import *
import os
import sys

def print_usage():
	print("Usage: ", sys.argv[0], "[flags]...")
	print("\t-l [license name] \tSpecifies the name of license to append. Type --list to list available license")
	print("\t-e [extensions] \tSpecifies the extensions of files to append license to")
	print("\t-n [name] \t\tSpecifies the name of the license holder")
	print("\t-y [year] \t\tSpecifies the year to add to license")
	print("\t-p [year] \t\tSpecifies the name of the program to add to license")
	print("\t--list\t\t\tLists available licenses")
	
def print_available_licenses():
	print("Available licenses:")
	for (_, _, filenames) in os.walk("licenses"):
		for filename in filenames:
			print(" -" + filename)

def main():
	if len(sys.argv) == 2:
		if sys.argv[1].lower() == "--help" or sys.argv[1].lower() == "-help":
			print_usage()
			return
		elif sys.argv[1] == "--list":
			print_available_licenses()
			return
	
	try:
		param = parseParameters(sys.argv)
	except InvalidUsage:
		print("Invalid usage! Type --help for usage")
		return
	except InvalidOption as err:
		print("Invalid option:", err.what, "Type --help for usage")
		return

	if param == None:
		print_usage()
		return
	
	if len(param.extensions) == 0:
		print("Extensions not specified! Type --help for usage")
		return
	
	if len(param.name) == 0 or len(param.year) == 0 or len(param.program_name) == 0:
		print("License informations not specified! Type --help for usage")
		return
	
	if not check_file_extensions(param.extensions):
		print("\"." + ext + "\" is not a known file extension! Type --help for usage")
		return
	
	if not os.path.exists(param.location):
		print("\"" + param.location + "\" does not exist! Type --help for usage")
		return
	
	try_add_license(param)
					
if __name__ == "__main__":
	main()
    