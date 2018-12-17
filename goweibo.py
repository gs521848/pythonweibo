from urllib import request,parse,error
import ssl
import time
import requests
import threading

def shuayuedu():
    while True:
        try:
            url='https://api.weibo.cn/2/profile/statuses?gsid=_2A25xA4KhDeRxGedJ71MW-CfEyj6IHXVTmJFprDV6PUJbkdAKLUnnkWpNVgY_SV3HjVnF_N2apIllnGh1mF0wjdAD&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=2d09610a&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=1&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&lfid=100103type%253D17%2526q%253D%25E7%25BB%2588%25E5%258D%2597%25E5%25B1%25B1&count=20&luicode=10000011&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&need_head_cards=0&feed_mypage_card_remould_enable=1&page=1&sourcetype=page&moduleID=pagecard&lcardid=1001030121_seqid%3A1194484508%7Ctype%3A17%7Ct%3A%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26uid%3D2499320562%26qtime%3D1544024838%26&cum=C9F0AEA7'
            f=request.Request(url)
            f.add_header('user-agent','Weibo/31093 (iPhone; iOS 12.0; Scale/3.00)')
            f.add_header('x-validator','wwch0QlkWy7dyG5AlajAMjyj4S/p40V8z62vtX7G7mk=')
            f.add_header('x-sessionid','BBC53507-019E-4093-ABCC-55FAB6C2CFE3')
            f.add_header('cronet_rid','4722429')
            f.add_header('accept-encoding','gzip, deflate')
            f.add_header('snrt','normal')
            context = ssl._create_unverified_context()
            request.urlopen(f,context=context)
            time.sleep(1)
        except error.HTTPError as e:
            time.sleep(3600)
        except error.URLError as u:
            time.sleep(3600)

t1= threading.Thread(target=shuayuedu,name='shua1')
t2= threading.Thread(target=shuayuedu,name='shua2')
t3= threading.Thread(target=shuayuedu,name='shua3')
t4= threading.Thread(target=shuayuedu,name='shua4')
t5= threading.Thread(target=shuayuedu,name='shua5')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()




