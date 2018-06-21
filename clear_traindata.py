"""
The train data have some image do not have car so the bbox is none.
The first stage is to drop this from train.txt
"""
from functools import reduce
import re

root_path = 'D:/DataSet_raccon/jiaotong_traffic/'
train_path = 'train_1w.csv'
train_middle_path = 'train_1w_not_drop_0.txt'
home_root = '/home/jiangmingchao/jiaotongkakou_datasets/train_1w/'

if __name__ == '__main__':

    with open(root_path+train_path, 'r') as input_file:
        new_line = []
        for line in input_file:
            
            newline = line.replace('_', ',').replace(';', ',0 ').split('\n')[0]
            new_line.append(newline)

    new_line = new_line[1:]
    darg_zero = []
    index_num = []   # pop index list

    for i in range(len(new_line)):
        if len(new_line[i].split(',')) == 2:
            darg_zero.append(new_line[i])
            index_num.append(i)
    for index in index_num:
        new_line.pop(index)

    # add 0 at last of each line
    new_line_final = []
    for line in new_line:
        line += ',0'
        line = line.replace('.jpg,', '.jpg ')
        new_line_final.append(line)
    # add root path for final_list
    final_list = []
    for line in new_line_final:
        all_str = line.split(' ')  # type(list)
        head = all_str[0]          # type(string)
        # convert type str.float to float to int to str
        new_str_body = []
        body = reduce(lambda x, y: x+y, [line+' ' for line in all_str[1:]])
        head_str = home_root + head
        new_line = head_str + ' ' + body
        final_list.append(new_line)

    # write the train.txt without no car file
    with open(root_path+train_middle_path, 'w') as output_file:
        for line in final_list:
            output_file.write(line)
            output_file.write('\n')











