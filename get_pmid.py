#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
Bioconcept: We support five kinds of bioconcepts, i.e., Gene, Disease, Chemical, Species, Mutation. When 'BioConcept' is used, all five are included.
PMIDs: Single pmid or a pmid list (e.g. pmid=23819905,23819906)
"""
import requests
import os
import glob
def get_pmid(genes_path):
    if not os.path.exists('../pmid'):os.mkdir('../pmid')
    count=0
    with open(genes_path) as rf:
        for line in rf:
            count+=1
            gene = line.strip()
            url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={}&retmode=json&retmax=200000".format(gene)
            response = requests.get(url)
            json = eval(response.text)
            pmids = json["esearchresult"]["idlist"]
            num = len(pmids)
            with open('../pmid/'+gene + '.txt', 'w') as wf:
                for pmid in pmids:
                    wf.write(pmid+'\n')
            print("{} Finish get:{} 一共有id号{}个".format(count,gene,num))
def main():
    """
    first :run get_pmid(genes_path)
    second :run *
    :return:
    """
    #只在获取pmid号的时候使用
    #if not os.path.exists("../pmid/AAA1.txt"):
    print("Warning:正在从pubmed获取Pmid号！")
    print("如果已经下载，请停止！")
    genes_path = r"./2001.txt"
    get_pmid(genes_path)

if __name__=="__main__":
    main()

