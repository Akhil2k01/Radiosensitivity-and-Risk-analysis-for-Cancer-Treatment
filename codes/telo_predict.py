from PIL import Image
import numpy as np
from tensorflow import keras
import retrieve as r
import cv2

print("\nRunning telo_predict.py")

#Accessing the image variable
imgname = r.id

ref_path = "C:/Users/Dell/Desktop/final_proj/images/refimg.tiff"
ref_image = cv2.imread(ref_path)
refh, refw = ref_image.shape[:2]
#refh, refw = 220, 176
print("Reference image shape = ",ref_image.shape)

#new_image = cv2.imread('images/image/image6.jpg')
new_image = r.img
print("New image shape = ",new_image.shape)
cv2.imwrite("C:/Users/Dell/Desktop/final_proj/results/received_images/"+imgname+".tiff", new_image)
h, w = new_image.shape[:2]

start_h = int((h-refh)/2)
start_w = int((w-refw)/2)

end_h = start_h + refh
end_w = start_w + refw

new_image = new_image[start_h:end_h, start_w:end_w, :]
print("Processed image shape = ",new_image.shape)

cv2.imwrite("C:/Users/Dell/Desktop/final_proj/results/feeded_images/"+imgname+".tiff", new_image)

model = keras.models.load_model("C:/Users/Dell/Desktop/final_proj/codes/model.h5")
predicted_mask = model.predict(new_image.reshape(1, 220, 176, 3))
calibration_factor = 0.3
predicted_length = np.sum(predicted_mask) * calibration_factor
print('Predicted telomere length: {:.2f} pixels'.format(predicted_length))

print("Successfully predicted telomere length...")

