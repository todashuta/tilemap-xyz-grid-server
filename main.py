from flask import Flask, helpers
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from flask_script import Manager

app = Flask(__name__)
mananger = Manager(app)

@app.route("/<z>/<x>/<y>.png")
def index(z, x, y):
    #/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf
    #fontfile = "/usr/share/fonts/truetype/vlgothic/VL-PGothic-Regular.ttf"
    fontfile = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"

    img = Image.new("RGBA", (256, 256), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    draw.rectangle((1,1,254,254), fill=(255,255,255,255))
    draw.rectangle((2,2,253,253), fill=(255,255,255,0))

    font = ImageFont.truetype(fontfile, 32) #int(img.size[1]/10)

    # outline
    #draw.text((10-1,10-1), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    #draw.text((10+1,10-1), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    #draw.text((10-1,10+1), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    #draw.text((10+1,10+1), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))

    draw.text((10-2,10-2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10-2,10+0), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10-2,10+2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))

    draw.text((10+0,10-2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10+0,10+0), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10+0,10+2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))

    draw.text((10+2,10-2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10+2,10+0), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))
    draw.text((10+2,10+2), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(255,255,255,255))

    draw.text((10,10), "Z: {}\nX: {}\nY: {}".format(z, x, y), font=font, fill=(0,0,0,255))

    buf = BytesIO()
    img.save(buf, "png")
    resp = helpers.make_response(buf.getvalue())
    resp.headers["Content-Type"] = "image/png"
    return resp

if __name__ == "__main__":
    #app.run(debug=False)
    mananger.run()
