import numpy as np
import os
from PIL import  Image

# Set the parameters

# path ti the directory where the images are saved

path = "path\to\images"
	   

image_width , image_height = 201, 201							#size of the images
max_files = 1300
datset_name = "Non_Defect_Data"						

# Scan for the files in the folder and attached the filename to make full path for the files
onlyfiles = [f
             for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))]

print("Number of Image in the specified directory: ",len(onlyfiles))

# Display random files from the list

for i in range(120 , 122):
    print(onlyfiles[i])
    #img = Image.open(path + "/" + onlyfiles[i])
    #img.show()



dataset = np.ndarray((max_files, image_height , image_width),dtype=np.float32)

print("Writing Images to the  dataset...")

index = 0;					# variable to keep track of loop count

for file in onlyfiles:
    file_path = path + "/" + file
    # open Image and convert it to numpy array
    img = np.asarray(Image.open(file_path))
    img = img.reshape((image_height , image_width))

    # add image array to the dataset ndarray
    dataset[index] = img
    index +=1
    if (index == max_files ):                                     # Write only  maximum 1300 images
        break

print("Done writing all images")

# Show any random image from the dataset
img = Image.fromarray(np.uint8(dataset[200]))
img.show();

# save the data to numpy file
np.save("Data/"+datset_name, dataset)

# load the file and check the data

dataset_read = np.load("Data/"+datset_name+".npy")
print(dataset_read.shape)
img = Image.fromarray(dataset_read[200])
img.show()

