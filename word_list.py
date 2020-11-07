from itertools import product
import sys
import optparse
import asyncio
import os
class Word_List:
    def __init__(self):
        self.options=self.get_options()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.generate_word_list())


    def get_options(self):
        parse = optparse.OptionParser(f"Usage:    {sys.argv[0]} -f <from lenght> -t <to lenght> -c <charset>\nExample:  {sys.argv[0]} -f 5 -t 10 -c ABCD123")
        parse.add_option('-f',dest='FROM',type='int',help='specify the lenght of word list beging from') 
        parse.add_option('-t',dest='TO',type='int',help='specify the lenght of word list will ended in') 
        parse.add_option('-c',dest='CHARSET',type='string',help='specify the word list charset') 
        parse.add_option('-o',dest='OUTPUT',type='string',help='specify the output file') 
        (options,args)=parse.parse_args()
        if not options.CHARSET or not options.TO or not options.FROM or not options.OUTPUT:
            print(parse.usage)
            exit(0)
        elif options.TO < options.FROM:
            print(parse.usage)
            exit(0)
        else:
            return (options)
            
    async def generate_word_list(self):
        if os.path.exists(self.options.OUTPUT):
            os.remove(self.options.OUTPUT)
        with open(self.options.OUTPUT,'a') as file:
            for row in range(self.options.FROM,self.options.TO+1):
                for line in list(product(self.options.CHARSET,repeat=row)):
                    #await asyncio.sleep(1)
                    file.write(''.join(line)+"\n")

Word_List()
                
            




