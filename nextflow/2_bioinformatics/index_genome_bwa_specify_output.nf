
'''
Index a reference genome with BWA

Prerequisites:
1. install nextflow
2. install bwa
3. download reference genome. 
   eg. fasta sequence from NCBI (nucleotide section)

BWA is an aligner.
'''

params.ref="path/to/ref_genome.fa"
params.index_dir="path/to/output"

process index {

publishDir("${params.index_dir}", mode: 'copy')

input:
    path genome

output:
    path "${genome}.bwt", emit: ref_genome

script:
"""
bwa index $genome
"""
}

workflow {
    ref_ch=Channel.fromPath(params.ref)
 
index(ref_ch)                # calling the process "index"
index.out.ref_genome.view()


}