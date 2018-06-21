import xml.etree.ElementTree as ET
import os
from os import getcwd

image_path = 'D:/DataSet_raccon/raccoon_dataset-master/train_image/'
annot_path = 'D:/DataSet_raccon/raccoon_dataset-master/train_annot/'
image_val_path = 'D:/DataSet_raccon/raccoon_dataset-master/valid_image/'
annot_val_path = 'D:/DataSet_raccon/raccoon_dataset-master/valid_annot/'
classes = ['raccoon']


# convert annotation to image_id xmin, ymin, xmax, ymax, cls_id
def convert_annotation(in_file):
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),
             int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file = " " + ",".join([str(a) for a in b]) + ',' + str(cls_id)
        return list_file


image_list = []
annot_list = []
for image_file in os.listdir(image_val_path):
    image_list.append(image_file)
for annot_file in os.listdir(annot_val_path):
    annot_list.append(annot_file)

with open('voc_valid.txt', 'w') as f:
    for image, annot in zip(image_list, annot_list):
        voc_file = convert_annotation(annot_val_path+annot)
        voc_image_file = image_val_path+image+' '+voc_file
        f.write(voc_image_file)
        f.write('\n')



