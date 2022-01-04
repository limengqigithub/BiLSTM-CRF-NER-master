# -*- coding:utf-8 -*-
# @Time   :2021/12/4 3:28 下午
# @Author :Bubble
# @FileName:统计信息代码.py
import numpy as np


def number_of_sentences(path):
    return len([1 for row in open(path, 'r', encoding='utf-8').readlines() if not row.strip()])


def max_min_mean_std(path):
    sentence_len = []  # 用来存储每个句子的长度
    sentence = []  # 句子暂存器
    with open(path, 'r', encoding='utf-8') as f:
        for row in f.readlines():  # 读取每一行
            if row.strip():
                # 在没遇到空字符之前把字逐一放进暂存器
                sentence.append(row.strip())
            else:
                # 遇到空字符，计算句子长度并保存，置句子暂存列表为空
                sentence_len.append(len(sentence))
                sentence = []
    sentence_len.append(len(sentence))  # 把最后一个句子的长度也考虑进来
    return max(sentence_len), min(sentence_len), np.std(sentence_len)


def get_labels(path):
    labels = set()  # 这里用集合来存储标签，起到去重复的作用
    with open(path, 'r', encoding='utf-8') as f:
        for row in f.readlines():  # 读取每一行
            if row.strip():  # 去掉每行的换行符
                labels.add(row.strip().split()[1])  # 把标签添加到集合中
    return f'一共有{len(labels)}个标签。', list(labels)  # 以列表的形式返回


def get_labels_num(path):
    label_to_num = {}
    f = open(path, 'r', encoding='utf-8')
    for row in f.readlines():  # 读取每一行
        if not row.strip(): continue  # 过滤空行
        label = row.strip().split()[1]  # 取出带有位置标识符的实体，
        if label.startswith('B') or label.startswith('S'):
            label = label.strip().split('-')[1]
            if label not in label_to_num:
                label_to_num[label] = 1
            else:
                label_to_num[label] += 1
    f.close()
    return label_to_num

def show_zhuzhuang(data):
    import matplotlib.pyplot as plt
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    waters = [d[0] for d in data.items()]
    buy_number = [d[1] for d in data.items()]
    plt.bar(waters, buy_number)
    plt.title('实体数量统计直方图')
    plt.show()


if __name__ == '__main__':
    train_path = 'ResumeNER/train.char.bmes'
    # train_dataset_number = number_of_sentences(train_path)
    # print(train_dataset_number)
    # print(max_min_mean_std(train_path))
    # print(len(get_labels(train_path)))
    # print(get_labels(train_path))
    # print(get_labels_num(train_path))
    # show_zhuzhuang(get_labels_num(train_path))
    print(range(10))