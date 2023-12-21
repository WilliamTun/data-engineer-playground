
# What is an executor?
- Executors run airflow tasks. 
- Different types exist that run tasks differently. 

# How to define an executor?
- via the "executor=" parameter
  in airflow.cfg file

# Examples:
- SequentialExecutor:
  - Default airflow executor
  - Runs one task at a time
  - good for debugging
  - not recommended for production
- LocalExecutor:
  - run on a single system
  - treats tasks as processes
  - can start concurrent tasks - limited by system resources
  - level of parallelism is defined by user
  - can use all the resources of a given host system
  - recommended for production
- CeleryExecutor:
  - Celery is a general queing system for python
  - Celery allows multiple systems to communicate
    as a basic cluster
  - multiple worker systems can be defined
  - Disadvantage:
    Celery is more difficult 
    to configure and set up
  - Advantage:
    Good for large scale production systems
    and tasks with many DAGs
    and requires lots of system resources
