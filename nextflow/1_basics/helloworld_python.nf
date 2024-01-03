process sayHello {
    """
    #!/usr/bin/python
    print("Hello world")
    """
}

workflow {
    sayHello()
}