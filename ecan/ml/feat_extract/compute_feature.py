from PIL import Image
from skimage.feature import hog
import numpy as np
import matplotlib.pyplot as plt

def compute_hog(sample):
    d = {
        'cells_per_block': (1, 1),
        'orientations': 8,
        'pixels_per_cell': (12, 12),
        'normalise': True,
        'visualise': False
    }
    name = 'hog_032415'
    img = sample.im.path.encode('ascii', 'replace')
    img = Image.open(img).convert('L')
    img = np.array(img)
    ft = hog(img, **d)

    # ft, hogimg = hog(img, **d)
    # nrow, ncol = img.shape
    # xsize = 10.
    # ysize = xsize*float(nrow)/float(ncol)
    # fig5, ax5 = plt.subplots(1,2,num=5,figsize=[xsize,ysize/2.])
    # [i.axis('off') for i in ax5]
    # fig5.subplots_adjust(0,0,1,1,0,0)
    # im5a = ax5[0].imshow(img, cmap=plt.cm.gray)
    # im5b = ax5[1].imshow(hogimg, cmap=plt.cm.gray)
    # fig5.canvas.draw()
    # plt.show()
    # print ft
    return ft

def compute_thumb(sample):
    THUMBNAIL_SIZE = (80, 60)
    img = sample.im.path.encode('ascii', 'replace')
    img = Image.open(img).convert('L')
    img.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    ft = np.array(img).flatten()
    return ft
