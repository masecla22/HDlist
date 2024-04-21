import zopflipng
import requests
from bs4 import BeautifulSoup
import os
import shutil
from PIL import Image


def download_asset(item):
    originalItem = item
    item = item.replace(" ", "_")
    url = f"https://hayday.fandom.com/wiki/{item}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Find an imd with data-image-key = f"{item}.png"
        img = None
        for i in soup.find_all("img"):
            if i.get("data-image-key") == f"{item}.png" and i.get("src").startswith(
                "https://"
            ):
                img = i
                break
        if img:
            img_url = img["src"]
            # Remove all query parameters
            img_url = img_url.split("?")[0]
            img_url = img_url.split("/revision")[0]
            print(f"Downloading {item} from {img_url}")
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(f"../images_original/{originalItem}.png", "wb") as f:
                    f.write(img_response.content)
        else:
            print(f"No image found for {item}")


def resize_asset(item):
    sizes = [256, 128, 64, 32]
    for size in sizes:
        img = Image.open(f"../images_original/{item}.png")
        img.thumbnail((size, size))
        img.save(f"../public/assets/images_{size}/{item}.png", "PNG", optimize=True)

        # Optimize using zopflipng
        data = open(f"../public/assets/images_{size}/{item}.png", "rb").read()
        result, code = zopflipng.png_optimize(data)

        if code == 0:
            with open(f"../public/assets/images_{size}/{item}.png", "wb") as f:
                f.write(result)
        else:
            print(f"Error optimizing {item}")

        print(f"  Resized {item} to {size}x{size}")
        print(
            f"  Optimized {item} to {os.path.getsize(f'../public/assets/images_{size}/{item}.png')} bytes"
        )


# ADD HERE
items = ["Help"]

for item in items:
    # download_asset(item)
    resize_asset(item)
