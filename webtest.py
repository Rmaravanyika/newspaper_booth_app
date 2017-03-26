from urllib import request
import re


#,'http://nytimes.com','http://cnn.com'
the_url = ['https://www.newsday.co.zw/']


#regular expression to get the title of the page
the_regex = '<h1>(.*?)</h1>'
th_regex = '<p>(.+?)</p>'
pattern = re.compile(the_regex)
patter = re.compile(th_regex)



for item in the_url:
    htmlfile = request.urlopen(item)
    htmlfilel = request.urlopen(item)
    htmltext = htmlfile.read()
    htmltexti = htmlfilel.read()
    titles = re.findall(pattern,str(htmltext))
    titles_body = re.findall(patter,str(htmltexti))

    i=0
    try:
        while i<len(the_regex):
            i+=1
            print(titles[i] + ':' + '\n'  + titles_body[i] + '\n' + '\n')
            #print(titles_body[i])
        
    except:
        pass
        

