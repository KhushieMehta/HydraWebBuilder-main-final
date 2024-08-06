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

id = "Page1"
header = True
p = True
hc = "Heading"
pc = "lorem ipsum doler sit amet hvj ibibi hjiib iohih"
fill = "Video"
iurl = "https://images.pexels.com/photos/4063792/pexels-photo-4063792.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
vurl = "https://videos.pexels.com/video-files/7872533/7872533-hd_1080_1918_30fps.mp4"
animation = "fade-in"


def plainBottom(id, header, headerContent, p, pContent, fillOption, url, headerAnimation, pAnimation):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    code = f'<amp-story-page id="{id}">'

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " >
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive">
          </amp-img>
        </amp-story-grid-layer>
        """

    code += f"""<amp-story-grid-layer template="vertical" style="align-content:end">
        """
    if(header):
        code += f"""    <h1 { f'animate-in={headerAnimation}' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""    <p { f'animate-in={pAnimation}' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """</amp-story-grid-layer>
    </amp-story-page>
    """

    return code 

def gradientBottom(id, header, headerContent, p, pContent, fillOption, url, headerAnimation, pAnimation):
    """
    id: id for page 
    [header | p] : if header/p is enabled
    [headerAnimation | pAnimation] : types of animation for tags
    fillOption: Image/Video
    url: Url link for Images / Video   
    """
    code = f'<amp-story-page id="{id}">'

    if(fillOption == "Video"):
        code += f"""
        <amp-story-grid-layer template="fill">          
            <amp-video autoplay
                width="900"
                height="1600"
                layout="responsive"
                src="{url}"
                poster= " " >
            </amp-video>
        </amp-story-grid-layer>
        """
    if(fillOption == "Image"):
        code += f"""
        <amp-story-grid-layer template="fill">
          <amp-img src="{url}"
              width="900" height="1600"
              layout="responsive">
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
        code += f"""    <h1 { f'animate-in={headerAnimation}' if headerAnimation != 'None' else ''}>{headerContent}</h1>
        """

    if(p):
        code += f"""    <p { f'animate-in={pAnimation}' if pAnimation != 'None' else ''}>{pContent}</p>
        """    
    
    code += """</amp-story-grid-layer>
    </amp-story-page>
    """

    return code 

print(gradientBottom(id, header, hc, p, pc, fill, vurl, animation, animation))
