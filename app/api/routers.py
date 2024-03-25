from fastapi import APIRouter

from app.api.endpoints import endpoints

main_router = APIRouter()


for router in (endpoints.router,):
    main_router.include_router(router)
