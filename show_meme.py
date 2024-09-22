from PIL import Image
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':
    img = Image.open('memes/meme1.jpg')
    
    plt.imshow(img)
    plt.axis('off')
    plt.show()