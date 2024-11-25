from PIL import Image, ImageDraw, ImageFont

collab = Image.open("collab.png").convert("RGB")
draw = ImageDraw.Draw(collab)
hit_boxes = []

with open("imagemap.md","r") as f:
    for i in f.read().split("\n"):
        if len(i.split(" ")) == 6:
            x,y,width,height = [int(x) for x in i.split(" ")[:4]]
            hit_boxes.append([x,y,width,height, i.split(" ")[5]])

for i in hit_boxes:
    print(i)
    draw.rectangle(((i[0],i[1]),(i[2]+i[0],i[1]+i[3])), outline="red")
    draw.text((i[0],i[1]),i[4])

collab.save("wow.png")