from PIL import Image
import numpy as np
import time
MAD_target = []


def compare(target, compare):
    count = 0
    for i in range(16):
        for j in range(16):
            count += int(compare[0][i][j]) - int(target[i][j])
    return count


def sequential_search(reference_arr):
    vector =[]
    x, y = 0, 0
    start = time.time()
    end = time.time()
    for ma in MAD_target:
        min = 9999999
        for i in range(-31, 31):
            for j in range(-31, 31):
                # 使用一個範圍去搜尋
                temp = compare(parseblock(np.asarray(reference_arr), (ma[1]+j), (ma[2]+i)), ma[0])
                if temp < min:
                    min = temp
                    x = j
                    y = i
        vector.append([y, x])
    end = time.time()
    use_time = (end - start)
    print('花費時間 :', use_time)
    print('比較次數 :', 63*63*len(MAD_target))
    return vector


def logarithmic_search(reference_arr):
    vector = []
    x, y = 0, 0
    start = time.time()
    end = time.time()
    for ma in MAD_target:
        min = 9999999
        
    end = time.time()
    use_time = (end - start)
    print('花費時間 :', use_time)
    print('比較次數 :', 63 * 63 * len(MAD_target))
    return vector

def openfile():
    # 開啟圖檔
    try:
        i1 = Image.open('i1.jpg')
        i2 = Image.open('i2.jpg')
    except FileNotFoundError:
        print("找不到此檔案!")
        exit(0)

    # 轉成灰階
    i1 = i1.convert("L")
    i2 = i2.convert("L")
    # 轉成矩陣
    target_arr = np.asarray(i1).copy()
    reference_arr = np.asarray(i2).copy()

    # 分割出Block Reference
    for i in range(0, i1.size[0], 16):
        for j in range(0, i1.size[1], 16):
            ss = []
            ss.append(parseblock(target_arr, j, i))
            MAD_target.append([ss, i, j])
    return i2


def parseblock(arr=[], startx=0, starty=0):
    tar_arr = arr.copy()
    mat = []
    for k in range(startx, startx+16):
        a = []
        for l in range(starty, starty+16):
            if k >= len(tar_arr):
                k -= len(tar_arr)
            if l >= len(tar_arr[k]):
                l -= len(tar_arr[k])
            a.append(tar_arr[k][l])
        mat.append(a)
    return mat


if __name__ == '__main__':
    reference_arr = openfile()
    vec_seq = sequential_search(reference_arr)




