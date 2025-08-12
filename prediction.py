from model import GEN
import cv2
import numpy as np
from sewar import full_ref
from skimage import metrics

def process(path):
	model = GEN()
	model.model.load_weights('tr.h5')
	image = cv2.imread(path)
	image = cv2.resize(image,(256,256))
	image = np.divide(image,255.0)
	image = np.expand_dims(image,axis=0)
	pred = model.model.predict(image)
		
	#Last
	alpha = min(pred[0][0][0][0] * 1.5 + 0.95, 1.5689420402050019)
	beta = max(pred[0][0][0][1] * 0.5 - 1.5, -1.4790416579246521)
	
	#option
	#alpha = min(pred[0][0][0][0] * 1.2 + 1.1, 1.843972110748291)
	#beta = max(pred[0][0][0][1] * 0.3 - 1.8, -1.766176199913025)

	print("Alpha = ", alpha)
	print("Beta = ", beta)
	image = cv2.imread(path)
	image = cv2.resize(image,(512,512))
	pred = cv2.convertScaleAbs(image,alpha = alpha,beta = beta*50)

	psnr_img=full_ref.psnr(image, pred, MAX=None)
	print("PSNR: Peak Signal-to-Noise Ratio = ", psnr_img)

	ssim_img = full_ref.ssim(image, pred, ws=11, K1=0.01, K2=0.03, MAX=None, fltr_specs=None, mode='valid')
	print("SSIM: Structural Similarity Index = ", ssim_img)
	
	cv2.imshow('Result Image',pred)
	cv2.imshow('Original Image',image)
	cv2.waitKey(0)
	cv2.imwrite('Result Image.jpg',pred)