#lists:
list_title=["Web &#38; HTML  for Beginners",
            "HTML &#38; CSS &#38; DOM",
            "Python"]

list_subtitle =[
["Definitions","How the Web Works?","HTML"],
["WebPage ingredients","Text Editors for coding","Avoiding Repetition"],
["Introduction to Programming","Variables &#38; Strings &#38; Lists",
"Input&#8594;Function&#8594;Output","Control Flow &#38; Loops &#38; Operators"]
]

list_content =[
"<br> <b> HTML </b> stands for <em><b>Hyper Text Markup Language </b></em>  which is the main document type of the web, invented in 1990s.",
"When a user opens a web browser and writes www.udacity.com, the computer sends an HTTP request to a server. ",
"HTML has &#34;Text content&#34; (what you see), &#34;markup&#34; (what it looks), &#34;references to other documents&#34; (images, videos, etc), &#34;links to other pages&#34;."
]
#TOP of HTML
def generate_HTML_top():
  txt_top='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ilkin&#39;s webpage</title>
    <link rel="stylesheet" type="text/css" href="Notes-2.css">
</head>
 
<body>
 <h1 class="title">&#34;Introduction to Programming Nanodegree&#34; Notes</h1> 
  '''
  return txt_top


#MENU

def generate_menu(list_title,list_subtitle):
  txt1= '''
  <div>
  <h2>menu </h2>
    <ul>'''
  txt2= ''
  count_titles = len(list_title)
  for index in range(count_titles):
    title = list_title[index]
    txt2+= '''
    <li class="sub-menu"><a href="#link'''+str(index+1)+'''">'''+title+''' </a>
      <ul class="menu">'''

    list_sub_for_title = list_subtitle[index]
    count_subs = len(list_sub_for_title)
    for indes in range(count_subs):
      subtitle = list_sub_for_title[indes]
      txt2+= '''
        <li class="sub-menu"><a href="#link'''+str(index+1)+'''.'''+ str(indes+1) +'''">'''+ subtitle +'''</a></li>'''
    txt2+= '''
      </ul> 
    </li>'''
  txt3= '''
    </ul>
  </div> 
  '''
  return txt1 + txt2 + txt3


#Example of a content in HTML
def generate_content(list_title,list_subtitle):
  n=1
  txt_cnt1= '''
 <div id="link''' + str(n) + '''">
  <h2> ***''' + list_title[n-1] +''' </h2>
  '''
  txt_cnt2 = ''
  list_subtitle_1 = list_subtitle[n-1]
  subt_1_count = len(list_subtitle_1)
  for subt_1 in range(subt_1_count):
    subt = list_subtitle_1[subt_1]
    cnt = list_content[subt_1]
    txt_cnt2 += '''
    <div>
      <div id="link'''+ str(n) + '''.''' + str(subt_1+1) + '''" class="subtitle"> ''' + subt + ''' </div>'''
    txt_cnt2 += '''
      '''+ cnt + '''
    </div> '''
  txt_cnt3= '''

  </div>'''

  return txt_cnt1 + txt_cnt2 + txt_cnt3

#end of HTML
def generate_HTML_end():
  txt_end='''
</body>

</html>
'''
  return txt_end


#Prints
print generate_HTML_top() 
print generate_menu(list_title,list_subtitle)  
print generate_content(list_title,list_subtitle)
print generate_HTML_end()
