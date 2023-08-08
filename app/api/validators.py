from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        charity_room_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(charity_room_id, session)
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return charity_project


async def check_charity_project_opened(
        charity_room_id: int,
        session: AsyncSession,
) -> None:
    charity_project = await charity_project_crud.get(charity_room_id, session)
    if charity_project.close_date is not None:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_charity_project_invested(
        charity_room_id: int,
        session: AsyncSession,
) -> None:
    charity_project = await charity_project_crud.get(charity_room_id, session)
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_charity_project_new_full_amount(
        project: CharityProject,
        new_full_amount: int,
) -> None:
    if (project.full_amount < new_full_amount
            or project.invested_amount > new_full_amount):
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )
