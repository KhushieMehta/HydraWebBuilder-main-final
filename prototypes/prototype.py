def boilerplate(title,link):
    print('<!doctype html>')
    print('<html amp lang="en">')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<script async src="https://cdn.ampproject.org/v0.js"></script>')
    print('<script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>')
    print(f'<title>{title}</title>')
    print('<meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">')
    print(f'<link rel="canonical" href="{link}">')
    print('<style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>')
    print('<style amp-custom>')
    print('h1, h2, p{ color: white; padding:16px;}')
    print('</style>')
    print('</head> \n')
    print('<body>') 

def AMPstandalone(title,poster):
    print('<amp-story standalone')
    print(f'title="{title}"')
    print('publisher="Dynatons"')
    print('publisher-logo-src="https://example.com/logo/1x1.png"')
    print(f'poster-portrait-src="{poster}">')

def page(img,img_alt,id = "cover"):
    print(f'<amp-story-page id="{id}">')
    print('<amp-story-grid-layer template="fill">')
    print(f'<amp-img src="{img}" width="900"')
    print('height="1600"')
    print('layout="responsive"')
    print(f'alt="{img_alt}">')
    print('</amp-img>')
    print('</amp-story-grid-layer>')
    print('<amp-story-grid-layer template="thirds">')
    print('<h1 grid-area="middle-third" align-self="end" justify-self="center">Hello World</h1>')
    print('<p grid-area="lower-third" align-self="start" justify-self="start">This is the cover page of this story.</p>')
    print('</amp-story-grid-layer>')
    print('</amp-story-page>')

def ending():
    print('</amp-story>')
    print('</body>')
    print('</html>')


boilerplate("Hello World","Link")
AMPstandalone("Hello","Link_To_Image")
page("ImgSrc","ImgAlt")
ending()