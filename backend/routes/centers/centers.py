import sys
from typing import Any

from common.services.centers.centers import Centers
from common.errors import raise_http_error, ErrorCode
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get(
    path="/centers",
    tags=["ORMA_CENTERS"],
    summary="Get all Centers"
)
async def get_orma_centers(
        center_name: str = None,
        center_code: str = None,
        external: bool = False,
        deleted: bool = False,
        page: int = 1,
        size: int = 20
) -> Any:
    try:
        centers = Centers(
            center_name=center_name,
            center_code=center_code,
            external=external,
            deleted=deleted,
            page=page,
            size=size
        )

        return JSONResponse(
            content=centers.return_centers()
        )
    except:
        raise_http_error(file=__file__, sys_traceback=sys.exc_info())
