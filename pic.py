from PIL import Image

img = Image.open('106044_benefit.jpg')
watermark = Image.open('benefit.png')

watermark.paste(img, (0, 150))
watermark.save("106044_benefit+watermark.png")
