from PIL import Image
import random

random.random()
num = random.randint(0, 2)
def crop(boardsize):
    img = "" # 처음 불러오는 이미지
    cropimage = [] # 자른 이미지 저장 리스트
    #num = 2

    img = Image.open(fr'C:/Users/cwyi6/OneDrive/문서/python/sliding_puzzle/puzzle_image/picture{num}.jpg')
    tile_size = img.size[0] / boardsize

    for a in range(boardsize ** 2 - 1):
        x1 = tile_size * (a%boardsize)
        y1 = tile_size * (a//boardsize)
        x2 = tile_size * ((a%boardsize)+1)
        y2 = tile_size * ((a//boardsize)+1)
        cropping_area = (x1 ,y1 , x2, y2)
        cropimage.append(img.crop(cropping_area))
    return num, cropimage

# for i in range(boardsize):
    #    for j in range(boardsize):
     #       x1 = tile_size * i
     #       y1= tile_size * j
     #       x2 = (tile_size * i) + 1
     #       y2 = (tile_size * j) + 1
     #       cropping_area = (x1, y1, x2, y2)
     #       cropimage.append(img.crop(cropping_area))
    #return cropimage

#def cropimage(img_path):
 #   img = Image.open(img_path)