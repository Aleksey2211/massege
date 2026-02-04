from database import async_session_maker
from configs import settings, DATABASE_URL

from sqlalchemy import select
from users.models import User

class UserDAO:


    @classmethod
    async def find_all_users(cls):
        async with async_session_maker as session:
            query = select(User)
            users = await session.execute(query)
            return users.scalars().all()



