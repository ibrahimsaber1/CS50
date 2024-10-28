file_name = input("file name: ").lower().strip()
# print(file_name[-3:])

if file_name[-4:] == ".gif" or file_name[-4:] == ".png":
    print(f"image/{file_name[-3:]}")
elif file_name[-5:] == ".jpeg" or file_name[-4:] == ".jpg" :
    print(f"image/jpeg")
elif  file_name[-4:] == ".zip" or file_name[-4:] == ".pdf":
    print(f"application/{file_name[-3:]}")
elif file_name[-4:] == ".txt":
    print(f"text/{file_name[:-4]}")
else:
    print("application/octet-stream")
