from PIL import Image
import numpy as np


def average_gray(arr, p_s, gr, i, j):
    """
    Возвращает усредненный оттенок серого для одного пикселя массива arr размера p_s с числом градаций gr
    :param arr: исходный массив, полученный из картинки
    :param p_s: размер одного элемента мозаики
    :param gr: число градаций серого
    :param i: координата по ширине с которой начинаем усреднение цвета
    :param j: координата по длине с которой начинаем усреднение цвета
    :return: усредненный цвет пикселя с учетом числа градаций серого
    >>> average_gray(np.array([[[1, 56, 3], [23, 54, 6]], [[4, 87, 67], [102, 36, 91]]]), 1, 5, 0, 0)
    20
    """
    average = np.sum(arr[i: i + p_s, j: j + p_s]) // (p_s ** 2 * 3)
    average -= average % gr
    return average


def transform_to_mosaic(arr, p_s, gr):
    """
    Трансформирует исходный массив пикселей, полученный из картинки в массив пикселей с усредненным серым цветом
    для каждых p_s пикселей и числом градаций серого gr
    :param arr: исходный массив, полученный из картинки
    :param p_s: размер одного элемента мозаики
    :param gr: число градаций серого
    :return: массив пикселей с p_s шириной пикселей одного цвета
    """
    for i in range(0, len(arr), p_s):
        for j in range(0, len(arr[1]), p_s):
            average = average_gray(arr, p_s, gr, i, j)
            arr[i: i + p_s, j: j + p_s] = np.full(3, average)
    return arr


def main():
    file_name = input("Введите имя файла который хотите преобразовать в мозаику: ").strip()
    res_name = input("Введите имя файла в который будет записан результат преобразования: ").strip()
    pixel_size = int(input("Введите размер одного элемента мозаики: "))
    gray_gradation = 255 // int(input("Введите число градаций серого:"))
    img = Image.open(file_name)
    img_arr = np.array(img)
    img_arr = transform_to_mosaic(img_arr, pixel_size, gray_gradation)
    res = Image.fromarray(img_arr)
    print("Преобразование завершено... Результат записан в файл \"" + res_name + "\"")
    res.save('res.jpg')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
