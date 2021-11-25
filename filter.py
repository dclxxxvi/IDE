from PIL import Image
import numpy as np


def pixel_brightness(arr, p_s, gr, i, j):
    '''
    Возвращает оттенок серого одного пикселя

    '''
    brightness = np.sum(arr[i: i + p_s, j: j + p_s]) // (p_s ** 2 * 3)
    brightness -= brightness % gr
    return brightness


def transform_to_mosaic(arr, p_s, gr):
    for i in range(0, len(arr), p_s):
        for j in range(0, len(arr[1]), p_s):
            brightness = pixel_brightness(arr, p_s, gr, i, j)
            arr[i: i + p_s, j: j + p_s] = np.full(3, brightness)


file_name = input("Введите имя файла который хотите преобразовать в мозаику: ").strip()
res_name = input("Введите имя файла в который будет записан результат преобразования: ").strip()
pixel_size = int(input("Введите размер одного элемента мозаики: "))
gray_gradation = 255 // int(input("Введите число градаций серого:"))
img = Image.open(file_name)
img_arr = np.array(img)
transform_to_mosaic(img_arr, pixel_size, gray_gradation)
res = Image.fromarray(img_arr)
print("Преобразование завершено... Результат записан в файл \"" + res_name + "\"")
res.save('res.jpg')
