"""
jiaotong kakou data
change bbox of csv file
"""
from functools import reduce
import cv2


def split_bbox(image_path):
    """
    Params:
        return image id, box_list of each car in image_id
    """
    image, bbox = image_path.split(',')
    each_bbox = bbox.split(';')

    sub_box = []
    for box in each_bbox:
        sub_box.append(box.split('_'))
    sub_box[-1][-1] = sub_box[-1][-1].split('\n')[0]
    return image, sub_box


def draw_rectangle(image, b_box):
    """
    Params:
        draw rectangle of box in image
    """
    img = cv2.imread(image)
    for box in b_box:
        x, y, w, h = [int(i) for i in box]
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), color=[255, 255, 0], thickness=2)

    cv2.imshow('1', img)
    if cv2.waitKeyEx() == ord('q'):
        cv2.destroyAllWindows()


def change_vocannoation(image_id, bbox, classes):
    """
    Params:
        return voc list format
    """
    classes_num = [x for x in range(len(classes))]
    new_list = [image_id]
    for box in bbox:
        new_list.extend(box)
        new_list.extend(classes_num)
    return new_list


def get_string(voc_list):
    """
    Params:
        return voc_list to string
    """
    str_line = ''
    str_root_path = '/home/jiangmingchao/jiaotongkakou_datasets/train_1w/'
    str_line += str_root_path
    str_line += str(voc_list[0])
    str_line_box_classes = ''
    voc_list_box = voc_list[1:]

    sub_sub_list = []

    for i in range(len(voc_list[1:])):
        # split with five elements
        if i % 5 == 0:
            sub_voc_list = []
            for num in range(5):
                index = 0
                # some image doesn't have coord (x, y, w, h) remove it from train_voc
                try:
                    sub_voc_list.append(str(int(float(voc_list_box.pop(index)))))
                except Exception as e:
                    print(str_line, voc_list[1:])
            sub_sub_list.append(sub_voc_list)

    str_bbox = ''
    for i in range(len(sub_sub_list)):
        str_single_bbox = reduce(lambda x, y: str(x) + ',' + str(y), sub_sub_list[i])
        str_bbox += str_single_bbox
        str_bbox += ' '

    str_line_box_classes += str_bbox

    return str_line + ' ' + str_line_box_classes


def generate_vocfile(input_path, output_path):
    """
    Params:
        return voc file
    """
    with open(input_path, 'r') as input_file:
        file_list = [line for line in input_file]
    train_file_list = file_list[1:]
    voc_file_list = []
    # generate a voc file list
    for i in range(len(train_file_list)):
        image, b_box = split_bbox(train_file_list[i])
        new_list = change_vocannoation(image, b_box, classes=['car'])
        voc_file_list.append(new_list)
    #　save voc format file to jiaotong_train.txt
    with open(output_path, 'w') as file:
        for file_line in voc_file_list:
            string_line = get_string(file_line)
            file.write(string_line)
            file.write('\n')
    print('output voc file have been done!')


if __name__ == '__main__':

    '''file path'''
    root_path = 'D:/DataSet_raccon/jiaotong_traffic/'
    train_bbox_path = root_path + 'train_1w.csv'
    train_bbox_path_b = root_path + 'train_b.csv'
    train_image_path = root_path + 'train_1w/'
    train_image_path_b = root_path + 'train_b/'
    output_voc_train_path = 'D:/DataSet_raccon/jiaotong_traffic/train_1w.txt'
    output_voc_trainb_path = 'D:/DataSet_raccon/jiaotong_traffic/train_b.txt'
    output_voc_train_1_path = 'D:/DataSet_raccon/jiaotong_traffic/train_1w1.txt'

    '''
    used for choice txt file
    '''
    FLAG = 'train_1w'

    if FLAG == 'train_1w':
        generate_vocfile(input_path=train_bbox_path, output_path=output_voc_train_1_path)
    else:
        generate_vocfile(input_path=train_bbox_path_b, output_path=output_voc_trainb_path)

