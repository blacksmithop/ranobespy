import gradio as gr 
from dotenv import load_dotenv
from os import getenv
from src.ranobes import Ranobes
from src.models import Comment
from typing import List


load_dotenv()

USERNAME, PASSWORD = getenv("RANOBES_USERNAME"), getenv("RANOBES_PASSWORD")
ranobes = Ranobes(username=USERNAME, password=PASSWORD)

with gr.Blocks() as demo:
    gr.Markdown("# Latest Comments")

    comments = ranobes.get_latest_comments()
    comments: List[Comment]

    for comment in comments:
        author = comment.author
        novel = comment.novel
        
        # with st.chat_message(name=author.name, avatar=author.image_url):
        gr.Markdown(f"Author: {author.name}")
        gr.Markdown(f"<img src=\"{author.image_url}\" alt=\"Image Alt\" gryle=\"height: 50px; width:50px;\"/>")
        # gr.Markdown(f"![MarineGEO circle logo]({author.image_url} \"MarineGEO logo\")")
        
        gr.Markdown(f"Novel: [{novel.name}]({novel.novel_url})")
        gr.Markdown(f"Chapter: {novel.chapter}")
        gr.Markdown(f"<img src=\"{novel.image_url}\" alt=\"Image Alt\" gryle=\"height: 50px; width:50px;\"/>")
        # gr.Markdown(f"![MarineGEO circle logo]({novel.image_url} \"MarineGEO logo\")")
        
        gr.Markdown(f"Comment: {comment.comment}")
        gr.Markdown(f"{comment.upvote}👍 {comment.downvote}👎")


if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0', server_port=8000)