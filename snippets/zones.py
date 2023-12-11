import cv2
import numpy as np


class BreedZones:
    tl = (2851, 230)
    br = (3846, 2750)
    top = tl[1]
    bottom = br[1]
    left = tl[0]
    right = br[0]
    padding = 0

    def __init__(self, left_offset, top_offset):
        self.left_offset = left_offset
        self.top_offset = top_offset
        height = self.bottom - self.top
        self.zone_height = int(height / 12)
        self.left += left_offset + self.padding
        self.right += left_offset - self.padding

    def get_rectangle(self, index: int):
        top = self.zone_height * index
        top += self.top_offset
        bottom = self.zone_height * (index + 1)
        bottom += self.top_offset

        tl = (self.left, self.top + top + self.padding)
        br = (self.right, self.top + bottom - self.padding)
        middle = (tl[0] + br[0]) / 2, (tl[1] + br[1]) / 2
        return tl, br, middle

    def find_ink_zones(self, image, index):
        tl, br, middle = self.get_rectangle(index)
        # expand the detection zone
        m = 10
        # Crop the image to the target zone
        cropped_image = image[tl[1] - m:br[1] + m, tl[0] - m:br[0] + m]

        cv2.namedWindow('Image')
        cv2.imshow('Image', cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Adjust the point coordinates to the cropped image
        point = (middle[0] - tl[0], middle[1] - tl[1])

        # Initialize minimum area and rectangle. Initially set to infinity.
        min_area = float('inf')
        rect = None

        # Check each contour to find the smallest bounding rectangle that encloses the point
        print('Number of contours:', len(contours))
        for contour in contours:
            if cv2.pointPolygonTest(contour, point, False) >= 0:
                rect = cv2.boundingRect(contour)
                area = rect[2] * rect[3]  # width * height
                print('Rectangle', rect, ', Area', area)
                if area < min_area:
                    min_area = area
                    rect = rect


        # Return the smallest rectangle, adjusting back to original image coordinates
        if rect is not None:
            # (x, y, w, h)
            rect = (rect[0] + tl[0], rect[1] + tl[1], rect[2], rect[3])
            # (x1, y1), (x2, y2)
            return (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3])
        return None, None
