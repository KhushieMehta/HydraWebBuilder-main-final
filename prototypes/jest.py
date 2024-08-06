#import sys
#sys.path.insert(1,'X:\\HydraWebBuilder\\Engine')

from ..Engine import data 
from ..Engine import hgen 

ani = data.Animation('None','Fade-in','None')
vis = data.Visuals('Image','https://picsum.photos/900/1600')
info = data.Dataset('cover',True,True,'Heading','Lorem ipsum dolor sit amet')

style1 = {
    "id": ["#my", "#myheading1","#myheading2"],
    "tag": "h1",
    "font": "ariel",
    "color" : "#1169FF",
    "size" : "25px"
}

style2 = {
    "id": ["#my", "#my69","#my24"],
    "tag": "p",
    "font": "ariel",
    "color" : "#1169FF",
    "size" : "25px"
}

print(hgen.htmlPreview('plainTop',ani,info,vis,style1,style2).code)
