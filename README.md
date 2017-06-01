# django-elasticsearch

### ElasticSearch indexes documents for your data instead of using data tables like a regular relational database does. This speeds up search, and offers a lot of other benefits that you don’t get with a regular database.

### Installing elasticsearch
```
mkdir elasticsearch-example
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.tar.gz
tar -xzf elasticsearch-5.1.1.tar.gz
./elasticsearch-5.1.1/bin/elasticsearch
```
### $ curl -XGET http://localhost:9200 : run this command to see if it working or browse to the specified url.

Main changes are made in search.py, models.py, and signals.py for indexing

### To automatically index all the data for elasticsearch:
```
$ ./manage.py shell
>>> from elasticsearchapp.search import *
>>> bulk_indexing()
```
### To check for indexing use: $ curl -XGET 'localhost:9200/blogpost-index/blog_post_index/1?pretty'
Specify the id accordingly. In this example it is set to 1

### receiver is not working due to unknown issue.

### To make a search query here for author(to make search query function for other fields follow up search.py):
```
$ ./manage.py shell
>>> from elasticsearchapp.search import *
>>> print(search(author="<author name>"))
```
