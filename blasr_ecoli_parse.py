import re
import collections

with open("blasr_ecoli.sam", 'r') as sam_file:
	#add each line to a dictionary of lists
	numlines = 0
        d = collections.defaultdict(list)
	for line in sam_file:
       	    if line.startswith('m'):
		    name = line.split()[0]
		    id_num = name
		    #id_num = name.split('/')[0]
		    #id_num = id_num.split('_')[2]
		    if(id_num in d):
			    if(len(d[id_num]) < 2):
				    d[id_num].append(line)
		    else:
			    d[id_num].append(line)
	    numlines += 1
	new_d = collections.defaultdict(list)
	#iterate over dict, saving lines with a 0 and 16
	for k, v in d.iteritems():
		ct = 0
		keep = 0
		for i in v:
			alignment = i.split()[1]
			sz = i.split()[9]
			if(ct == 0):
				prev = alignment
				ct += 1
			elif(ct == 1):
				curr = alignment
				if(curr == prev):
					keep = 0
				#elif(len(sz) > 10000):
				else:
					keep = 1
				ct = 0
		if(keep == 1):
			for j in v:
				new_d[k].append(j)

	#return the sizes
	VAL = 0
#	insertions = list()
#	deletions = list()
#	substitutions = list()
	for k, v in new_d.iteritems():
#		if(VAL > 10):
#			break
#		ins = 0
#		dels = 0
#		subs = 0
		print k, ": "
		for j in v:
			strand = j.split()[9]
#			info = j.split()[5]
#			info = info.split('=')
#			for m in info:
#				r = re.compile("([0-9]+)([a-zA-Z]+)([0-9]+)")
#				res = r.match(m)
#				if res:
#					num_occurrences = int(res.group(1))
#					chartype = res.group(2)
#				if(chartype == 'I'):
#					ins += num_occurrences
#				elif(chartype == 'S'):
#					subs += num_occurrences
#				elif(chartype == 'D'):
#					dels += num_occurrences
			print "\t", len(strand)
#		print "\tinsertions: ", ins, ", subs: ", subs, ", deletions: ", dels
#		VAL += 1
		
	print "Total inconsistencies: ",len(new_d)
	print "Total number of lines: ", numlines
	print "Percentage: ", 100 * float(len(new_d))/float(numlines)
