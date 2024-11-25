hit_boxes = []

with open("imagemap.md","r") as f:
    for i in f.read().split("\n"):
        if len(i.split(" ")) == 6:
            spl = i.split(" ")
            x,y,width,height = [int(x) for x in spl[:4]]
            redirect,title = spl[4:]
            hit_boxes.append([x,y,width,height,redirect,title])

lines = []

for i in hit_boxes:
    x,y,width,height,redirect,title = i
    lines.append(" ".join([str((x/1920)*100),str((y/1080)*100),str((width/1920)*100),str((height/1080)*100),redirect,title]))

with open("fixed.md","w+") as f:
    f.write("\n".join(lines))