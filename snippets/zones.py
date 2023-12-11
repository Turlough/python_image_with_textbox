

class BreedZones:
    tl = (2851, 230)
    br = (3846, 2750)
    top = tl[1]
    bottom = br[1]
    left = tl[0]
    right = br[0]
    padding = 40

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
        return tl, br
