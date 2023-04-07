import os
import cv2
import copy
from PIL import ImageFont, ImageDraw, Image
import numpy as np

#a1=""
a = input("Choose a font:"+"\n"+"1.Aldrich-Regular.ttf")
if a == "1":
     a1 = "Aldrich-Regular.ttf"


b = input("What size will the text be")
x = input("X coordinate")
y = input("Y coordinate")

img = cv2.imread('00_00.png')
img = cv2.resize(img, (1600, 900))
for hour in range(24):
    for minutes in range(60):
         new_img = copy.deepcopy(img)

         time_text = str(hour).zfill(2)  + ":" + str(minutes).zfill(2)
         # time_text = "01" + ":" + str(minutes).zfill(2)
         print (time_text)

         # font = cv2.FONT_HERSHEY_SIMPLEX
         # bottomLeftCornerOfText = (130, 175)
         # fontScale = 4
         # fontColor = (128, 128, 128)
         # thickness = 5
         # lineType = 100
         #
         # cv2.putText(new_img, time_text,
         #     bottomLeftCornerOfText,
         #     font,
         #     fontScale,
         #     fontColor,
         #     thickness,
         #     lineType)

         fontpath = a1
         font = ImageFont.truetype(fontpath, int(b))
         img_pil = Image.fromarray(img)
         draw = ImageDraw.Draw(img_pil)
         draw.text((int(x), int(y)),time_text, font=font, fill=(255, 255, 255, 0))
         new_img = np.array(img_pil)

         filename = time_text.replace(":", "_") + ".png"
         cv2.imwrite(os.path.join("images", filename), new_img)

# cv2.imshow("123", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
