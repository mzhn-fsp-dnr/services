"""Application main."""

# --------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
# --------------------------------------------#
from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from src.routers import services
from src import database, config
from src.models import base


@lru_cache
def get_settings():
    return config.Settings()


conf_settings = get_settings()

app = FastAPI(debug=conf_settings.APP_DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=conf_settings.ALLOWED_ORIGINS,
    allow_credentials=conf_settings.ALLOW_CREDENTIALS,
    allow_methods=conf_settings.ALLOW_METHODS,
    allow_headers=conf_settings.ALLOW_HEADERS,
)
app.include_router(services.router)

logger.add("log_api.log", rotation="100 MB")  # Automatically rotate log file


def get_info():
    """
    Info function.
    """
    info = {"version": conf_settings.APP_VERSION, "fastapi_debug": app.debug}
    return info


@app.get("/health")
def health():
    """
    Health router.
    """
    logger.info("this is health")
    result = {"status": "ok", "info": get_info()}
    return result
