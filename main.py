from cli import LatexOCR
from PIL import Image

img = Image.open(r'test_img/3.png')
model = LatexOCR()
print(model(img))