import pandas as pd
import numpy as np

#converting string to list
def keyword_extraction_from_list(keywords):
    if isinstance(keywords,float):
        return 0
    array=[]
    for i in range(len(keywords.split(","))):
            # array.append(keywords.split(",")[i].replace("[","").replace('"',"").replace(']',"").lstrip())
            array.append(keywords.split(",")[i].replace("[", "").replace("'", "").replace(']', "").lstrip())
    return array


#for getting one paper which has the most matching keywords
"""
input is user keywords
Output is one paper which has the most matching keywords 
"""
def match_paper(keyword_list):
    print("keyword_list ",keyword_list)
    matching_papers = {}

    df = pd.read_csv('~/Documents/CIMPLE_project/app/services/dataset/author_info_test1_new.csv')
    length = len(df)
    for i in range(length):

        c = 0
        author_keywords = keyword_extraction_from_list(df['paper_kewords_from_pubmed'][i])
        if author_keywords == 0:
            continue

        list1 = keyword_list + author_keywords
        df1 = pd.value_counts(np.array(list1))
        for j in df1.values:
            if j >= 2:
                c = c + 1
        if c >= 1:
            matching_papers[df['paper_id'][i]] = c
        matching_papers = sorted(matching_papers.items(), key=lambda x: x[1], reverse=True)
        matching_papers = dict(matching_papers)

    top_item = None
    top_value = None
    for key, value in matching_papers.items():
        top_item = key
        top_value = value
        break

    row = df[df['paper_id'] == top_item].index[0]
    doi = df['doi'][row]


    return top_item, doi