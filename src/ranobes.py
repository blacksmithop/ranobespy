from requests_html import HTMLSession
from src.latest_comments import CommentParser


BASE_URL = "https://ranobes.top/index.php"

comment_parser = CommentParser()

class Ranobes:
    def __init__(self, username: str, password: str):
        self.session = HTMLSession()
        self.authenticate_session_with_credentials(username, password)
        # add re-authenticate logic

    def authenticate_session_with_credentials(self, username: str, password: str):
        self.session.post(f"{BASE_URL}?do=lostpassword", files=dict(login_name=username, login_password=password, login="submit"))

    def get_latest_comments(self):
        response = self.session.post(f"{BASE_URL}?do=lastcomments")
        response.html.render()
        comment_data = comment_parser.parse_data(response.text)
        return comment_data