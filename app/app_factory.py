import os

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from common.errors import OrkgNlpApiError
from common.util import io

# from routers import email, ORCID_email,unpywall_email,keyword_from_title,keyword_from_doi,title_from_author_name,fact_checker_system
from routers import fact_checker_system
_registered_services = []


def create_app():
    app = FastAPI(
        title='CIMPLE Project',
        root_path=os.getenv('CIMPLE', ''),
        servers=[
            {'url': os.getenv('CIMPLE', ''), 'description': ''}
        ],
    )

    _configure_app_routes(app)
    _configure_exception_handlers(app)
    _configure_cors_policy(app)
    _save_openapi_specification(app)

    return app


def _configure_app_routes(app):
    # app.include_router(email.router)
    # app.include_router(ORCID_email.router)
    # app.include_router(unpywall_email.router)
    # app.include_router(keyword_from_doi.router)
    # app.include_router(keyword_from_title.router)
    # app.include_router(title_from_author_name.router)
    app.include_router(fact_checker_system.router)


def _configure_exception_handlers(app):

    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )

    async def orkg_email_extraction_api_exception_handler(request: Request, exc: OrkgNlpApiError):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                'location': exc.class_name,
                'detail': exc.detail
            })
        )

    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(OrkgNlpApiError, orkg_email_extraction_api_exception_handler)


def _configure_cors_policy(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False
    )


def _save_openapi_specification(app):
    app_dir = os.path.dirname(os.path.realpath(__file__))
    io.write_json(app.openapi(), os.path.join(app_dir, '..', 'openapi.json'))
