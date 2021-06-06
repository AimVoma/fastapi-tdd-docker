# project/app/api/crud.py


from typing import List, Union

from app.models.pydanticSchemas import SummaryPayloadSchema
from app.models.tortoiseORM import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> Union[List, None]:
    summaries = await TextSummary.all().values()

    if not summaries:
        return None
    return summaries
