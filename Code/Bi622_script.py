#!/usr/bin/env python
import argparse, re 
import gzip 
import Bioinfo
import matplotlib.pyplot as plt

def get_args():
	parser = argparse.ArgumentParser(description ="A program to calculate quality score distribution per nucleotide")
	parser.add_argument("-f", required=True)
	parser.add_argument("-o", required=False)
	return parser.parse_args()

args = get_args()
input_file = args.f


def init_list(lst: list, value: float=0.0) -> list:
	for i in range(0,101): # looping 101 times, not walking through the list 
		lst.append(value)
	return lst
print("running")

my_list=[]
my_list = init_list(my_list,0.0) # my_list (RHS) is original empty list, my_list (LHS) is the result ofthe computed expression(fn call)
def populate_list(file):
	my_list=[]
	my_list = init_list(my_list,0.0) 
	with gzip.open (file, "rt") as fh:
		line_cnt= 0
		for record in fh: #looping through every record
			line = record.strip('\n')
			if line_cnt%4 ==3:
				index = 0
				for letter in line:
					my_list[index] += Bioinfo.convert_phred(letter)  
					index += 1
			line_cnt+=1 
	return my_list,line_cnt

my_list,count = populate_list(input_file)	

index=0 #  elements in my_list
print("# Base Pair Mean Quality Score", sep="\t")
for score in my_list:
    reads=(count/4)
    mean_qual = score/reads
    my_list[index]= mean_qual
   
    print(index, my_list[index], sep="\t")
    index +=1


x = range(index)

plt.bar(x,height = my_list) #ro - dot plot / plt.bar(my_list) - bar graph 
plt.axis([0,100,0,45]) # The axis function in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
plt.title('nucleotide distribution')
plt.xlabel('Base Pair')
plt.ylabel('mean Q')
plt.savefig('11_untrimR2.png')
#plt.show()
