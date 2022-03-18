from bs4 import BeautifulSoup
from urllib.request import urlopen

cnt = 0
title_list = []
link_list = []

# 지정한 url의 모든 html 코드를 긁어온다.
html=urlopen('https://www.boannews.com/media/t_list.asp')
bs=BeautifulSoup(html,'html.parser')

# 긁어온 코드에서 span 태그의 class 이름이 news_txt인 것만 title에 저장한다.
# boanews 홈페이지에서는 기사 제목을 <span class='news_txt'>에 작성해놓음.
title = bs.select('span[class = news_txt]')

# <div class = news_list> 밑에 <a href= ~~>로 기사 링크가 걸려있음
link = bs.select('div.news_list a')

# title에는 기사 제목 뿐만 아니라 태그까지 모두 포함되어 있기 때문에 get_text()를 이용해 text만 뽑아준다.
# 뽑은 기사 제목을 title_list라는 list에 저장
for i in title:
    title_list.append(i.get_text())

# <div class = news_list>에 <a href = ~~>로 2개의 링크를 써놨음
# 그래서 1개씩만 출력해주기 위해 link의 수를 카운트 하고 cnt가 홀수일 경우에만 출력하도록 해줌
# 뽑은 link를 link_list라는 list에 저장
for i in link:
    cnt += 1
    if cnt % 2 == 1:
        link_list.append("https://www.boannews.com" + i.attrs["href"])

# 반복문을 기사 title의 개수만큼 돌리고 title_list와 link_list에서 하나씩 뽑아줌
for i in range(0, len(title)):
    print(title_list[i] + ' ' + link_list[i])