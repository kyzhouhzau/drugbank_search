#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
from elasticsearch import Elasticsearch
from config import config as cf
from elasticsearch.helpers import bulk, streaming_bulk

es = Elasticsearch()
def create_index(client,index):
    if not es.indices.exists(index='pubmed_index'):
        client.indices.create(index=index, body=cf.index_mappings)

def main(datapath):
    
    create_index(es,"pubmed_index")
    # we load the repo and all commits
    with open(datapath,'r') as rf:
        count=0
        actions=[]
        for line in rf:
            line = line.strip()
            line = line.strip()
            json = eval(line)
            try:
                action = {"_index":"pubmed_index",
                                "_type":"PubMed",
                                "_id":json["id"],
                                "_source":json
                        }
            except KeyError:
                with open("ennro.log",'a') as wf:
                        wf.write(line)
                continue

            actions.append(action)
            if len(actions)==3000:
                success, _ = bulk(es, actions, index = "pubmed_index")
                es.indices.refresh(index='pubmed_index')
                count+=success
                actions=[]
                print("成功插入 {} 篇文本！".format(count))
        success, _ = bulk(es, actions, index = "pubmed_index")
        es.indices.refresh(index='pubmed_index')
        count+=success
        print("成功插入 {} 篇文本！".format(count))
    
if __name__=="__main__":
    datapath = "./pubtator29/4-4.txt"
    main(datapath)
    # print(es.count(index='pubmed_index')['count'], 'documents in index')