#!/bin/bash       

#SBATCH -p bgmp               #partition time

#SBATCH --cpus-per-task=24    #number of cores requested 

#SBATCH --job-name=STAR_Bi623   #Job name
#SBATCH -o %j.out               # File to which standard out will be written
#SBATCH -e %j.err		        #File to which standard err will be written
#SBATCH --nodes=1               #number of nodes
#SBATCH --ntasks=1              #numberof tasks per array job
#SBATCH --account=bgmp  
#SBATCH --time=0-5:00:00



#where the genome index will be stored
genome_Dir="/projects/bgmp/schalla/bioinfo/Bi623/Assignment/Leslie_Assignment/QAA/genome_Dir/Mus_musculus.GRCm39.dna.ens104.STAR_2.7.1a"
#where the reference genome is 
genome_fastafile="Mus_musculus.GRCm39.dna.primary_assembly.fa"

#where the annotation is 
genome_gtf="/projects/bgmp/schalla/bioinfo/Bi623/Assignment/Leslie_Assignment/QAA/Code/Mus_musculus.GRCm39.104.gtf"

#reads to be alligned as provided by Leslie: 
# Reads from Library 14
L14_R1="/projects/bgmp/shared/2017_sequencing/demultiplexed/14_3B_control_S10_L008_R1_001.fastq.gz"
L14_R2="/projects/bgmp/shared/2017_sequencing/demultiplexed/14_3B_control_S10_L008_R2_001.fastq.gz"

# Reads from Library 14
L11_R1="/projects/bgmp/shared/2017_sequencing/demultiplexed/11_2H_both_S9_L008_R1_001.fastq.gz"
L11_R2="/projects/bgmp/shared/2017_sequencing/demultiplexed/11_2H_both_S9_L008_R2_001.fastq.gz"

out_file_14="/projects/bgmp/schalla/bioinfo/Bi623/Assignment/Leslie_Assignment/QAA/Output/Mmus_alligned_L14"

out_file_11="/projects/bgmp/schalla/bioinfo/Bi623/Assignment/Leslie_Assignment/QAA/Output/Mmus_alligned_L11"

conda activate QAA
module load samtools/1.5

echo $genome_Dir
echo $genome_fastafile

##Indexing the genome /generating the index files. The indexed files will then be stored in genome_Dir
#/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate --genomeDir $genome_Dir  --genomeFastaFiles $genome_fastafile --sjdbGTFfile $genome_gtf


#Aligining to the ref genome or mapping the input reads (14R1, 14R2 and 11R1,11R2) to the ref genome:
/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped Within KeepPairs --alignIntronMax 1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn $L14_R1 $L14_R2 --genomeDir $genome_Dir --outFileNamePrefix $out_file_14

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped Within KeepPairs --alignIntronMax 1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn $L11_R1 $L11_R2 --genomeDir $genome_Dir --outFileNamePrefix $out_file_11
 
