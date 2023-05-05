import pandas as pd
import numpy as np
import re
def get_keywords(expertise_area):
    # keyword = []
    # expertise_area = ''.join((z for z in expertise_area if not z.isdigit()))
    # expertise_area = expertise_area.replace("'","").replace("(","").replace(")","").replace("'","")
    # print("expertise_area loop ",type(expertise_area))
    #
    # # for x,y in range(len(expertise_area.split(","))):
    # #     print("x ",x)
    # #     print("y ",y)
    # #     keyword.append(x)
    # for i in range(len(expertise_area.split(","))):
    #     keyword.append(expertise_area.split(",")[i].replace("[", "").replace('"', "").replace(']', "").lstrip())
    # # print("exper ",keyword)
    #
    # return keyword
    expertise_area = expertise_area.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "")
    keyword =re.findall(r"'(.*?)'", expertise_area, re.DOTALL)

    return keyword

def get_author_expertise_area_match(list1,list2):
    list3 = list1 + list2
    print("list3 ",list3)
    c=0
    df = pd.value_counts(np.array(list3))
    print("df.index",df.index)
    print("df.values ",df.values)
    # print("df loop ",df)
    for j in df.values:
        # print("j ",j)
        if j>=2:
            c=c+1
            # print("j ",j)
    return c


def top_author_list(pubmed_id,list1):

    df_co_author = pd.read_csv('/home/farhana/Documents/orkg-email-address-extraction-main./app/services/dataset/co_author_expertise_area1.csv')
    df_author = pd.read_csv('/home/farhana/Documents/orkg-email-address-extraction-main./app/services/dataset/author_info_for_20_data.csv')


    top_authors ={}
    row1 = df_author[df_author['paper_id'] == pubmed_id].index[0]
    #print(pubmed_id)
    #print(np.argwhere(df_author.values == pubmed_id).tolist())
    author_list=[]
    authors = df_author['Author_list'][row1]
    for i in range(len(authors.split(","))):
        author_list.append(authors.split(",")[i].replace("[", "").replace('"', "").replace(']', "").lstrip())
    # print("type ",type(author_list))
    for i in range(len(author_list)):
        author = author_list[i].replace("'","")
        print("author ",author)
        keywords = []
        #     Celestin  Danwang
        #     Celestin  Danwang
        # if author in list(df_author['Author_name']):
        #     row = df_author[df_author['Author_name'] == author].index[0]
        #     expertise_area = df_author['expertise_area_from_pubmed'][row]
        # print("df  ",df_co_author['author_name'][0])

        if str(author) in list(df_co_author['author_name']):

            row = df_co_author[df_co_author['author_name'] == author].index[0]
            print("row ",row)
            expertise_area = df_co_author['expertise_area'][row]
            print("exper type ",type(expertise_area))
        else:
            print('f{0} not found', author)
            continue
        print("expertise area ", expertise_area)

        keywords = get_keywords(expertise_area)
        print("keywords ",keywords)
        top_authors[author] = get_author_expertise_area_match(keywords, list1)
        print("top author ",top_authors)
    return top_authors