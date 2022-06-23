import cv2 as cv
import numpy as np

img=cv.imread("shishi.jpg")
gray=cv.imread("shishi.jpg", 0)

print("""
Please choose:
    1. Accept/load colored img. Grayscale should be rejected.
    2. Output a pixel value.
    3. Modify a pixel value.
    4. Set img dimensions. Within boundaries or not.
    5. Set img total pixel count. Higher or lower than the set pixel.
    6. Show the currently loaded image's data type.
""")

opt=int(input("input number: "))
if opt == 1 :
    imgshape = len(img.shape)
    grayshape = len(gray.shape)
    if imgshape > grayshape:
        cv.imshow("colored", img)
        cv.waitKey(0)
    else:
        exit()

elif opt == 2:
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    color = int(input("selection: \n 1. BLUE \n 2. GREEN \n 3. RED\ninput number: "))
    c=color-1
    print(img.item(x, y , c))


elif opt == 3:
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    print(img[x, y])
    for i in range(0, 3, 1):
        color = int(input("selection: \n 1. BLUE \n 2. GREEN \n 3. RED\ninput number: "))
        pixelValue = int(input("Pixel Value: "))
        c=color-1
        img.itemset((x, y, c), pixelValue)
    print(img[x, y])
    cv.imshow("colored", img)
    cv.waitKey(0)

elif opt == 4:
    x=450
    y=150
    print(img.shape)
    print(f"""
                Total pixel in x-axis: {img.shape[0]}
                Total pixel in y-axis: {img.shape[1]}
                Compared value in x-axis: {x}
                Compared value in y-axis: {y}
            """)

    if x <= img.shape[0] and y <= img.shape[1] :
        print("Within boundaries")
    else :
        print("Out of boundaries")

elif opt == 5:
    x=150
    y=150
    fixedValue=x * y
    totalPixel=img.shape[0] * img.shape[1]

    print(f"""
              Fixed variable: {fixedValue}
              Total pixels: {totalPixel}
            """)

    if fixedValue > totalPixel :
        print("Higher")
    elif fixedValue < totalPixel :
        print("Lower")
    else :
        print("Equal")

elif opt == 6:
    print(f"Image data type: {img.dtype}")

else:
    exit()