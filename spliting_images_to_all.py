import os
import sys
import cv2
import shutil
import random


image_dir = "images"
spliting_dir = "output"
persons = ["Prathamesh", "Rajeev", "Rushikesh", "Sanket", "Shubhanshu"]

os.makedirs(spliting_dir, exist_ok = True)


total_images = [os.path.join(sub_dir_path, images) for sub_dir_path in os.listdir(image_dir) for images in os.listdir(os.path.join(image_dir, sub_dir_path))]

# random.shuffle(total_images)
# random.shuffle(total_images)
print(len(total_images))
splited_images = []
img_len = int(len(total_images)/len(persons))
for i in range(0, len(total_images), img_len):
    splited_images.append(total_images[i:i+img_len])


for idx, pname in enumerate(persons):
    for image in splited_images[idx]:
        directory, imagename = os.path.split(image)
        output_dir = os.path.join(spliting_dir, pname, directory)
        os.makedirs(output_dir, exist_ok = True)
        output_path = os.path.join(output_dir, imagename)
        shutil.copy(os.path.join(image_dir, image), output_path)
