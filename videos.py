import os

path = "redball/redball (5-10-2021 8-30-30 PM)/"
images = os.listdir(path)
print(images)
for i in range(len(images)):
    print(images[i])

