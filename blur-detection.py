# import the necessary packages
from imutils import paths
import argparse
import cv2
import sys
 
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in paths.list_images(args["images"]):
	# load the image, convert it to grayscale and put them into a argparse 
	# measure the focus of the image using laplacian tranform 
	# then we set up threshhold that is 100 at base and measure the images blurryness in argparse 
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)

	if fm > args["threshold"]:
		text = imagePath+" - Not Blurry: "+str(fm)
		print(imagePath+" - Not Blurry: "+str(fm))
 
	# a threshhold is applied and if image is less than that 
	# it is considered blurry 
	if fm < args["threshold"]:
		text = imagePath+" - Blurry: "+str(fm)
		print(imagePath+" - Blurry: "+str(fm))
