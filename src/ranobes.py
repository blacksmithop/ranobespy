from requests_html import AsyncHTMLSession
from src.latest_comments import CommentParser


BASE_URL = "https://ranobes.top/index.php"

comment_parser = CommentParser()

class Ranobes:
    def __init__(self, username: str, password: str):
        self.session = AsyncHTMLSession()

        self.session.run(lambda: self.authenticate_session_with_credentials(username=username, password=password))

    async def authenticate_session_with_credentials(self, username: str, password: str):
        await self.session.post(f"{BASE_URL}?do=lostpassword", files=dict(login_name=username, login_password=password, login="submit"))
        print("Authenticated")

    async def fetch_comment_data(self):
        response = await self.session.post(f"{BASE_URL}?do=lastcomments")
        await response.html.arender()
        return response
    
    def get_latest_comments(self):
        response = self.session.run(self.fetch_comment_data)[0]
        comment_data = comment_parser.parse_data(response.text)
        return comment_data