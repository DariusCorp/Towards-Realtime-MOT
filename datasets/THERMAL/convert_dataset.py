import json
import os
from glob import glob
from os.path import join, isfile

PATH_THERMAL = './images'
PATH_LABELS = './labels_with_ids/'
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

if __name__ == '__main__':
    json_file = open('D:/Licenta/Towards-Realtime-MOT/datasets/THERMAL/instances_default.json')
    json_annotations = json.load(json_file)
    thermal_images = [f for f in os.listdir(PATH_THERMAL) if isfile(join(PATH_THERMAL, f))]

    print(thermal_images)
    for annotation in json_annotations['annotations']:
        write_mode = 'a'
        if annotation['category_id'] == 1:
            if isfile(PATH_LABELS + thermal_images[annotation['image_id'] - 1].replace('.bmp', '.txt')) is False:
                write_mode = 'w'
            labels_with_ids_file = open(PATH_LABELS + thermal_images[annotation['image_id'] - 1].replace('.bmp', '.txt'),
                                        write_mode)
            x_min = annotation['bbox'][0]
            y_min = annotation['bbox'][1]
            width = annotation['bbox'][2]
            height = annotation['bbox'][3]
            labels_with_ids_file.write("{category} {identity} {x_center} {y_center} {width} {height}\n".format(
                category=0,
                identity=annotation['attributes']['track_id'],
                x_center=(x_min + width / 2) / IMAGE_WIDTH,
                y_center=(y_min + height / 2) / IMAGE_HEIGHT,
                width=width / IMAGE_WIDTH,
                height=height / IMAGE_HEIGHT,
            ))
    for annotation in json_annotations['annotations']:
        if isfile(PATH_LABELS + thermal_images[annotation['image_id'] - 1].replace('.bmp', '.txt')) is False:
            write_mode = 'w'
            labels_with_ids_file = open(
                PATH_LABELS + thermal_images[annotation['image_id'] - 1].replace('.bmp', '.txt'),
                write_mode)
            labels_with_ids_file.write('')
# 640/480