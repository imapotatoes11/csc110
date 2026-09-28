import numpy as np
from PIL import Image
from picture import pic

# Show the original picture. No edits are required here.
#img = Image.fromarray(np.array(pic, dtype=np.uint8))
#img.show()
arr = np.array(pic, dtype=np.uint8)

average = lambda a,b,c: (a + b + c) // 3
#average = lambda a,b,c: int((a*b*c) ** (1/3))
arr = np.array([[[average(i,j,k), average(i,j,k), average(i,j,k)] for i,j,k in row] for row in arr], dtype=np.uint8)

#arr.sort()
img = Image.fromarray(arr)
img.show()

# ToDo: Answer the following questions
    # 1. The image data is stored in a variable called "pic". What is the structure of this variable?
    # 2. What is meant by "convert an image to gray scale"? Is there only one way to do it?
    # 3. Trace the entire starting code carefully. Where is the picture data originating?


# ToDo convert image to Grayscale without using built-in functions.


# Reshow pic now that it has been converted to grayscale.
print("Display the new gray scale image")
img = Image.fromarray(np.array(pic, dtype=np.uint8))
img.show()

# ToDo: Answer the following questions after you've implemented the grayscale conversion
    # 1. Calculate how many total iterations did Python perform. How can you verify this value
    # 2. How much smaller should the grayscale image file be compared to the full colour version?
    # 3. If you were only given a grayscale image, could you convert it back to colour?
    # 4. Explore other methods of grayscale conversion to see how they impact the final image.
    # 5. Create a new variable "method" that lets you choose grayscale computation methods. For example "average".
    #       Note: you will have to also modify your nested loops accordingly to accommodate the user's selection.
