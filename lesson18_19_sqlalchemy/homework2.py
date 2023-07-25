import asyncio
from sqlalchemy import select
from models import User, Post, Like, session


async def update_users_likes():
    async with session() as session:
        async with session.begin():
            users = await session.execute(
                select(User).join(Post).outerjoin(Like).group_by(User).having(Like.id.is_(None))
            )
            users_without_likes = users.scalars().all()

            for user in users_without_likes:
                for post in user.posts:
                    like = Like()
                    post.likes.append(like)

    async with session() as session:
        async with session.begin():
            users = await session.execute(
                select(User).join(Post).join(Like)
            )
            users_with_likes = users.scalars().all()

            for user in users_with_likes:
                print("User:", user.name)
                for post in user.posts:
                    print("Post:", post.title)
                    for like in post.likes:
                        print("Like ID:", like.id)


asyncio.run(update_users_likes())