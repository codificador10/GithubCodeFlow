from fastapi import APIRouter
from models.repoInfo import RepoLink
from database.database import collection_name
from parser.pythonFilesFromRepoParse import parseTheRepo
from pymongo import UpdateOne

router = APIRouter()

@router.post("/parseRepo") 
async def postFunctions(repo_link: RepoLink):
    functions_info = parseTheRepo(repo_link.repo_link)
    bulk_operations = []

    for function_info in functions_info:
        filter_query = {
            "functionName": function_info.functionName,
            "fileName": function_info.fileName
        }

        update_operation = {
            "$setOnInsert": function_info.dict()
        }

        bulk_operations.append(UpdateOne(filter_query, update_operation, upsert=True))

    # Execute bulk update operations
    if bulk_operations:
        collection_name.bulk_write(bulk_operations, ordered=False)

    return {"message": "Functions added successfully"}