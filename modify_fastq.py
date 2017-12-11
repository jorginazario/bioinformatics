import sys

counter = 0
with open(sys.argv[1], 'r') as myFile:
	for line in myFile:
		line = line.strip()
		counter += 1
		num = counter%4
		if num == 1:
			line = line.split(' ')
			print line[0] + "_5"
			secondname = line[0] + '_3'
		if num == 2:
			line_length = len(line)
			one_third_line_num = line_length/3
			print line[:one_third_line_num]
			secondbases = line[2*one_third_line_num:]
		if num == 3:
			line = line.split(' ')
			line = line[0]
			new_comment = line + "_5"
			secondcomment = line + '_3'
			print new_comment
		if num == 0:
			one_third_line_num = line_length/3
			print line[:one_third_line_num]
			print secondname
			print secondbases
			print secondcomment
			print line[2*one_third_line_num:]
			

