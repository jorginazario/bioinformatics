import re
import collections

with open("blasr_ecoli.sam", 'r') as sam_file:
	#add each line to a dictionary of lists
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
	new_d = collections.defaultdict(list)
	#iterate over dict, saving lines with a 0 and 16
	for k, v in d.iteritems():
		ct = 0
		keep = 0
		for i in v:
			alignment = i.split()[1]
			if(ct == 0):
				prev = alignment
				ct += 1
			elif(ct == 1):
				curr = alignment
				if(curr == prev):
					keep = 0
				else:
					keep = 1
				ct = 0
		if(keep == 1):
			for j in v:
				new_d[k].append(j)

	#return the sizes
	for k, v in new_d.iteritems():
		print k, ": "
		for j in v:
			strand = j.split()[9]
			print "\t", len(strand)
	print "Total inconsistencies: ",len(new_d)
