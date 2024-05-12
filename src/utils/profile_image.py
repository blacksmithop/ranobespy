import re

URL_EXPR = r"(?<=background-image:url\()[^?)]+(?=[?)])"
find_url = re.compile(URL_EXPR)


def parse_profile_images(image_style: str):
    image_url = find_url.findall(image_style)[0]
    image_url = image_url.lstrip("/")
    
    if "ranobes" in image_url:
        image_url = f"https://{image_url}"
    elif "templates" in image_url:
        image_url = f"https://ranobes.top/{image_url}"
        
    return image_url