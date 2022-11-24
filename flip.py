import numpy as np
import cv2
from glob import glob
import os
import argparse

# parsing
parser = argparse.ArgumentParser()
parser.add_argument("dataset_input",
                    help="directory containing data you want to rotate.")

parser.add_argument("-o",
                    dest="dataset_output",
                    help="directory to store generated data. this directory will be made automatically.",
                    default="data_rotational")

parser.add_argument("-t",
                    dest="time_interval",
                    help="time interval to control speed of displaying images.",
                    default=0,
                    type=int)

parser.add_argument("-r",
                    dest="ratio",
                    help="ratio for ignoring bounding box near the edges of image.",
                    default=0.8,
                    type=float)

parser.add_argument("-a",
                    dest="angle_interval",
                    help="angle interval for rotating.",
                    default=0,
                    type=int)

parser.add_argument("-s",
                    dest="show_image",
                    action="store_true",
                    help="instead of saving data, showing images with bounding boxes without saving.",
                    default=False)

args = parser.parse_args()
dataset_input = args.dataset_input
dataset_output = args.dataset_output
time_interval = args.time_interval
ratio = args.ratio
angle_interval = args.angle_interval
show_image = args.show_image
angle_interval = [angle_interval]

dirname_input_image = os.path.join(dataset_input, "images")
dirname_input_label = os.path.join(dataset_input, "labels")
dirname_output_image = os.path.join(dataset_output, "images")
dirname_output_label = os.path.join(dataset_output, "labels")


def mkdir_p(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)


if not show_image:
    mkdir_p(dataset_output)
    mkdir_p(dirname_output_image)
    mkdir_p(dirname_output_label)

image_names = sorted(glob(dirname_input_image + "/*"))
print("# of images: %d" % len(image_names))


# label and coord are bounding box of yolo and opencv format respectively
# yolo format: <category> <x center> <y center> <width_bbox> <height_bbox> ; range: 0-1
# opencv format: <category> <x_left> <y_top> <x_right> <y_bottom> ; range: 0-width_image or 0-height_image
def label2coord(label,
                height_image,
                width_image):
    category = label[0]
    x_center_bbox = float(label[1])
    y_center_bbox = float(label[2])
    width_bbox = float(label[3])
    height_bbox = float(label[4])
    x_left = int((x_center_bbox - width_bbox / 2.) * width_image)
    x_right = int((x_center_bbox + width_bbox / 2.) * width_image)
    y_top = int((y_center_bbox - height_bbox / 2.) * height_image)
    y_bottom = int((y_center_bbox + height_bbox / 2.) * height_image)
    return category, x_left, y_top, x_right, y_bottom


def coord2label(coord,
                height_image,
                width_image):
    category = coord[0]
    x_left = float(coord[1])
    y_top = float(coord[2])
    x_right = float(coord[3])
    y_bottom = float(coord[4])
    x_center_bbox = (x_left + x_right) / 2. / width_image
    y_center_bbox = (y_top + y_bottom) / 2. / height_image

    if (x_right > x_left):
        width_bbox = (x_right - x_left) / width_image
    elif (x_left > x_right):
        width_bbox = (x_left - x_right) / width_image

    if(y_bottom > y_top):
        height_bbox = (y_bottom - y_top) / height_image
    elif(y_top > y_bottom):
        height_bbox = (y_top - y_bottom) / height_image

    return category, x_center_bbox, y_center_bbox, width_bbox, height_bbox


def show(image, time_interval):
    cv2.imshow("image", image)
    key = cv2.waitKey(time_interval)
    if key == ord("q"):
        quit()


for image_name0 in image_names:
    print(image_name0)
    label_name = os.path.join(dirname_input_label, os.path.splitext(os.path.basename(image_name0))[0] + ".txt")
    with open(label_name, "r") as f0:
        labels0 = f0.read().splitlines()

    image0 = cv2.imread(image_name0)
    height_image0, width_image0 = image0.shape[:2]
    coords = []
    for label in labels0:
        label = label.split()
        coord = label2coord(label, height_image0, width_image0)
        h2 = 2 * height_image0
        w2 = 2 * width_image0
        coords.append([coord[0], coord[1], coord[2], coord[3], coord[4]])

    for angle in angle_interval:
        image_name = os.path.join(dirname_output_image,
                                  os.path.splitext(os.path.basename(image_name0))[0] + "_%03d" % angle + ".jpg")
        label_name = os.path.join(dirname_output_label,
                                  os.path.splitext(os.path.basename(image_name0))[0] + "_%03d" % angle + ".txt")
        print(image_name)

        image = cv2.flip(image0, 1)
        center = int(width_image0 / 2)



        if show_image:
            image_annotated = image.copy()
        else:
            file_label = open(label_name, "w")

        for coord in coords:
            category, x_left0, y_top0, x_right0, y_bottom0 = coord
            print("original: ", category, x_left0, y_top0, x_right0, y_bottom0)
            area0 = (x_right0 - x_left0) * (y_bottom0 - y_top0)

            x_left = 2 * center - x_left0
            x_right = 2 * center - x_right0
            y_top, y_bottom = y_top0, y_bottom0

            x_left, x_right = np.clip([x_left, x_right], 0, width_image0)
            y_top, y_bottom = np.clip([y_top, y_bottom], 0, height_image0)
            area = (x_right - x_left) * (y_bottom - y_top)
            print("filp: ", category, x_left, y_top, x_right, y_bottom )
            label = coord2label([category, x_left, y_top, x_right, y_bottom], height_image0, width_image0)
            file_label.write(" ".join([str(l) for l in label]) + "\n")


        if not show_image:
            cv2.imwrite(image_name, image)

        else:
            show(image_annotated, time_interval)
