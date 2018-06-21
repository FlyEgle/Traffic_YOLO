"""
convert file float to int
"""
from functools import reduce


def get_changeable_result(old_file_line):
    """
    :param old_file_line: no change float to int
    :return: get the new and final line of file change th e float to int and the type(list)
    """
    line_1 = old_file_line[1:-1]  # get the each line body not image_path and '/n'
    new_line_1 = []               # generate a new list for append convert float to int
    for index in range(len(line_1)):
        try:
            new_line_1.extend([str(int(float(x))) for x in line_1[index].split(',')])
        except Exception as e:
            # print(new_line_1, 'image_path:{}'.format(old_file_line[0]), e)
            pass
    # print(new_line_1)

    new_new_line = []
    for s_index in range(len(new_line_1)):
        if (s_index + 1) % 5 == 0:
            new_new_line.append(
                    new_line_1[s_index - 4] + ',' + new_line_1[s_index - 3] + ',' + new_line_1[s_index - 2] + ',' +
                    new_line_1[s_index - 1] + ',' + new_line_1[s_index])

    final_line = [old_file_line[0]]
    final_line.extend(new_new_line)
    # get the final result
    return final_line


if __name__ == '__main__':
    path = 'D:/DataSet_raccon/jiaotong_traffic/train_1w_not_drop_0.txt'
    with open(path, 'r') as f:
        file_list = []
        for line in f:
            file_list.append(line)

    # get the split from space str line
    new_file_list = []
    for line in file_list:
        new_file_list.append([l for l in line.split(' ')])

    final_file = []
    for line in new_file_list:
        changable_list = get_changeable_result(line)
        head = changable_list[0]
        try:
            body = reduce(lambda x, y: x+y, [line + ' ' for line in changable_list[1:]])
        except Exception as e:
            print(head, e)
        new_line = head + ' ' + body
        final_file.append(new_line)
        # print(new_line)

    with open('D:/DataSet_raccon/jiaotong_traffic/new_change.txt', 'w') as f:
        for line in final_file:
            f.write(line)
            f.write('\n')


