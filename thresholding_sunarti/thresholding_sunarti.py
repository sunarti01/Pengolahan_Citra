from PIL import Image, ImageEnhance

gambar = Image.open("pengambangan1.jpg")

enhancer = ImageEnhance.Brightness(gambar)

gambar_terang = enhancer.enhance(1.8) 

gambar_terang.save("pengambangan2.jpg")

gambar_terang.show("pengembangan2.jpg")