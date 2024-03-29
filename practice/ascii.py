from PIL import Image
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('file')
parse.add_argument('-o','--output')
parse.add_argument('--width',type=int,default=80)
parse.add_argument('--height',type=int,default=80)

args = parse.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.1725*g+0.0722*b)

    unit = (256.0+1)/length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT))

    txt = ''

    for j in range(HEIGHT):
        for i in range(WIDTH):
            txt += get_char(*im.getpixel((i,j)))
        txt +='\n'
    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)