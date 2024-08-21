# from cli import LatexOCR
# from PIL import Image
# import sys
# import os
# import time
# import matplotlib.pyplot as plt
#
#
# model = LatexOCR()
#
# image_path = "test_img/test/0000000.png"
# image = Image.open(image_path)
# latex_math = model(image)
#
# image.show()
#
# print(f"Mã LaTeX gốc: {latex_math}")
#
#
# # if __name__ == '__main__':
# #     folder_path = "test_img/test"
# #     start_time = time.time()
# #
# #
# #     image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
# #
# #     for image_file in image_files:
# #         image_path = os.path.join(folder_path, image_file)
# #         image = Image.open(image_path)
# #         latex_math = model(image)
# #
# #         image.show()
# #
# #         plt.figure()
# #         plt.text(0.5, 0.5, latex_math, fontsize=20, ha='center', va='center')
# #         plt.axis('off')
# #         plt.show()
# #
# #         print(f"Mã LaTeX gốc cho {image_file}: {latex_math}")
#
import matplotlib.pyplot as plt

latex_expression = r"$e^{i\pi}+1=0$"
fig = plt.figure(figsize=(10,10))  # Dimensions of figsize are in inches
text = fig.text(
    x=1,  # x-coordinate to place the text
    y=1,  # y-coordinate to place the text
    s=latex_expression,
    horizontalalignment="center",
    verticalalignment="center",
    fontsize=16,
)

plt.show()
