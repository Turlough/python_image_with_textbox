

class BreedZones:
    tl = (2851, 230)
    br = (3846, 2750)
    top = tl[1]
    left = tl[0]
    right = br[1]
    padding = 10

    def __init__(self):
        height = self.br[1] - self.tl[1]
        self.height = int(height/8)

    def get_rectangle(self, index: int):
        top = self.height * index
        bottom = self.height * (index + 1)
        tl = (self.left, self.top + top + self.padding)
        br = (self.right, self.top + bottom - self.padding)
        return tl, br
