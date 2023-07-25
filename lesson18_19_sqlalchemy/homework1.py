import asyncio
from datetime import datetime
from sqlalchemy import select
from models import Post, Comment, session


async def update_post_with_comment(post_id, new_comment):
    async with session() as session:
        async with session.begin():
            post = await session.get(Post, post_id)
            comments = post.comments

            if comments:
                first_comment = comments[0]
                updated_title = f"{first_comment.title} (updated at {datetime.now()})"
                first_comment.title = updated_title


            new_comment_obj = Comment(new_comment)
            comments.append(new_comment_obj)

    async with session() as session:
        async with session.begin():
            post = await session.get(Post, post_id)
            comments = post.comments

            print("Updated Title:", comments[0].title)
            print("New Comment:", comments[-1].text)

post_id = 1
new_comment = "This is a new comment"

asyncio.run(update_post_with_comment(post_id, new_comment))