import os
import random
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array, array_to_img


# Define path to the source image and mask directory
image_dir = 'sliced/'
mask_dir = 'masks/'

# Define paths to the augmented image and mask directories
aug_image_dir = 'aug_sliced'
aug_mask_dir = 'aug_masks'

# Create the augmented image and mask directories if they do not exist
if not os.path.exists(aug_image_dir):
    os.makedirs(aug_image_dir)
if not os.path.exists(aug_mask_dir):
    os.makedirs(aug_mask_dir)

# Create ImageDataGenerator with augmentation options
data_gen_args = dict(rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='reflect',
        samplewise_center=False,
        samplewise_std_normalization=False,
        featurewise_center=False,
        featurewise_std_normalization=False,
        zca_whitening=False)

image_datagen = ImageDataGenerator(**data_gen_args)
mask_datagen = ImageDataGenerator(**data_gen_args)

# Define the number of images to generate for each class
num_augmented_images = 10

# Generate augmented images for the image class
for filename in os.listdir(image_dir):
    img = load_img(image_dir + filename)  # Load image
    x = img_to_array(img)  # Convert image to array
    x = x.reshape((1,) + x.shape)  # Reshape image for augmentation
    i = 0
    for batch in image_datagen.flow(x, batch_size=1, shuffle=False,
                              save_to_dir=aug_image_dir, save_prefix=filename[:-5], save_format='tiff'):
        i += 1
        if i >= num_augmented_images:
            break  # Break loop after generating num_augmented_images augmented images
       
print("Augmenting Images - Done")
# Generate augmented images for the mask class
for filename in os.listdir(mask_dir):
    img = load_img(mask_dir + filename)  # Load image
    x = img_to_array(img)  # Convert image to array
    x = x.reshape((1,) + x.shape)  # Reshape image for augmentation
    i = 0
    for batch in mask_datagen.flow(x, batch_size=1,
                              save_to_dir=aug_mask_dir, save_prefix=filename[:-5], save_format='tiff'):
        i += 1
        if i >= num_augmented_images:
            break  # Break loop after generating num_augmented_images augmented images

print("Augmenting Masks - Done")
     
#--------------------------------------------compare original and augment image---------------------------

"""
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
import random
import matplotlib.pyplot as plt

# Define the ImageDataGenerator with augmentation parameters
datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='mirror')

# Set the path to the directory containing the original images
original_dataset_path = ''

# Loop through each class and randomly select 10 images to augment and display
for class_dir in os.listdir(original_dataset_path):
    # Create a list of the file paths for the images in the class directory
    filepaths = [os.path.join(original_dataset_path, class_dir, f) for f in os.listdir(os.path.join(original_dataset_path, class_dir))]
    # Select 10 random file paths
    random_filepaths = random.sample(filepaths, k=10)
    # Load and display each image along with its augmented version
    for filepath in random_filepaths:
        # Load the image
        img = load_img(filepath)
        # Convert the image to a numpy array
        x = img_to_array(img)
        # Reshape the array to a 4D tensor with shape (1, height, width, channels)
        x = x.reshape((1,) + x.shape)
        # Generate batches of augmented images
        i = 0
        for batch in datagen.flow(x, batch_size=1):
            i += 1
            # Show the original and augmented images side by side
            if i == 1:
                fig, axs = plt.subplots(1, 2)
                axs[0].imshow(img)
                axs[0].set_title('Original')
                axs[1].imshow(array_to_img(batch[0]))
                axs[1].set_title('Augmented')
                fig.suptitle(class_dir)
                plt.show()
            # Exit the loop after generating one augmented image
            if i > 0:
                break

"""