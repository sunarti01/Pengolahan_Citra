import cv2 
 
# membaca citra 
img = cv2.imread('sunarti.jpg.jpg') 
 
# menampilkan dimensi citra asli 
print('Original Image Shape:', img.shape) 
 
# resize citra menggunakan cv2.resize() 
resized_img = cv2.resize(img, (900, 900)) 
 
# menampilkan dimensi citra hasil resize 
print('Resized Image Shape:', resized_img.shape) 
 
# menampilkan citra asli dan citra hasil resize 
cv2.imshow('Original Image', img) 
cv2.imshow('Resized Image', resized_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 