# Imagezen

The image generator takes in image as input and generates multiple derivative images by using various image transformation and distortion algorithms. I used the OpenCV library for the transformation and distortion of images. The user selects a set of transformation functions and distortion algorithms and give any required parameters.

# Run the applicttion

To run the application you need to download the source code files, edit use an input text file to define the function names and images to be used. This input file and the images need to be in the same folder and the source code.

# Input
### Text File
The user will input a text file thet is in a required format.
The following is an example of input text file.

>image: sc1.jpg && sc2.png && sc3.jpg
>num_filters: all
>rotateFromCenter: 10 && 20 && 30 && 180 && 170 && 160
>translatoion: [[1,0,100],[0,1,50]]
>affine: [[50,50],[200,50],[50,200]] & [[10,100],[200,50],[100,250]]
>threshBinaryInv: 127 & 255
>adaptiveMean: 255 & 11 & 2 && 255 & 9 & 2
>adaptiveGaussian: 255 & 11 & 2
>threshOtsu: 255
>bilateriaBlur:
>cannyEdge:

In the above example of the test file, you can see that the first work in each line will be an attribute. 
- The first line contains image names which says "image:" then the list of image names are given saparated with "&&".
- The second line contains the number of functions/filters to be used in each combination (i.e. the number of filters to be used in each output image). If all possible combination is to be used then the used can define it as "all".
- From the third line an on the text file must contain the list of all functions with its oparamaters. If the function takes more then one paramater then the parameters must be seperated with a "&". There are some functions which do not take any pparameters, they are left blank. 
- If the user wants to use the same function more then once, with a different parameter, the user can add more paramerets in the same line saparated with "&&". In the above example text file the function rotateFromCenter takes in only one parameter but is being used 6 different times with 6 diffewrent parameters. Another examople is adaptiveMean fiunctin which takes 3 parameters, here this function is being used twice by giving 2 levels of parameters, firstly 255 & 11 & 2 and secondly 255 & 9 & 2. This way many level parameter can be passes untill and unless they are different.

> Do check out the file, function defination, which contains all the function names with the parameters it needs.

# Add your own image filter/transformation/distortation function 

Your own function can be added to the file "filters.py". Make sure you import all the dependencies that are not there. To use the function that you added, you can add its name to the input text file with the parameters it needs in the format defined above. 
To add your own function in this application first you need to understand the standards of the functions used in this application. They are:
- All the functions must exactly use 2 paramaters. (img, val)
- The first parameter "img" is the image name that is passed to the function.
- The second "val" is an array of string which contains all the values the function needs as  parameter.
- Below is an example of a function which contains a single value in the paramater "val"

```sh
def rotateFromCenter(img, val):
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),int(val),1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst
```

- Below is another example function, but ths function needs multiple values to be passed as parameter, so we hve the paramater "val" as an array of strings that contains all the parameter values that this function needs.

```sh
def adaptiveMean(img,val): 
    val = val.split('&')
    maxValue = int(val[0])
    blockSize = int(val[1])
    C = int(val[2])
    img = cv2.medianBlur(img,5)
    dst = cv2.adaptiveThreshold(img,maxValue,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,blockSize,C)
    return dst
```
