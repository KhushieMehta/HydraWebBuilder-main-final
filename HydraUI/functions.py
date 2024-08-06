from data import *

def boilerplate(title, canonical):
    code =f"""<!doctype html>
               <html amp lang="en">
                <head>
                  <script async custom-element="amp-analytics" src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script>
                  <script async custom-element="amp-video" src="https://cdn.ampproject.org/v0/amp-video-0.1.js"></script>
                  <meta charset="utf-8">
                  <meta name="description" content="{title}">
                  <script async src="https://cdn.ampproject.org/v0.js"></script>
                  <script async custom-element="amp-story"
                      src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
                  <title>{title}</title>
                  <meta name="viewport"
                        content="width=device-width,minimum-scale=1,initial-scale=1">
                  <link rel="canonical" href="{canonical}">"""
    return code

def AMPstandalone(title,publisher,logo,poster):
    amp = f"""<amp-story
              standalone
              title="{title}"
              publisher="{publisher}"
              publisher-logo-src="{logo}"
              poster-portrait-src="{poster}">"""
    return amp

def style(*args):
    """
    args : dictionary containing style options
    keys:
    id: list containing page ids
    tag: h1 p div
    font: font family
    size: font size
    color: font color
    """

    start = """
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
    <style amp-custom>
    """

    end = """
    </style>
    </head>
    <body>
    """
    
    final = """
    """
    for arg in args:
        id = arg["id"]
        tag = arg["tag"]
        font = arg["font"]
        color = arg["color"]
        size = arg["size"]

        code = ""
        for i in range(0,len(id) - 1):
            code += f"#{id[i]} {tag},"
        code += f"#{id[-1]} {tag}"
        code += "{"
        code += f"""
        font-family: {font};
        font-size: {size}px;
        color: {color};
        """
        code += """}
        """
        final += code

    return start + final + end


def ending():    
    end = """
    </amp-story>
    </body>
    </html>"""
    return end

def plainTop(data : Dataset, ani: Animation, vis: Visuals):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    id = data.id
    header = data.header
    headerContent = data.headerData
    p = data.content
    pContent = data.contentData
    fillOption = vis.filloptions
    url = vis.url
    headerAnimation = ani.headerAnimation
    pAnimation = ani.pAnimation
    imgAnimation = ani.imgAnimation
    
    code = f"""
    <amp-story-page id="{id}">
    """

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " { f'animate-in={imgAnimation} animate-in-delay="0.5s" ' if imgAnimation != 'None' else ''}>
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive"
              { f'animate-in="{imgAnimation}" animate-in-delay="0.5s" ' if imgAnimation != 'None' else ''}>
          </amp-img>
        </amp-story-grid-layer>
        """

    code += f"""
        <amp-story-grid-layer template="vertical">
        """
    if(header):
        code += f"""
        <h1 { f'animate-in="{headerAnimation}" animate-in-delay="0.5s"' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""
        <p { f'animate-in="{pAnimation}" animate-in-delay="0.5s" ' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """
        </amp-story-grid-layer>
    </amp-story-page>
    """

    return code 

def plainBottom(data : Dataset, ani: Animation, vis: Visuals):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    id = data.id
    header = data.header
    headerContent = data.headerData
    p = data.content
    pContent = data.contentData
    fillOption = vis.filloptions
    url = vis.url
    headerAnimation = ani.headerAnimation
    pAnimation = ani.pAnimation
    imgAnimation = ani.imgAnimation

    code = f'<amp-story-page id="{id}">'

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " { f'animate-in={imgAnimation} animate-in-delay="0.5s" ' if imgAnimation != 'None' else ''}>
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive" { f'animate-in={imgAnimation} animate-in-delay="0.5s"' if imgAnimation != 'None' else ''}>
          </amp-img>
        </amp-story-grid-layer>
        """

    code += f"""<amp-story-grid-layer template="vertical" style="align-content:end">
        """
    if(header):
        code += f"""    <h1 { f'animate-in={headerAnimation} animate-in-delay="0.5s"' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""    <p { f'animate-in={pAnimation} animate-in-delay="0.5s"' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """</amp-story-grid-layer>
    </amp-story-page>
    """

    return code 

def gradientTop(data : Dataset, ani: Animation, vis: Visuals):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    id = data.id
    header = data.header
    headerContent = data.headerData
    p = data.content
    pContent = data.contentData
    fillOption = vis.filloptions
    url = vis.url
    headerAnimation = ani.headerAnimation
    pAnimation = ani.pAnimation
    imgAnimation = ani.imgAnimation

    code = f'<amp-story-page id="{id}">'

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " { f'animate-in={imgAnimation} animate-in-delay="0.5s"' if imgAnimation != 'None' else ''}>
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive" { f'animate-in={imgAnimation} animate-in-delay="0.5s"' if imgAnimation != 'None' else ''}>
          </amp-img>
        </amp-story-grid-layer>
        """

    code += f"""
    <amp-story-grid-layer template="fill">
        <div style="background: linear-gradient(
            to top,  
            rgba(256,256,256,0) 0%,   
            rgba(256,256,256,0.2) 60%,  
            rgba(0,0,0,0.8) 75%,  
            rgba(0,0,0,1) 90%  
        );">
        </div>
    </amp-story-grid-layer>
    """

    code += f"""<amp-story-grid-layer template="vertical">
        """
    if(header):
        code += f"""    <h1 { f'animate-in={headerAnimation} animate-in-delay="0.5s" ' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""    <p { f'animate-in={pAnimation} animate-in-delay="0.5s"' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """</amp-story-grid-layer>
    </amp-story-page>
    """

    return code 


def gradientBottom(data : Dataset, ani: Animation, vis: Visuals):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    id = data.id
    header = data.header
    headerContent = data.headerData
    p = data.content
    pContent = data.contentData
    fillOption = vis.filloptions
    url = vis.url
    headerAnimation = ani.headerAnimation
    pAnimation = ani.pAnimation
    imgAnimation = ani.imgAnimation
    
    code = f'<amp-story-page id="{id}">'

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " { f'animate-in={imgAnimation} animate-in-delay="0.5s"' if imgAnimation != 'None' else ''}>
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive" { f'animate-in={imgAnimation} animate-in-delay="0.5s"' if imgAnimation != 'None' else ''}>
          </amp-img>
        </amp-story-grid-layer>
        """

    code += f"""
    <amp-story-grid-layer template="fill">
        <div style="background: linear-gradient(
            to bottom,  
            rgba(256,256,256,0) 0%,   
            rgba(256,256,256,0.2) 60%,  
            rgba(0,0,0,0.8) 75%,  
            rgba(0,0,0,1) 85%  
        );">
        </div>
    </amp-story-grid-layer>
    """

    code += f"""<amp-story-grid-layer template="vertical" style="align-content:end">
        """
    if(header):
        code += f"""    <h1 { f'animate-in={headerAnimation} animate-in-delay="0.5s"' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""    <p { f'animate-in={pAnimation} animate-in-delay="0.5s"' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """</amp-story-grid-layer>
    </amp-story-page>
    """

    return code 

