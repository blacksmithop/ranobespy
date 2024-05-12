from requests_html import HTMLSession

BASE_URL = "https://ranobes.top/index.php"


class Ranobes:
    def __init__(self, username: str, password: str):
        self.session = HTMLSession()
        self.authenticate_session_with_credentials(username, password)
        # add re-authenticate logic

    def authenticate_session_with_credentials(self, username: str, password: str):
        self.session.post(f"{BASE_URL}?do=lostpassword", files=dict(login_name=username, login_password=password, login="submit"))
