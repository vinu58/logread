#!/usr/bin/python
#read log files


print "Welcome to my log checking script"
print "#################################"

file=raw_input ('please enter the filename along with path (eg: /var/log/syslog)\n')
keyword=raw_input ('please enter the keyword to be searched(bluetooth or sigterm)\n')

with open( file, 'r' ) as f:
	for line in f:
		if keyword in line:
			print line
			
#Another method

def readfile():
    try:
        with open( file, 'r' ) as f:
            for line in f:
                if keyword in line:
                    print line
    
    except:
        print "Something went wrong"
	
print readfile()

#except IOError:
#    print('An error occured trying to read the file.')
    
#except ValueError:
#    print('Non-numeric data found in the file.')

#except ImportError:
#    print "NO module found"
    
#except EOFError:
#    print('Why did you do an EOF on me?')

#except KeyboardInterrupt:
#    print('You cancelled the operation.')

#except:
#    print('An error occured.') 

