from PIL import Image
import matplotlib.pyplot as plt



if __name__ == '__main__':
    image_path = 'mem.jpg'

    img = Image.open(image_path)

    plt.imshow(img)
    plt.axis('off')
    plt.show()


