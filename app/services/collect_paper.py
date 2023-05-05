import pandas as pd
import numpy as np


def keyword_extraction_from_list(keywords):
    if isinstance(keywords,float):
        return 0
    array=[]
    for i in range(len(keywords.split(","))):
            # array.append(keywords.split(",")[i].replace("[","").replace('"',"").replace(']',"").lstrip())
            array.append(keywords.split(",")[i].replace("[", "").replace("'", "").replace(']', "").lstrip())
    return array

def match_paper(keyword_list):
    print("keyword_list ",keyword_list)
    matching_papers = {}

    df = pd.read_csv('/home/farhana/Documents/orkg-email-address-extraction-main./app/services/dataset/author_info_test1_new.csv')
    length = len(df)
    for i in range(length):

        c = 0
        # print("i ",i)
        # print("before ",df['paper_kewords_from_pubmed'][i])
        author_keywords = keyword_extraction_from_list(df['paper_kewords_from_pubmed'][i])
        # print("author_keyword ",author_keywords)
        if author_keywords == 0:
            continue

        list1 = keyword_list + author_keywords
        # print("list1 ",list1)
        df1 = pd.value_counts(np.array(list1))
        # print("df1.index",df1.index)
        # print("df1.values ",df1.values)
        for j in df1.values:
            if j >= 2:
                c = c + 1
        # print("c ",c)
        if c >= 1:
            matching_papers[df['paper_id'][i]] = c
        matching_papers = sorted(matching_papers.items(), key=lambda x: x[1], reverse=True)
        matching_papers = dict(matching_papers)
        # print("matching papers ", matching_papers)

    top_item = None
    top_value = None
    for key, value in matching_papers.items():
        top_item = key
        top_value = value
        break
    # print("top item", top_item)
    # print("top value", top_value)
    row = df[df['paper_id'] == top_item].index[0]
    doi = df['doi'][row]
    # print("doi ",doi)

    return top_item, top_value,doi