from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

# from elasticsearchapp import models
import models

# make global connection to your ElasticSearch
connections.create_connection()

# The DocType works as a wrapper to enable you to write an index like a model
class BlogPostIndex(DocType):
	author = Text()
	posted_date = Date()
	title = Text()
	text = Text()

	class Meta:
		index = 'blogpost-index'
	# The bulk command is located in elasticsearch.helpers which is included when you 
	# installed elasticsearch_dsl since it is built on top of that library. 

def bulk_indexing():
	BlogPostIndex.init()
	es = Elasticsearch()
	bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
