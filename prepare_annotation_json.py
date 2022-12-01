import os
import sys
import json
import glob


image_dir = os.path.join("data", "images")
annotation_dir = os.path.join("data", "annotations")
os.makedirs(annotation_dir, exist_ok=True)

labels = ["background", "plastic"]
image_urls = []
annotation_urls = []

for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    name, ext = os.path.splitext(image_name)
    image_path = os.path.join(image_dir, image_name)
    annotation_path = os.path.join(annotation_dir, f"{name}.png")
    image_urls.append(image_path)
    annotation_urls.append(annotation_path)

annotation = {}
annotation['labels'] = labels
annotation['imageURLs'] = image_urls
annotation['annotationURLs'] = annotation_urls

with open("annotation.json", "w") as obj:
    json.dump(annotation, obj)