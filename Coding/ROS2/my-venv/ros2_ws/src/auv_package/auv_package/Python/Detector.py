import cv2
import sys
import time
from Functions_For_Detector import differentThresholds, ShapeAddToImage, ColourAddToImage, colour, connections, show


def main():
	start_time = time.time()
	img = cv2.imread("test_image_8.jpeg")
	sys.setrecursionlimit(img.shape[0]*img.shape[1])
	obj = VisionDetector()
	# for a in range(img.shape[0]):
	# 	for b in range(img.shape[1]):
	# 		print(f"img[{a}][{b}]: {img[a][b]}")
	colours_detected = obj.colour_detector(img)
	# show(colours_detected)
	print(f"height: {img.shape[0]} width: {img.shape[1]}")
	shapes_detected = obj.shape_detector(img, colours_detected)
	end_time = time.time()
	print(f"Total time: {end_time - start_time}")
	# print(shapes_detected)
	cv2.imshow("hmm", img)
	cv2.waitKey(0)



class VisionDetector:
	def __init__(self):
		pass

	def colour_detector(self, image):
		height = image.shape[0]
		width = image.shape[1]
		used = []
		temp = []
		for a in range(width):
			temp.append(False)
		for a in range(height):
			used.append(temp.copy())
		temp = []
		colours = {"White": set(), "Red": set(), "Green": set(), "Blue": set(), "Yellow": set(), "Cyan": set(), "Purple": set(), "Gray": set(), "Black": set(), "Unknown": set()}
		sum_x = sum_y = counter = i = j = p = q = mid_x = mid_y = total = 0
		while i < height:
			j = 0
			while j < width:
				if used[i][j]:
					if j == width - 1 and i == height - 1:
						break
					else:
						j += 1
					continue
				sum_x = sum_y = counter = 0
				colourPrimary = colour(image[i, j])
				connections(image, used, temp, i, j, colourPrimary)
				total += len(temp)
				if 900*len(temp) >= height*width:
					for string in temp:
						p = int(string.split(", ")[0])
						q = int(string.split()[1])
						sum_x += q
						sum_y += p
						counter += 1
					mid_x = sum_x // counter
					mid_y = sum_y // counter
					ColourAddToImage(image, colours, image[i, j], mid_x, mid_y)
				temp = []
				j += 1
			i += 1
		print(f"left pixels: {(height*width - total)}")
		return colours

	def shape_detector(self, image, colours):
		counter = -1
		finalThreshold = differentThresholds(image)
		# cv2.imshow("FT", finalThreshold)
		shapes = set()
		contours, hierarchy = cv2.findContours(finalThreshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for contour in contours:
			counter += 1
			approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
			weights = cv2.moments(contour)
			if weights['m00'] != 0.0 and 900*weights['m00'] >= image.shape[0]*image.shape[1] and 0.9 >= weights['m00']/(image.shape[0]*image.shape[1]):
				center_x = int(weights['m10']/weights['m00'])
				center_y = int(weights['m01']/weights['m00'])
			else:
				continue
			if hierarchy[0][counter][3] != -1:
				if 0.7 <= weights['m00']/cv2.moments(contours[hierarchy[0][counter][3]])['m00']:
					continue
			cv2.drawContours(image, approx, -1, (0, 0, 0), 3)
			colour = ""
			for availableColours in ["White", "Red", "Green", "Blue", "Yellow", "Cyan", "Purple", "Gray", "Black"]:
				for coord in colours[availableColours]:
					if abs(coord[0] - center_x) <= image.shape[1] / 30 and abs(coord[1] - center_y) <= image.shape[0] / 30:
						colour = availableColours
			if len(approx) != 2:
				ShapeAddToImage(image, approx, colour, shapes, center_x, center_y)
		return shapes

if __name__ == "__main__":
	main()
