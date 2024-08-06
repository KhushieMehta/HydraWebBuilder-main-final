from functions import *
from data import *

class Router:
    def __init__(self, name):
        if(name == "Plain Bottom"):
            self.function = plainBottom
        if(name == "Gradient Bottom"):
            self.function = gradientBottom
        if(name == "Plain Top"):
            self.function = plainTop
        if(name == "Gradient Top"):
            self.function = gradientTop

    def __call__(self, data, ani, vis):
        return self.function(data, ani, vis)


class htmlPreview:
    def __init__(self, function, ani : Animation, data : Dataset, vis : Visuals, *args):
        page = Router(function)
        a = boilerplate("None", "None")
        b = style(*args)
        c = AMPstandalone("None","None","None","None") 
        d = page(data, ani, vis)
        self.code = a + b + c + d + ending()

class htmlExport:
    def __init__(self, start: Start, filename):
        self.start = start
        self.filename = filename
        self.pages = [] #all the page code in strings
        self.styles = [] # save all the style objects

        self.a = boilerplate(self.start.title,self.start.canonical)
        self.c = AMPstandalone(self.start.title, self.start.publisher, self.start.logo, self.start.poster)

    def insertSyles(self, style1: Style, style2: Style):
        self.styles.append(style1)
        self.styles.append(style2)

    def insertPage(self, page: Page):
        final = Router(page.function)(page.dataset,page.animation,page.visual)
        self.pages.append(final)

    def finalStyle(self):
        return style(*(x.getarg() for x in self.styles))
    
    def pageMaker(self):
        code = self.a + self.finalStyle() + self.c
        for page in self.pages:
            code += page
        code += ending()
        self.code = code

    def maker(self):
        with open(self.filename, "w") as f:
            f.write(self.code)
            f.close()
    
    def getCode(self):
        return self.code 
    