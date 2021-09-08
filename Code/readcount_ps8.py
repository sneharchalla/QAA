#!/usr/bin/env python
import argparse, re 
#import matplotlib.pyplot as plt

def get_args():
	
	parser = argparse.ArgumentParser(description ="A program to parse protein fasta files and filter only the longest protein per gene")
	parser.add_argument("-f", required=True)
	parser.add_argument("-o", required=True)
	
	return parser.parse_args()

args = get_args()
input_file = args.f
out_file = args.o

mapped_count=0
unmapped_count=0
#uniq_dict= {}

with open (input_file, "r") as fh:
	while True:
		new_line = fh.readline()
		if new_line == "" :
			break
		if new_line[0] == "@": #check for qname
			continue
		else:
			flag = new_line.split()[1]
			#name = new_line.split()[0]
			#uniq_dict[name] = flag
	#for key,value in uniq_dict.items():
		#flag = value
			if ((int(flag) & 4)!=4) and ((int(flag) & 256 )!= 256):  #is it mapped?
				#mapped = True
				mapped_count+=1
			else:
				if ((int(flag) & 256 )!= 256):
					unmapped_count+=1
			
total = mapped_count + unmapped_count
print(mapped_count,unmapped_count)
#print(total)

with open ('out_file' , "w") as fo:			
	fo.write(f"Mapped Count:{mapped_count}\n Unmapped Count:{unmapped_count}\n Total:{total}\n")
		
		




