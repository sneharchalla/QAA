#!/usr/bin/env python
import argparse, re 
import gzip 
import Bioinfo
import matplotlib.pyplot as plt
import numpy as np

def get_args():
	parser = argparse.ArgumentParser(description ="A program to calculate quality score distribution per nucleotide")
	parser.add_argument("-f1", required=True)
	parser.add_argument("-f2", required=True)
	parser.add_argument("-o", required=False)
	return parser.parse_args()

args = get_args()
input_file_1 = args.f1
input_file_2 = args.f2


def init_list(lst: list, value: float=0.0) -> list:
	for i in range(0,101): # looping 101 times, not walking through the list 
		lst.append(value)
	return lst
print("running")

#my_list=[]
#my_list = init_list(my_list,0.0) # my_list (RHS) is original empty list, my_list (LHS) is the result ofthe computed expression(fn call)
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

my_list_R1,count = populate_list(input_file_1)	
my_list_R2,count = populate_list(input_file_2)
index=0 #  elements in my_list
#print("# Base Pair Mean Quality Score", sep="\t")
#for score in my_list:
#    reads=(count/4)
#    mean_qual = score/reads
#    my_list[index]= mean_qual
#   
#    print(index, my_list[index], sep="\t")
#    index +=1


#x = range(101)
#X = ['Lib_14', 'Lib_11']
YR1 = my_list_R1  # values(Qscore) from R1 file for each library
YR2 = my_list_R2  # values from R2 file for each library

X_axis = np.linspace(0.0,101.0,101)#float(range(101))  # X_axis is the base position or every base position in the length of the read
#To avoid overlapping of bars in each library, the bars are shifted -0.2 units and +0.2 units from X-axis
#The width of the bars of each group is taken as 0.4 units
plt.bar(X_axis - 0.3, YR1, 0.4, label = 'R1', color = 'blue' ) #ro - dot plot / plt.bar(my_list) - bar graph 
plt.bar(X_axis + 0.3, YR2, 0.4, label = 'R2', color = 'red' )

#plt.xticks(X_axis, X)
plt.title('nucleotide distribution in the libraries')
plt.xlabel('Base pair pos')
plt.ylabel('Mean Q')
plt.savefig('11_combined.png')
#plt.show()
