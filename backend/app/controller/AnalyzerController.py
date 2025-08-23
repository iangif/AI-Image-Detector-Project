from fastapi import APIRouter, Query, File, UploadFile

router = APIRouter()


@router.get("/test")
def get_items(category: str = Query(None)):
    print("Made it")
    return {"message": "Access Successful!"}

@router.post("/image-upload")
async def uploadImage(file: UploadFile = File(...)) :
    filename = file.filename
    contentType = file.content_type

    contents = await file.read()

    with open(f"uploads/{filename}", "wb") as f :
        f.write(contents)
    
    return {"filename": filename, "type": contentType, "size": len(contents)}
