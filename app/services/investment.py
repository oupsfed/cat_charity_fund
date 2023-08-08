from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud


async def invest(obj_in,
                 session: AsyncSession):
    project = await charity_project_crud.get_by_attribute(
        'fully_invested',
        False,
        session)
    donation = await donation_crud.get_by_attribute(
        'fully_invested',
        False,
        session
    )
    if None in [donation, project]:
        return
    amount_to_close_project = project.full_amount - project.invested_amount
    donation_left = donation.full_amount - donation.invested_amount
    if amount_to_close_project > donation_left:
        project.invested_amount += donation_left
        donation.invested_amount = donation.full_amount
        donation.fully_invested = True
        donation.close_date = datetime.now()
    elif amount_to_close_project < donation_left:
        donation.invested_amount += amount_to_close_project
        project.invested_amount = project.full_amount
        project.fully_invested = True
        project.close_date = datetime.now()
    elif amount_to_close_project == donation_left:
        project.invested_amount = project.full_amount
        project.fully_invested = True
        project.close_date = datetime.now()
        donation.invested_amount = donation.full_amount
        donation.fully_invested = True
        donation.close_date = datetime.now()

    session.add(project)
    session.add(donation)
    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    await invest(obj_in, session)
