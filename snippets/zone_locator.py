"""
Use this script to display an image and show co-ordinates of mouse clicks.
Note that locations are relative to the form boundary,
not the corner of the image.

The boundary is identified first, and its corner co-ordinates are
subtracted from the mouse locations.

This means that Zones can be easily identified
by clicking on top-left and bottom-right corners
"""

import cv2

scale = 0.2
color1 = (0, 0, 255)
color2 = (0, 255, 0)
thickness = 5
# Target areas
x1, y1 = 600, 75


# Mouse callback function to display the coordinates of the mouse click,
# relative to form boundary
def mouse_callback(event, mouse_x, mouse_y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse coordinates: x={mouse_x/scale - x}, y={mouse_y/scale - y}")


# Load the scanned image
image = cv2.imread(r'..\images\form.tif')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (11, 11), 50)

# Threshold the image to create a binary mask
_, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary mask
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Contours', len(contours))
# input('stop')

contours = sorted(contours, key=cv2.contourArea, reverse=True)
# Filter out small contours
min_contour_area = 10
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

form_contour = filtered_contours[0]

x, y, w, h = cv2.boundingRect(form_contour)
print(x, y, w, h)
# Outer outer_boundary
cv2.rectangle(image, (x, y), (x + w, y + h), color1, thickness)

# Scale down the image to 25% of its original size
scaled_image = cv2.resize(image, None, fx=scale, fy=scale)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

cv2.imshow('Image', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


