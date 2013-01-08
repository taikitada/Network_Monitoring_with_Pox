import ConfigParser

def ConfigParseReturn(config_file, ):
	config = ConfigParser.SafeConfigParser()
	config.read('server.conf')

	for section in config.sections():
		print "<", section, ">"
		for option in config.options(section):
			print option, config.get(section, option)