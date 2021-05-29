# project/app/db.py

import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")


def init_db(app: FastAPI) -> None:

    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoiseORM"]},
        generate_schemas=False,
        add_exception_handlers=False,
    )
    Tortoise.init_models(['app.models.tortoiseORM'], 'models')

async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoiseORM"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


# run_async(generate_schema())
if __name__ == "__main__":
    run_async(generate_schema())