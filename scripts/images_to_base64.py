import base64, glob, os

os.chdir("./gatos")
for file in glob.glob("*.jpg"):
    with open(file, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
    
    newFile = file.rsplit(".")[0]
    print(newFile)
    with open('./converted/m_g'+newFile, 'x') as f:
        f.write(b64_string.decode('utf-8'))

# print(b64_string.decode('utf-8'))
