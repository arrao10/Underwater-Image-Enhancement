import cv2
import numpy as np
from tensorflow.keras.utils import Sequence
from random import shuffle

class Generator(Sequence):
    def __init__(self,images,batch_size):
        self.image_set = images
        self.batch_size = batch_size
        self.len = int(np.ceil(len(self.image_set)/self.batch_size))

    def __len__(self):
        return int(self.len)

    def __getitem__(self, idx):
        y = []
        x = []
        current_list = self.image_set[int(idx * self.batch_size): int((idx + 1) * self.batch_size)]
        for img in current_list:
            image = cv2.imread(img)
            alpha = 2.0 + (1.63 - 1.5) * np.random.random()
            beta = -1.5 + (1.8 + 1.6) * np.random.random()     

            #alpha = 0.3 + (2.0-0.3)*np.random.random()
            #beta = 12.0 + (1.0+1.0)*np.random.random()
            image = cv2.convertScaleAbs(image,alpha = alpha,beta = beta*50)
            image = np.divide(image,255.0)
            x.append(image)
            y.append(np.asarray([1.0/alpha,-beta/alpha]).reshape(1,1,2))

        return np.asarray(x), np.asarray(y)

    def on_epoch_end(self):
        shuffle(self.image_set)
