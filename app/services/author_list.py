import pandas as pd
import numpy as np
import re

#For convering string to list
def get_keywords(expertise_area):

    expertise_area = expertise_area.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "")
    keyword =re.findall(r"'(.*?)'", expertise_area, re.DOTALL)

    return keyword

# return the number of matching keywords from two lists
def get_author_expertise_area_match(list1,list2):
    list3 = list1 + list2
    c=0
    df = pd.value_counts(np.array(list3))

    for j in df.values:
        if j>=2:
            c=c+1

    return c

#This function gives author ranking
"""
Input is PMCID, user keywords
Output is author ranking
"""
def top_author_list(pubmed_id,list1):

    df_co_author = pd.read_csv('~/Documents/CIMPLE_project/app/services/dataset/co_author_expertise_area1.csv')
    df_author = pd.read_csv('~/Documents/CIMPLE_project/app/services/dataset/author_info_test1_new.csv')


    top_authors ={}
    row1 = df_author[df_author['paper_id'] == pubmed_id].index[0]
    author_list=[]
    authors = df_author['Author_list'][row1]
    for i in range(len(authors.split(","))):
        author_list.append(authors.split(",")[i].replace("[", "").replace('"', "").replace(']', "").lstrip())
    for i in range(len(author_list)):
        author = author_list[i].replace("'","")
        keywords = []

        if str(author) in list(df_co_author['author_name']):

            row = df_co_author[df_co_author['author_name'] == author].index[0]
            expertise_area = df_co_author['expertise_area'][row]

        else:

            continue

        keywords = get_keywords(expertise_area)
        top_authors[author] = get_author_expertise_area_match(keywords, list1)
    return top_authors