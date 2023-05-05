import json
import sys
import pandas as pd
sys.path.append("..")

from fastapi import APIRouter, UploadFile, Form, File
from fastapi.responses import HTMLResponse

from app.common.util.decorators import log
from app.services.author_list import top_author_list
from app.services.collect_paper import match_paper

router = APIRouter(
    prefix='/fact_checker_suggestion',
    tags=['fact_checker']
)

@router.post('/fact_checker_suggestion/', status_code=200)
@log(__name__)
def get_author_list(keywords):
    try:
        # recommended_author = None
        # pubmed_id =None
        # print("type ",type(keywords))
        # list1 = keywords.split(",")
        list1 =[]
        for i in range(len(keywords.split(","))):
            list1.append(keywords.split(",")[i].replace("[", "").replace('"', "").replace(']', "").lstrip())
        pubmed_id, value, doi = match_paper(list1)
        print("pubmed_id ",pubmed_id)
        if pubmed_id == None:
            print("not found")
        else:
            recommended_author = top_author_list(pubmed_id,list1)

        return doi ,recommended_author
    except:
        print("keywords are not matched with existing papers")






