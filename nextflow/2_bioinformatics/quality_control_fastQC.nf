params.fastq = "path/to/fastq/*"
params.qc_report = "path/to/output_report"

process QC {
publishDir("${params.qc_report}", mode: "copy")

input:
    path fastq 

output:
    path "*"

script:
"""
fastqc $fastq
"""

}