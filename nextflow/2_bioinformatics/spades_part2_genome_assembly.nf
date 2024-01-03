
params.read1="path/to/read1_fastq.gz"
params.read2="path/to/read2_fastq.gz"
params.SPADES_OUTPUT="path/to/SPADES_OUTPUT"


process assemble {

publishDir("${params.SPADES_OUTPUT}", mode: "copy")

input:
    path read1 
    path read2 

output:
    path "*", emit: spades_output 

script:

"""

# explanation: https://www.youtube.com/watch?v=8x9fYQGjO68&list=PLe1-kjuYBZ07r9atHzJmxpZjsxPOBHLf9&index=4&ab_channel=BioinformaticsCoach
# 35 minutes into the video
echo ${read1.simpleName} | cut -d'_' -f | xargs -i spades.py --careful -1 $read1 -2 $read2 -o '{}' 


"""

}

workflow {

read1_ch = Channel.fromPath(params.read1)
read2_ch = Channel.fromPath(params.read2)

assemble(read1_ch, read2_ch)
assemble.out.spades_output.view() # view what is emitted 
}
