from fastapi import APIRouter


router=APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    return{"status":"OK"}

@router.get("/First_test")
def test():
    return{"Message":"Omaala naanga dha"}