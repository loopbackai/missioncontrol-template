import asyncio
from launchkit import LaunchKit


def add_user_to_newsletter(email: str):
    """
    Add a user to the newsletter.
    """
    return {"message": f"User {email} added to newsletter. 2"}


async def launch_rocket():
    """
    Launch a rocket.
    """
    for i in range(3):
        print(f"Rocket launching in {3-i}...")
        await asyncio.sleep(1)
    return {"message": "Rocket launched!"}


actions = LaunchKit([launch_rocket, add_user_to_newsletter])
