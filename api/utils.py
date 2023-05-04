from routers import AVATAR_IMGS_DIR, DOMAIN



def convertFileName(file, newFileName):
    oldFileName = file.filename
    tail_index = oldFileName.rfind(".")
    return newFileName + oldFileName[tail_index:]


async def saveAvartarImgToStatic(file, fileName):
    file.filename = convertFileName(file, fileName)
    contents = await file.read()
    
 
    #save the file
    with open(f"{AVATAR_IMGS_DIR}{file.filename}", "wb") as f:
        f.write(contents)
 
    return DOMAIN + AVATAR_IMGS_DIR + file.filename