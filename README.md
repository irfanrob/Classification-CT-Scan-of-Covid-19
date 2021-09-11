# Classification-CT-Scan-of-Covid-19
 
The dataset that I used were from Iran researcher Mohammad Rahimzadeh. From the dataset that he shared, I took 1000 images that contain 500 infected Covid-19 images and 500 normal images. 

The dataset that I used is shared in this folder : https://drive.google.com/drive/folders/1sqKQh_Kbi7h8ao-u0TFmY5DST4lga36F?usp=sharing

The whole dataset can be seen here : https://github.com/mr7495/COVID-CTset

The raw images are 16-bit grayscale images in TIFF format and normal monitors cannot visualize the image clearly. According to Mohammad Rahimzadeh instruction, the dataset must be normalized first by converted it to float by dividing each image pixel value by the maximum pixel value of that image. By using this normalisation the images will be 32-bit float type pixel values which can be seen in normal monitors.

**Normalized**
![normalized](https://user-images.githubusercontent.com/75148994/132940711-90caf24b-3348-4e5e-87d6-976a868adb51.png)

After normalized the images, I added 2 preprocessing methods to these images which are gaussian filter and CLAHE. The gaussian filter can reduce the noise of the images, also detect the edge of the images. As for CLAHE, this method can improve the visibility level of the images.

**Gaussian filter**
![gaussian filter](https://user-images.githubusercontent.com/75148994/132940970-92b5c077-20a6-4fa6-a8ab-4e2d58725ab8.png)

**CLAHE**
![clahe](https://user-images.githubusercontent.com/75148994/132940986-5973669c-2416-433a-889a-dc6778306279.png)

In this project, I used AlexNet architecture with 5 optimizers which are SGD, Adadelta, RMSprop, Adam, and AdaMax. The learning rates that were used are 0.1, 0.001, and 0.0001. After the training process, I analyze and compare the accuracy, loss, and precision. 

The result of the project can be seen here : https://drive.google.com/drive/folders/1QoH7QBv56g0BoOm3jCDRbkFBTzQkwcEJ?usp=sharing

I also set the checkpoint for each training, so the best weight can be saved. With the best weight that I’ve got, I load it to the application prototype that I built so this application could detect the CT-Scan images whether is it Covid-19 or normal.

The book and journal unfortunately only available in Indonesian language, but the abstract of the book and journal is available in English language. The book and journal can be accessed below :

Book : https://drive.google.com/file/d/17dIDVaBaXrqnw1fjVp9M6_c92j_S2jau/view?usp=sharing

Journal : https://drive.google.com/file/d/1DgaX53oz2fSc3PSQw8Zg7eVcJB2v2cQi/view?usp=sharing

If you have any questions, contact me by this email: irfanrobbani78@gmail.com
