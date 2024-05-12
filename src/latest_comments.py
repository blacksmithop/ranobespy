from bs4 import BeautifulSoup
from src.models import Author, Comment, Novel
from typing import List
from src.utils.profile_image import parse_profile_images

class CommentParser:
    def parse_data(self, html_text: str):
        soup = BeautifulSoup(html_text, "html.parser")
        cmnt_divs = soup.find_all("div", class_="comment")
        
        comments: List[Comment] = []
        
        for cmnt_div in cmnt_divs:
            
            try:
                author_name, author_profile_url = cmnt_div.find("a").text, cmnt_div.find("a")["href"]
                author_image_style = cmnt_div.find("a").find("span")["style"]
                author_image_url = parse_profile_images(image_style=author_image_style)
                
                upvote, downvote = cmnt_div.find("span", class_="ratingplus").find("span").text, cmnt_div.find("span", class_="ratingminus").find("span").text
                
                novel_name = cmnt_div.find("h4")["title"]
                novel_image_src = cmnt_div.find("img")["src"]
                novel_image_url = f"https://ranobes.top{novel_image_src}"
                
                comment_url = cmnt_div.find("div", class_="com_content").find("a")["href"]
                novel_url = comment_url.split("#")[0]
                
                novel_chapter_raw = cmnt_div.find("b", class_="title").find("a").text
                
                try:
                    chapter_num = novel_chapter_raw.strip("\n:")
                    if chapter_num == "":
                        novel_chapter = None
                    else:
                        chapter_num = chapter_num.split(" ")[1]
                        chapter_num = chapter_num.rstrip(":.")
                        chapter_num = chapter_num.replace('\ufeff', '')
                        try:
                            novel_chapter = int(chapter_num)
                        except Exception as e:
                            novel_chapter = float(chapter_num)
                except Exception as e:
                    print(e)
                    novel_chapter = None

                comment_text = cmnt_div.find("div", class_="cont-text").find_all("div")[0].text
                
                author = Author(name=author_name, profile_url=author_profile_url, image_url=author_image_url)
                novel = Novel(name=novel_name, novel_url=novel_url, image_url=novel_image_url, chapter=novel_chapter)
                comment = Comment(author=author, upvote=upvote, downvote=downvote, novel=novel, comment=comment_text, comment_url=comment_url)
                
                comments.append(comment)
        
            except Exception as e:
                print(e)

        return comments
            