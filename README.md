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
* [Problem Set](#problem-set)
    - [Sales Data](#sales-data)
    - [Log Data](#log-data)
    - [Forum Data](#forum-data)
    - [Using Combiner](#using-combiner)
* [Author](#author)

## Project Scope

The problem set is building around the three datasets typical for Big Data: sales, web logs and forum. Advancing through the problem set, I will answer questions about the data with MapReduce and Hadoop, learn the fundamental principles behind it, and understand MapReduce design patterns.

### Project Environment

The Hadoop environment comes with a [virtual machine image](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-VM-4.1.1.c.zip) from Cloudera, executed in [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
1) Unzip the virtual machine image;
1) In VirtualBox, create a new Linux/RedHat64 machine;
1) I've given it 8 Gb memory and 2 CPUs;
1) Choose to use an existing hard disk and point to `*.vmdk` file of the VM image;
1) Set VM network adapter to 'Bridged Adapter';
1) Start the machine. You can SSH and SFTP to it's IP with user 'training' & password 'training'.

### Project Datasets

* **Sales Data**: This data comes with the machine image in `~/udacity_training/data/purchases.txt` tab-separated. A 1000-line sample is available in this repository.
* **Web Server Log**: This data comes with the machine image in `~/udacity_training/data/access_log` in [Common Log Format](http://en.wikipedia.org/wiki/Common_Log_Format). A 1000-line sample is available in this repository.
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

## Problem Set

### Sales Data

- [x] Give us a sales breakdown by product category across all of our stores.

> `hs map_sale_by_item.py reduce_sum.py _`

- [x] Find the monetary value for the highest individual sale for each separate store.

> `hs map_sale_by_store.py reduce_max.py _`

- [x] Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

> `hs map_sale_by_store.py reduce_totals.py _`

- [x] Find mean of sales for each weekday.

> `hs map_sale_by_weekday.py reduce_mean.py _`

### Log Data

- [x] Count hits to page.

> `hs map_log_by_path.py reduce_sum.py _` then `grep` for page.

- [x] Count hits from IP.

> `hs map_log_by_ip.py reduce_sum.py _` then `grep` for IP.

- [x] Find the most popular path(s) by counts.

> 1) `hs map_log_by_path.py reduce_sum.py _`, save to `hit_count.tsv`
> 1) `sort -t$'\t' -k2nr hit_count.tsv | head -5`  
> or  
> `cat hit_count.tsv | ./reduce_top.py`

### Forum Data

- [x] Create an index of all words that appear in the body of a forum post and node id(s) they can be found in.

> `hs map_forum_index.py reduce_index.py _`

- [x] Join the forum node and forum user data: `forum_nodes.tsv` and `forum_users.tsv`. The output from the reducer for each forum post should be:`forum_nodes.id` `forum_nodes.title` `forum_nodes.author_id` `forum_nodes.node_type` `forum_nodes.added_at` `forum_nodes.score` `forum_users.reputation` separated by `\t`.

> The mapper, `map_forum_join.py` should take in records from both `forum_node` and `forum_users` and keep, for each record, those fields that are needed for the reducer output. The mapper will start each line with user id followed by the line type (1 = user, 2 = node) to mark where it comes from (user data or node data).
>
> The mapper key for both types of lines is the user id: either `forum_users.user_ptr_id` or `forum_nodes.author_id`. During the sort and shuffle phases lines will be grouped based on the user id so the reducer can process and join them appropriately.
>
> Reducer, `reduce_forum_join.py` joins the tsv lines that come from 2 sources:
> 1) Line that starts with userid then 1 is the user data
> 1) Line that starts with userid then 2 is the forum node data

- [x] For each user find the hour(s) during which the user has posted the most posts.

> `hs map_forum_user_hour.py reduce_frequent.py _`

- [x] Process `forum_nodes.tsv` and output the length of the post and the average answer (just answer, not comment) length for each post.

> `hs map_forum_answer.py reduce_forum_answer.py _`

- [x] Find top 10 tags, ordered by the number of questions they appear in.

> Use `map_forum_tags.py` to count each tag appearance as 1, then two existing reducers: `reduce_sum.py` as combiner to count tag's appearances and then `reduce_top.py`

### Using Combiner

Compare the counter statistics of the same MapReduce job running with and without combiner. Combiner is the same as the reducer.

> `hs  map_sale_by_weekday.py reduce_max.py _`
> `hsc map_sale_by_weekday.py reduce_max.py _`

|Counter|Without Combiner|With Combiner|
|:---|---:|---:|
|Map input records|4,138,476|4,138,476|
|Map output records|4,138,476|4,138,476|
|Map output bytes|35,840,096|35,840,096|
|Combine input records|0|4,138,584|
|Combine output records|0|136|
|Reduce shuffle bytes|44,117,072|332|
|Reduce input records|4,138,476|28|
|Reduce output records|7|7|
|Spilled Records|12,219,835|164|
|CPU time spent (ms)|90,750|81,810|

As you can see, the combiner dramatically decreases records shuffling between the mapping and the reducing nodes. The visible performance increase is just 10% because Hadoop is running on a local machine, it will be higher on a real cluster where the records exchange between the nodes takes place over the network.

[//]: # (## What I Have Learned)

[//]: # (Through the implementation of this project I've learned:)

## Author

Andrii Dzugaiev, [in:dzugaev](https://www.linkedin.com/in/dzugaev/)
