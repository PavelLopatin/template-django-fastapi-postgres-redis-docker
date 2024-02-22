from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/example")
async def example():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "OK"
        }
    )
