from PIL import Image

# https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes
# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.new
def watermark(im, mark, position):
    layer = Image.new("RGBA", im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)


im = Image.open("img\\clungup.jpg")
mark = Image.open("img\\watermark.png")
mark = mark.resize((100,100))

out = watermark(im, mark, (0,50))
out.show()
out.save("img\\clungup_w_watermark.jpg")

# https://answers.microsoft.com/en-us/windows/forum/windows_10-files/windows-10-invalid-value-for-registry-jpeg/24d4ffe9-2a16-47e2-8da2-ea5d9f4593c4

