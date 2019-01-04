#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
from elasticsearch import Elasticsearch
es = Elasticsearch()
def search_elastic():
        # _query = {
        # 'query': {
        #         'match': {
        #                         "denotations": "Species",
        #                 },
        # }
        # }
        # _query = {
        #         'query': {
        #                 'match_phrase': {
        #                 'denotations':{
        #                         'term':"mutation &",
                                        
        #                         }
        #                 }
        #         }
        # }
        _query = {
                'query': {
                        'constant_score': {
                        'filter':{
                                'bool':{
                                        'must':[
                                                {"term":{"id":"29643855"}},
                                                #{"term":{"denotations": "snp"}}
                                                ],
                                        }
                                }
                        }
                }
        }
        _searched = es.search(index='pubmed_index', doc_type='PubMed', body=_query)
        for hit in _searched['hits']['hits']:
                print(hit['_source'], flush=True)
                print("Score:>>>>>>>", hit["_score"])
        


if __name__=="__main__":
        search_elastic()
        print(es.count(index='pubmed_index')['count'], 'documents in index')