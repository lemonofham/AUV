import math
import cv2
import numpy as np

def show(colours):
	for colour in ["White", "Red", "Green", "Blue", "Yellow", "Cyan", "Purple", "Gray", "Black", "Unknown"]:
		if len(colours[colour]) != 0:
			print(f"{colour}: {colours[colour]}")

def neighbours(height, width, p, q):
	neighbour = []
	if p == 0:
		if q == 0:
			neighbour.append((0, 1))
			neighbour.append((1, 0))
			neighbour.append((1, 1))
		elif q == width - 1:
			neighbour.append((0, q - 1))
			neighbour.append((1, q - 1))
			neighbour.append((1, q))
		else:
			neighbour.append((0, q - 1))
			neighbour.append((0, q + 1))
			neighbour.append((1, q - 1))
			neighbour.append((1, q))
			neighbour.append((1, q + 1))
	elif p == height - 1:
		if q == 0:
			neighbour.append((p - 1, 0))
			neighbour.append((p - 1, 1))
			neighbour.append((p, 1))
		elif q == width - 1:
			neighbour.append((p - 1, q - 1))
			neighbour.append((p - 1, q))
			neighbour.append((p, q - 1))
		else:
			neighbour.append((p - 1, q - 1))
			neighbour.append((p - 1, q))
			neighbour.append((p - 1, q + 1))
			neighbour.append((p, q - 1))
			neighbour.append((p, q + 1))
	else:
		if q == 0:
			neighbour.append((p - 1, 0))
			neighbour.append((p - 1, 1))
			neighbour.append((p, 1))
			neighbour.append((p + 1, 0))
			neighbour.append((p + 1, 1))
		elif q == width - 1:
			neighbour.append((p - 1, q - 1))
			neighbour.append((p - 1, q))
			neighbour.append((p, q - 1))
			neighbour.append((p + 1, q - 1))
			neighbour.append((p + 1, q))
		else:
			neighbour.append((p - 1, q - 1))
			neighbour.append((p - 1, q))
			neighbour.append((p - 1, q + 1))
			neighbour.append((p, q - 1))
			neighbour.append((p, q + 1))
			neighbour.append((p + 1, q - 1))
			neighbour.append((p + 1, q))
			neighbour.append((p + 1, q + 1))
	return neighbour

def colour(pixel):
	b = int(pixel[0])
	g = int(pixel[1])
	r = int(pixel[2])
	if abs(b - g) <= 20 and abs(g - r) <= 20 and abs(r - b) <= 20:
		if min(b, g, r) >= 150:
			return "White"
		else:
			return "Black"
	if b - r >= 50 and g - r >= 50:
		if g - b >= 50:
			return "Green"
		elif b - g >= 50:
			return "Blue"
		return "Cyan"
	if g - b >= 50 and r - b >= 50:
		if g - r >= 50:
			return "Green"
		elif r - g >= 50:
			return "Red" 
		return "Yellow"
	if r - g >= 50 and b - g >= 50:
		if r - b >= 50:
			return "Red"
		elif b - r >= 50:
			return "Blue"
		return "Purple"
	if r - g >= 20 and r - b >= 20:
		return "Red"
	if g - b >= 20 and g - r >= 20:
		return "Green"
	if b - r >= 20 and b - g >= 20:
		return "Blue"
	return "Unknown"

def approxLength(length1, length2):
	if 0.95 <= length1/length2 <= 1.05:
		return True
	return False

def parallel(slope1, slope2):
	if (slope1 == math.inf and slope2 == math.inf) or abs(slope1 - slope2) <= 0.1:
		return True
	return False

def perpendicular(slope1, slope2):
	if (slope1 == math.inf and abs(slope2) <= 0.1) or (slope2 == math.inf and abs(slope1) <= 0.1) or (-1.1 <= slope1*slope2 <= -0.9):
		return True
	return False

