from scrapy import Selector

html = '''
<html>
 <body>
 <div class="hello" id="hello">
 <p>Hello World!</p>
 </div>
 <div class="hello">
    <h1>It's almost Fridayyy!</h1>
    <p class="weekend">The weekend is so close!</p>
    <p class="week">It's just Thursday :( </p>
 </div>
 <p>Hope you are Enjoying Zindua So far</p>
 <p class='hello'>My Classmates at Zindua are fun</p>
 </body>
</html>
'''

html2 = '''
<html>
 <body>
    <div class="hello" id="hello">
        <p class="">Hello World!</p>
    </div>
    <div class="hello">
        <h1>It's almost Fridayyy!</h1>
        <p class="weekend">The weekend is so close!</p>
        <p class="week">It's just Thursday :( </p>
    </div>
    <p>Hope you are Enjoying Zindua So far</p>
    <p>My Classmates at Zindua are fun</p>
 </body>
</html>
'''

sel = Selector(text=html2)

# print(sel.xpath('/html/body/div[2]/p[@class="week"]').extract())

# print(sel.xpath('/html/body/div[2]/p[contains(@class, "week")]').extract())

# print(sel.css('html > body p').extract()) # /html/body//p in xpath

# print(sel.css('html > body > p:nth-of-type(2)').extract()) # /html/body/p[2] in xpath

print(sel.css('div.hello > p.week').extract())