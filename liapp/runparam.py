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
import sys
        
class RunParam:
	def __init__(self):
		pass
	
	location = ""
	license = ""
	extensions = []
	name = ""
	year = ""
	program_name = ""
	
class InvalidUsage(BaseException):
	def __init__(self):
		pass

class InvalidOption(BaseException):
	def __init__(self, w):
		self.what = w
	
def parseExtensions(extensions):
	ret = extensions.split('.')
	if len(ret):
		for i in range(0, len(ret) - 1):
			ext = ret[i]
			if len(ext) == 0:
				ret.pop(i)
	return ret
	
def parseParameters(argv):
	ret = RunParam()
	
	argv_len = len(argv)
	if argv_len > 1:
		i = 1
		while i < argv_len:
			arg = argv[i]
			
			if arg == "-l":
				i += 1
				if i < argv_len:
					ret.license = argv[i]
				else:
					raise InvalidUsage()
			elif arg == "-e":
				i += 1
				if i < argv_len:
					ret.extensions = parseExtensions(argv[i])
				else:
					raise InvalidUsage()
			elif arg == "-n":
				i += 1
				if i < argv_len:
					ret.name = argv[i]
				else:
					raise InvalidUsage()
			elif arg == "-y":
				i += 1
				if i < argv_len:
					ret.year = argv[i]
				else:
					raise InvalidUsage()
			elif arg == "-p":
				i += 1
				if i < argv_len:
					ret.program_name = argv[i]
				else:
					raise InvalidUsage()
			else:
				if arg[0] == '-':
					raise InvalidOption(arg)
				else:
					ret.location = arg
			i += 1

		return ret
	return None
			
					