def differentThresholds(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# thresholded_image = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
	# canny = cv2.Canny(image, 50, 100)
	# cv2.imshow("C", canny)
	# lap = cv2.Laplacian(gray, cv2.CV_64F)
	# lap = np.uint8(np.absolute(lap))
	# cv2.imshow("L", lap)
	# sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
	# sobelx = np.uint8(sobelx)
	# sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
	# sobely = np.uint8(sobely)
	# sobel = cv2.bitwise_or(sobelx, sobely)
	# sobel = np.uint8(sobel)
	# cv2.imshow("SX", sobelx)
	# cv2.imshow("SY", sobely)
	# cv2.imshow("S", sobel)
	adapted_thresholded_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
	return adapted_thresholded_image

def quad(points):
	if points[0][0][0] - points[1][0][0] != 0:
		slope1 = (points[0][0][1] - points[1][0][1])/(points[0][0][0] - points[1][0][0])
		if abs(slope1) >= 6:
			slope1 = math.inf
	else:
		slope1 = math.inf
	if points[1][0][0] - points[2][0][0] != 0:
		slope2 = (points[1][0][1] - points[2][0][1])/(points[1][0][0] - points[2][0][0])
		if abs(slope2) >= 6:
			slope2 = math.inf
	else:
		slope2 = math.inf
	if points[2][0][0] - points[3][0][0] != 0:
		slope3 = (points[2][0][1] - points[3][0][1])/(points[2][0][0] - points[3][0][0])
		if abs(slope3) >= 6:
			slope3 = math.inf
	else:
		slope3 = math.inf
	if points[3][0][0] - points[0][0][0] != 0:
		slope4 = (points[3][0][1] - points[0][0][1])/(points[3][0][0] - points[0][0][0])
		if abs(slope4) >= 6:
			slope4 = math.inf
	else:
		slope4 = math.inf
	length1 = math.sqrt((points[0][0][1] - points[1][0][1])**2 + (points[0][0][0] - points[1][0][0])**2)
	length2 = math.sqrt((points[1][0][1] - points[2][0][1])**2 + (points[1][0][0] - points[2][0][0])**2)
	length3 = math.sqrt((points[2][0][1] - points[3][0][1])**2 + (points[2][0][0] - points[3][0][0])**2)
	length4 = math.sqrt((points[3][0][1] - points[0][0][1])**2 + (points[3][0][0] - points[0][0][0])**2)
	if parallel(slope1, slope3) or parallel(slope2, slope4):
		if approxLength(length1, length3):
			if approxLength(length2, length4):
				if perpendicular(slope3, slope4):
					if approxLength(length2, length1):
						return "Square"
					else:
						return "Rectangle"
				else:
					if approxLength(length2, length1):
						return "Rhombus"
					else:
						return "Parallelogram"
			else:
				if perpendicular(slope1, slope2) or perpendicular(slope3, slope4):
					return "Non-Isoceles Trapezium"
				else: 
					return "Isoceles Trapezium"
		else:
			if approxLength(length2, length4):
				if perpendicular(slope1, slope2) or perpendicular(slope3, slope4):
					return "Non-Isoceles Trapezium"
				else:
					return "Isoceles Trapezium"
			else:
				return "Non-Isoceles Trapezium"
	else:
		return "Quadrilateral"

def detect_figure(points, COM_x, COM_y):
	lengths = []
	circle = True
	for i in range(len(points)):
		lengths.append(math.sqrt((COM_x - points[i][0][0])**2 + (COM_y - points[i][0][1])**2))
	if not approxLength(lengths[len(points) - 1],lengths[0]):
		circle = False
	for i in range(len(points) - 1):
		if not approxLength(lengths[i+1], lengths[i]):
			circle = False
	if circle:
		return "Circle"
	else:
		change = []
		increasing = True
		decreasing = True
		if lengths[0] > lengths[len(points) - 1]:
			decreasing = False
		else:
			increasing = False
		for i in range(len(points) - 1):
			if lengths[i+1] > lengths[i] and decreasing:
				increasing = True
				decreasing = False
				change.append(i)
			elif lengths[i] > lengths[i+1] and increasing:
				decreasing = True
				increasing = False
				change.append(i)
		if len(change) == 4:
			if abs(change[0] - change[2]) <= 0.6*len(points) and abs(change[1] - change[3]) <= 0.6*len(points):
				return "Ellipse"
			else:
				return "Non Standard Figure"
		else:
			return "Non Standard Figure"

def connections(image, used, temp, i, j, compareColour):
	if used[i][j]:
		return
	else:
		used[i][j] = True
		temp.append(f"{i}, {j}")
	for coord in neighbours(image.shape[0], image.shape[1], i, j):
		if used[coord[0]][coord[1]]:
			continue
		if colour(image[coord[0]][coord[1]]) == compareColour:
			connections(image, used, temp, coord[0], coord[1], compareColour)
	return

def ShapeAddToImage(image, approx, colour, shapes, center_x, center_y):
	cv2.putText(image, "Shape: ", (center_x - 60, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	cv2.putText(image, "Colour: ", (center_x - 60, center_y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	match len(approx):
		case 3:
			shapes.add("Triangle")
			cv2.putText(image, "Triangle", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 4:
			type_of_quad = quad(approx)
			shapes.add(type_of_quad)
			cv2.putText(image, type_of_quad, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 5:
			shapes.add("Pentagon")
			cv2.putText(image, "Pentagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 6:
			shapes.add("Hexagon")
			cv2.putText(image, "Hexagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 7:
			shapes.add("Septagon")
			cv2.putText(image, "Septagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 8:
			shapes.add("Octagon")
			cv2.putText(image, "Octagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 9:
			shapes.add("Nonagon")
			cv2.putText(image, "Nonagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
		case 10:
			shapes.add("Decagon")
			cv2.putText(image, "Decagon", (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2) 
		case _:
			figure = detect_figure(approx, center_x, center_y)
			shapes.add(figure)
			cv2.putText(image, figure, (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	if colour != "":
		cv2.putText(image, colour, (center_x, center_y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	else:
		cv2.putText(image, "Unknown", (center_x, center_y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

def ColourAddToImage(img, colours, pixel, mid_x, mid_y):
	b_mid = int(img[mid_y, mid_x][0])
	g_mid = int(img[mid_y, mid_x][1])
	r_mid = int(img[mid_y, mid_x][2])
	text_colour = (255 - b_mid, 255 - g_mid, 255 - r_mid)
	detectedColour = colour(pixel)
	colours[detectedColour].add((mid_x, mid_y))
	# cv2.putText(img, detectedColour, (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_colour, 2)