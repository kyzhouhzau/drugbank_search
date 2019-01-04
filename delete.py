#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""

from elasticsearch import Elasticsearch

_es = Elasticsearch()
_es.indices.delete(index='pubmed_index', ignore=[400, 404])