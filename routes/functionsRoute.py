from fastapi import APIRouter,Query
from models.functionsInfo import functionInfo
from database.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/functions")
async def getAllFunctions():
    functionsInfo =list_serial(collection_name.find())
    return functionsInfo

@router.get("/functions/{id}")
async def getFunctionInfo(id: str)->functionInfo | dict:
    functionInfo = collection_name.find_one({"_id": ObjectId(id)})
    if functionInfo is None:
        return {"message": "function not found"}
    return functionInfo

@router.get("/findByFunctionName")
async def get_functions_by_name(functionName: str):
    function_infos = list(collection_name.find({
        "functionName": functionName
    }))
    return list_serial(function_infos)
   
@router.get("/findByFunctionAndFileName")
async def get_functions_by_name(functionName: str):
    function_infos =collection_name.find({
        "functionName": functionName
    })
    return list_serial(function_infos)
       
@router.get("/functions/{id}/fileName")
async def getFileName(id: str):
    functionInfo = collection_name.find_one({"_id": ObjectId(id)})
    return ({"fileName": functionInfo.get("fileName")})

@router.get("/functions/{id}/functionName")
async def getFunctionName(id: str):
    functionInfo = collection_name.find_one({"_id": ObjectId(id)})
    return ({"functionName": functionInfo.get("functionName")})

@router.get("/functions/{id}/functionBody")
async def getFunctionBody(id: str):
    functionInfo = collection_name.find_one({"_id": ObjectId(id)})
    if functionInfo:
        return ({"functionBody": functionInfo.get("functionBody")})
    else:
        return ({"message": "function is Empty"})
    
@router.get("/functions/{id}/fileClass")
async def getFunctionClass(id: str):
    functionInfo = collection_name.find_one({"_id": ObjectId(id)})
    if functionInfo:
        return ({"fileClass": functionInfo.get("fileClass")})
    else:
        return ({"message": "Function does not belong to any class"})

@router.post("/functions")
async def postFunctions( function: functionInfo):
    collection_name.insert_one(dict(function))      
    return ({"message": "Added Successfully"})

@router.put("/functions/{id}")
async def putFunctions( id:str, function:functionInfo):
    collection_name.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(function)})
    return ({"message": "Updated Successfully"})

@router.patch("/functions/{id}/functionBody")
async def patchFunctionsBody( id:str, functionBody: dict):
    function_id = ObjectId(id)
    collection_name.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(functionBody)})
    return ({"message": "Updated Successfully"})
