from cv2 import imread, imwrite, imshow, waitKey, IMREAD_GRAYSCALE
import math


image = imread('zebras.jpg', IMREAD_GRAYSCALE)
image_result = image.copy()
image_pixels = image.shape[0] * image.shape[1]


# Составление гистограммы
hist = []

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):

        hist[image[i][j]] += 1


# Нормализация гистограммы
hist_normalised = []

for i in range(0, len(hist)):

    hist_normalised[i] = hist[i] / image_pixels


# Среднеарифметический фильтр, апертура 3х3
aperture_shape = 9
k = 1.3

for i in range(1, image.shape[0] - 2):
    for j in range(1, image.shape[1] - 2):

        mean_value = 0

        for di in range(-1, 2):
            for dj in range(-1, 2):

                pixel = image[i + di][j + dj]
                mean_value += pixel * hist_normalised[pixel]

        dispersion = 0

        for di in range(-1, 2):
            for dj in range(-1, 2):

                pixel = image[i + di][j + dj]
                dispersion += ((pixel - mean_value) ** 2) * hist_normalised[pixel]

        mean_square_deviation = math.sqrt(dispersion)
        z_threshold = k * mean_square_deviation

        mean_pixels = 0
        mean_pixels_len = 0

        for di in range(-1, 2):
            for dj in range(-1, 2):

                if abs(image[i + di][j + dj] - mean_square_deviation) < z_threshold:

                    mean_pixels += image[i + di][j + dj]
                    mean_pixels_len += 1

        mean_pixels = mean_pixels / mean_pixels_len


# imshow('result', image_result)
# waitKey(0)
# imwrite('zebras-result.jpg', image_result)


# Сигма-фильтр, апертура 3х3

