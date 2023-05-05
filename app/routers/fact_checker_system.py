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
        user_keywords =[]
        #converting string to list from user input
        for i in range(len(keywords.split(","))):
            user_keywords.append(keywords.split(",")[i].replace("[", "").replace('"', "").replace(']', "").lstrip())
        pubmed_id, doi = match_paper(user_keywords) # here pubmed_id means PMCID
        if pubmed_id == None:
            print("not found")
        else:
            recommended_author = top_author_list(pubmed_id,user_keywords)

        return doi ,recommended_author
    except:
        print("keywords are not matched with existing papers")






