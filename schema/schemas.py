def individual_serial(functionInfo)->dict:
    return{
        "id": str(functionInfo["_id"]),
        "fileName": str(functionInfo["fileName"]),
        "functionName": str(functionInfo["functionName"]),
        "functionBody": str(functionInfo["functionBody"]),
        "functionClass": str(functionInfo["functionClass"]) if functionInfo["functionClass"] else None
    }

def list_serial(functionsInfo) -> list:
    return [individual_serial(functionInfo) for functionInfo in functionsInfo]

