from utils import convert_file_name
from settings import AVATAR_IMGS_DIR, DOMAIN


async def save_avatar_im_to_static(avatar_img_file, username):
    """
    Save avatar image to static folder
    """
    avatar_img_file.filename = convert_file_name(avatar_img_file, username)
    contents = await avatar_img_file.read()
    # save the file
    with open(f"{AVATAR_IMGS_DIR}{avatar_img_file.filename}", "wb") as f:
        f.write(contents)
    return DOMAIN + AVATAR_IMGS_DIR + avatar_img_file.filename