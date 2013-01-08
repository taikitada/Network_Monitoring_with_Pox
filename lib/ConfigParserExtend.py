import ConfigParser

class ConfigParserExtend:
	def __init__(self, config_file):
		self.config = ConfigParser.SafeConfigParser()
		(self.config).read(config_file)
		self.ConfigDict = {}

	def ReturnConfigDict(self):
		for section in (self.config).sections():
			self.ConfigDict[section] = {}
			for option in (self.config).options(section):
				self.ConfigDict[section].update({option: (self.config).get(section, option)})
		return self.ConfigDict

	"""
	Really, want to change to the ConfigDict Class Objext
	"""
	def ConfigParseDefine(self): # this is not work
		ClassX = "ClassX = type('ClassX', (object,), dict(a=1,b=2))"
		exec(ClassX)


if __name__ == '__main__':
	ConfigDict = ConfigParseDict("server.conf")
	print ConfigDict
