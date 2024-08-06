def initial(title):
    start =f"""<!doctype html>
               <html amp lang="en">
                <head>
                  <script async custom-element="amp-analytics" src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script>
                  <meta charset="utf-8">
                  <script async src="https://cdn.ampproject.org/v0.js"></script>
                  <script async custom-element="amp-story"
                      src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
                  <title>{title}</title>
                  <meta name="viewport"
                        content="width=device-width,minimum-scale=1,initial-scale=1">
                  <link rel="canonical" href="https://dynatons.com/web-stories/{title}.html">"""
    return start

def boilerplate():
    plate = """<link rel="preconnect" href="https://fonts.googleapis.com">
                  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@500;600&display=swap" rel="stylesheet">
                  <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
                  <style amp-custom>
                    amp-story-page {
                      background: white;
                    }
                    h1 {
                      font-size: 28px;
                      color: white;
                      font-family: 'Nunito', sans-serif;
                    }

                    h2 {
                      font-size: 24px;
                      color: white;
                      font-family: 'Nunito', sans-serif;
                    }
                    .poster{
                      border-top-style: solid;
                      border-color: #00F89F;
                		border-width: 5px;
                    }

                    .poster h1{
                      font-size: 36px;
                      color: white;
                      font-family: 'Nunito', sans-serif;
                    }


                    .content{
                      padding:16px;
                      background: rgba(0,0,0,0.4);
                      border-top-style: solid;
                      border-color: #00F89F;
                		border-width: 5px;
                    }
                    .content p{
                      font-size: 14px;
                      color: white;
                      font-family: 'Nunito', sans-serif;
                    }
                  </style>
                </head>
                <body>"""
    return plate

def AMPstandalone(title,img,imgTitle,date):
    amp = f"""<amp-story
              standalone
              title="{title}"
              publisher="Dynatons.com"
              publisher-logo-src="https://ik.imagekit.io/z83dq98xz/logo.png"
              poster-portrait-src="https://ik.imagekit.io/z83dq98xz/ik-seo/{img}/{imgTitle}.jpeg">
                            
              <amp-analytics type="gtag" data-credentials="include">
              <script type="application/json">
              """ + """
              {
                "vars" : {
                  "gtag_id": "G-B3PMLPNGEL",
                  "config" : {
                    "G-B3PMLPNGEL": { "groups": "default" }
                  }
                }
              }
              </script>
              </amp-analytics>""" + f"""

                <amp-story-page id="cover">
                <amp-story-grid-layer template="fill">
                  <amp-img src ="https://ik.imagekit.io/z83dq98xz/ik-seo/{img}/{imgTitle}.jpeg" 
                           width="900" height ="1600" layout="responsive">
                  </amp-img>
                </amp-story-grid-layer>
                <amp-story-grid-layer template="thirds">
                  <amp-img grid-area="upper-third" align-self="start" justify-self="start"
                           src="https://ik.imagekit.io/z83dq98xz/logo.png" 
                           width="80" height ="40">
                  </amp-img>
                  <h2 grid-area="middle-third" align-self="end" justify-self="start">{date}</h2>
                  <div class="poster" grid-area="lower-third">
                  <h1>
                  {title}  
                  </h1>
                  </div> 	
                </amp-story-grid-layer>
              </amp-story-page>"""
    return amp

def page(img,imgTitle,heading,content,n):
    Page = f"""<amp-story-page id="page{n}">
                <amp-story-grid-layer template="fill">
                  <amp-img src ="https://ik.imagekit.io/z83dq98xz/ik-seo/{img}/{imgTitle}.jpg" 
                           width="900" height ="1600" layout="responsive">
                  </amp-img>
                </amp-story-grid-layer>
                <amp-story-grid-layer template="thirds">
                  <h1 grid-area="middle-third" align-self="end" justify-self="start"
                      animate-in="fade-in"
                      animate-in-delay="0.8s"
                      animate-in-duration="0.5s">
                    {heading}
                  </h1>
                  <div class="content" grid-area="lower-third"
                       animate-in="fade-in"
                       animate-in-delay="1s"
                       animate-in-duration="0.75s">
                  <p>{content}</p>
                  </div> 	
                </amp-story-grid-layer>
               </amp-story-page>"""
    return Page

def ending():    
    end = """</body>
             </html>"""
    return end
