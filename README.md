# MapReduce with Hadoop & Python

## About / Synopsis

This project is my workbook of exercises completed through the Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617).

## Table of Contents
* [Project Scope](#project-scope)
    - [Project Environment](#project-environment)
    - [Project Datasets](#project-datasets)
* [Running MapReduce Jobs](#running-mapreduce-jobs)
    - [Test Your Job](#test-your-job)
    - [Put Data on HDFS](#put-data-on-hdfs)
    - [Run Hadoop](#run-hadoop)
    - [Get Result and Clear Output](#get-result-and-clear-output)
* [Author](#author)

## Project Scope

The problem set is building around the three datasets typical for Big Data: sales, web logs and forum. Advancing through the problem set, I will answer questions about the data with MapReduce and Hadoop, learn the fundamental principles behind it, and understand MapReduce design patterns.

### Project Environment

The Hadoop environment comes with a [virtual machine image](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-V M-4.1.1.c.zip) from Cloudera, executed in [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
1) Unzip the virtual machine image;
1) In VirtualBox, create a new Linux/RedHat64 machine;
1) I've given it 8 Gb memory and 2 CPUs;
1) Choose to use an existing hard disk and point to `*.vmdk` file of the VM image;
1) Set VM network adapter to 'Bridged Adapter';
1) Start the machine. You can SSH and SFTP to it's IP with user 'training' & password 'training'.

### Project Datasets

* **Sales Data**: This data comes with the machine image in `~/udacity_training/data/purchases.txt` tab-separated. A 1000-line sample is available in this repository.
* **Web Server Log**: This data comes with the machine image in `~/udacity_training/data/access_log` in [Common Log Format](http://en.wikipedia.org/wiki/Common_Log_Format) A 1000-line sample is available in this repository.
* **Forum Data**: Two tab-separated files representing forum nodes and users. It comes [from here](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz). Be careful taking the samples as the forum nodes body can contain newlines. Small testing samples are available in this repository.

## Running MapReduce Jobs

### Test Your Job

`cat testfile | ./mapper.py | sort | ./reducer.py`

Test files can be prepared from the datasets with `head` or `grep`, likewise these commands can be used in the above pipeline directly. Save test files if you need to reuse them or send more than one dataset to your mapper: `cat testfile1 testfile2 | _`

### Put Data on HDFS

`hadoop fs -mkdir input_folder`

`hadoop fs -put data_file input_folder/`

### Run Hadoop

Use alias `hs` defined in `.bashrc`:

`hs mapper.py reducer.py input_folder output_folder`

Alias `hsc` has the same syntax and runs `reducer.py` as a combiner on mapper nodes before reducing. Think well if using the reducer as a combiner is appropriate for your job.

### Get Result and Clear Output

`hadoop fs -get output_folder/part-00000 local_file`

`hadoop fs -rm -r output_folder`

To save your past result from overwriting, the Hadoop job will not run if `output_folder` exists. Before running your next job either remove or specify another output folder.

[//]: # (## What I Have Learned)

[//]: # (Through the implementation of this project I've learned:)

## Author

Andrii Dzugaiev, [in:dzugaev](https://www.linkedin.com/in/dzugaev/)
