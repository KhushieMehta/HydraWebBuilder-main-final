class Start:
    def __init__(self,canonical,title,publisher,poster,logo):
        self.canonical = canonical
        self.title = title
        self.publisher = publisher
        self.poster = poster
        self.logo = logo

    def publish(self):
        s = f"""
        {self.canonical}
        {self.title}
        {self.publisher}
        {self.logo}
        {self.poster}
        """
        print(s)

class Animation:
    def __init__(self,h,p,img):
        self.headerAnimation = h
        self.pAnimation = p
        self.imgAnimation = img

class Dataset:
    def __init__(self,id,h,p,hdata,pdata):
        self.id = id
        self.header = h
        self.content = p
        self.headerData = hdata
        self.contentData = pdata

    def setid(self, a):
        self.id = a

class Visuals: 
    def __init__(self,option,url):
        self.filloptions = option
        self.url = url
        
class Style:
    def __init__(self,id,tag,font,color,size):
        self.id = id
        self.tag = tag
        self.font = font
        self.color = color
        self.size = size

    def setid(self, a):
        self.id = a

    # Returns Dictionary
    def getarg(self):
        result = {}
        result["id"] = [self.id]
        result["tag"] = self.tag
        result["font"] = self.font
        result["color"] = self.color
        result["size"] = self.size
        return result
    
class Page:
    def __init__(self, function, info: Dataset, ani : Animation, vis: Visuals):
        self.function = function
        self.dataset = info
        self.animation = ani
        self.visual = vis