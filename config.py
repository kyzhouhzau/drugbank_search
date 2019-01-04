#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
class config():
    index_mappings = {
      "mappings": {
        "PubMed": {
          "properties": {
            "id":{
                  "type": "integer",
              },
            "title": {
              "type": "text",
              "analyzer": "standard",
              "search_analyzer": "standard"
            },
            "text": {
              "type": "text",
              "analyzer": "standard",
              "search_analyzer": "standard"
            },
             "denotations": {
              "type": "text",
              "analyzer": "standard",
              "search_analyzer": "standard"
            },
          }
        }
      }
    }
     