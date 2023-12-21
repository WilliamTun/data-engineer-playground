process sayHello {
    """
    echo 'hello world' > file.txt
    """
}

workflow {
    sayHello()
}