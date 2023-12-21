
# Run scripts
'''
nextflow run 1_helloworld.nf
'''

The above command will run and execute the helloworld nextflow script. It will create an output folder called "work". Within this is the outputs of the nextflow pipeline.
... Alternatively, you can specificy the outputs to be placed in a specific path. 


Note. If you want to add logs that print to the terminal in nextflow, in the nextflow script, just add in echo commands. 
To highlight echo's commands even further, you can call:
'''
nextflow run 1_helloworld.ng -process.echo 
'''

# Resource:
https://www.youtube.com/watch?v=sp45Bzri2sA&list=PLe1-kjuYBZ07r9atHzJmxpZjsxPOBHLf9
