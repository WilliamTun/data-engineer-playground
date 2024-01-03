
'''
prerequisites:
1. Go to EBI (European Nucleotide Archive)
2. Create a links.txt file
   which contains ftp links to fasta files:


   eg. 
   $ cat links.txt 
   ftp://ftp.sta.ebi.ac.uk/vol1/fastq/ERR333/004/ERR_1.fastq.gz
   ftp://ftp.sta.ebi.ac.uk/vol1/fastq/ERR333/004/ERR_2.fastq.gz
'''

params.linkfile="path/to/links.txt"
params.fastqfir="path/to/fastq"    # where downloaded files will be outputted

process download {

publishDir("${params.fastqdir}", mode: 'copy')

input:
    path linkfile 

output: 
    path: "*", emit: outputfile 

script:
"""
cat $linkfile | xargs -i -P 2wegt '{}'
"""
}

workflow {

link_ch=Channel.fromPath(params.linkfile) 
download(link_ch)                  # calling the "download process"
download.out.outputfile.view()     # calling & printing what is emitted from download process. 
}
