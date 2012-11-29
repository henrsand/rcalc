import sys

try:
	# If filename given, read file and carry on..
	if len(sys.argv) > 1:
		infile = sys.argv[1]
		f = open(infile,'r')
		print 'File read:', infile
		
		# Define constants and functions
		x = 0.0
		rownumber = 1
		result = {		"ADD": lambda x: x+y,
					"SUB": lambda x: x-y,
					"MUL": lambda x: x*y,
					"DIV": lambda x: x/y,
					"SQR": lambda x: x*x,
					}
		
		# Read row by row and map instruction to function via a dictionary
		row = f.readline()
		while row:
			operation = row.split()[0]
			if len(row.split()) == 2: 
				value = row.split()[1]
				y = float(value)
			else: y = ""
			x = result[operation](x)		
			row = f.readline()
			rownumber += 1
		print "\nResult: %0.2f\n" % x
	else:
		print "No filename given. Use 'python rcalc2.py filename'	"

# Error handling
except IOError:
	print "File error. Is '" + infile + "' a valid file?"
except IndexError:
	print "\nError: No data on row", rownumber
except KeyError:
	print "\n\nError: Operation", operation, "on row", rownumber, "not permitted."
except ValueError:
	print "\n\nError: Value", value, "on row", rownumber, "is not a number."
except ZeroDivisionError:
	print "\n\nError: Division by zero on row", rownumber, "is not defined."