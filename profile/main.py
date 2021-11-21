
import click

from utils.get_details import Details

@click.command()
@click.argument("user_name")
@click.option('-pic', default='', help='Path of your custom profile picture')
def create_profile(user_name: str, pic: str) -> None:
     details=Details()
     details(user_name=user_name,profile_pic=pic)
    


if __name__ == "__main__":
    create_profile()
