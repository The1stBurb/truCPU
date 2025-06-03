# hx=""
# with open("FONTS/4x6-font.ttf", "rb") as f:
#     data = f.read(64)  # read first 64 bytes
#     hx=data.hex()
# print(" ".join([hx[i]+hx[i+1] for i in range(0,len(hx),2)]))
def ish():
    lines=""
    with open("FONTS/4x6out.txt","r")as ft:
        lines=ft.read().split("\n")
    l2=[]
    # print(lines)
    for i in range(0,len(lines),5):
        l2.append("")
        # print(lines[i])
        for j in range(0,len(lines[i]),5):
            l2[-1]+=lines[i][j]#"#" if int(lines[i][j])<2  else " "
            # print(lines[i][j])
    with open("FONTS/4x6out2.txt","w")as ft2:
        ft2.write("\n".join(l2))
    print("done:")
def fish():
    from PIL import Image
    def image_to_ascii(image_path, output_path, threshold=128):
        # Open the image and convert to grayscale (L = 8-bit pixels)
        img = Image.open(image_path).convert("L")
        width, height = img.size
        cols=[]
        # col={255:"w",""}
        with open(output_path, 'w') as out_file:
            for y in range(height):
                row = ""
                for x in range(2,width):
                    pixel = img.getpixel((x, y))
                    if not pixel in cols:
                        cols.append(pixel)
                    # if pixel>=250:row+="0"
                    # elif pixel>=200:row+="1"
                    # elif pixel>=150:row+="2"
                    # elif pixel>=100:row+="3"
                    # elif pixel>=50:row+="4"
                    # elif pixel>=0:row+="5"
                    # if pixel in col:row+=col[pixel]
                    # else:row+="#"
                    # row+={}[pixel]
                    row += "#" if pixel < threshold else " "
                out_file.write(row + "|\n")

        print(f"ASCII saved to {output_path}")
        print("colours:",sorted(cols))

    # Example usage:
    image_to_ascii("FONTS/4x6img.png", "FONTS/4x6out.txt")
ish()