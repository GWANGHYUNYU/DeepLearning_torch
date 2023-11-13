from PIL import Image
import os

checkdir = r'D:\Coding\dataset\gender_kaggle\Train' # 데이터셋 경로
# checkdir = r'D:\Coding\dataset\gender_kaggle\Test' # 데이터셋 경로

files = os.listdir(checkdir)
format = [".JPG", ".JPEG",".PNG",'.jpg','.png','.jpeg'] # 이미지 파일 형식

for(path, dirs, f) in os.walk(checkdir):
    for file in f:
        if file.endswith(tuple(format)):
            try:
                temp_path = os.path.join(path, file)
                image = Image.open(temp_path).load()
                # image.close()
                #print(image)
            except Exception as e:
                print("An exception is raised:", e)
                print(file)
                os.remove(path+"/"+file)

# 083717.jpg        