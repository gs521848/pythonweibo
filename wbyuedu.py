from urllib import request,parse,error
import ssl
import time
# import requests
import threading
# import WinError
import socket
global urls
global url1
global url2
global url3

def shuayuedu():
   url1 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xDxb5DeRxGeVO71cR-SnEzj2IHXVTnS0xrDV6PUJbkdANLW_kkWpNTWDQd09Hyq0XAQ77kZzfHunts5pyz6kz&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=d5a96d1e&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A939345177%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544276715%26&cum=39F559A6'
   url2 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xD6ofDeRxGeVH4lYR9SbMyzuIHXVTnLrXrDV6PUJbkdAKLVTikWpNTwlInjDUqEEADaxfZjxoKCC5XAIARt8G&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=4935c499&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A263878888%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544280676%26&cum=AEABB26C'
   url3 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xD6rqDeRxGeVH4lYR9SnKzz2IHXVTnLkirDV6PUJbkdAKLUvNkWpNTwlI6X1xNMRijavYVO_A4xU1jvCALSPI&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=1879fa25&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A765636812%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544280773%26&cum=09173FD2'


   urls = url2
   while True:
        try:
            url1 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xDxb5DeRxGeVO71cR-SnEzj2IHXVTnS0xrDV6PUJbkdANLW_kkWpNTWDQd09Hyq0XAQ77kZzfHunts5pyz6kz&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=d5a96d1e&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A939345177%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544276715%26&cum=39F559A6'
            url2 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xD6ofDeRxGeVH4lYR9SbMyzuIHXVTnLrXrDV6PUJbkdAKLVTikWpNTwlInjDUqEEADaxfZjxoKCC5XAIARt8G&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=4935c499&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A263878888%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544280676%26&cum=AEABB26C'
            url3 = 'https://mapi.weibo.com/2/profile/statuses?gsid=_2A25xD6rqDeRxGeVH4lYR9SnKzz2IHXVTnLkirDV6PUJbkdAKLUvNkWpNTwlI6X1xNMRijavYVO_A4xU1jvCALSPI&wm=3333_2001&i=d799951&b=0&from=108B093010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=1879fa25&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__8.11.0__iphone__os12.0&ft=0&aid=01AnVuhIocFSDSK6pV3zOnQs36bm9d2UlzKXSFMYSEbooUwpg.&count=20&luicode=10000003&containerid=1076032499320562&featurecode=10000085&uicode=10000198&fid=1076032499320562&feed_mypage_card_remould_enable=1&need_head_cards=0&page=1&lfid=100103type%3D1%26q%3D%E7%BB%88%E5%8D%97%E5%B1%B1%26t%3D0&moduleID=pagecard&lcardid=seqid%3A765636812%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E7%BB%88%E5%8D%97%E5%B1%B1%7Cext%3A%26cate%3D15%26card_type%3D3%26qtime%3D1544280773%26&cum=09173FD2'
            f=request.Request(urls)
            f.add_header('user-agent','Weibo/31093 (iPhone; iOS 12.0; Scale/3.00)')
            f.add_header('x-validator','AiPCh+qxifXE06/4YYC7MMXQF+JMoLIbOI80oazh1d0=')
            f.add_header('x-sessionid','BBC53507-019E-4093-ABCC-55FAB6C2CFE3')
            f.add_header('cronet_rid','4722429')
            f.add_header('accept-encoding','gzip, deflate')
            f.add_header('snrt','normal')
            context = ssl._create_unverified_context()
            request.urlopen(f,context=context,timeout=5)
            time.sleep(1)
        except error.HTTPError as e:
            if str(e)=='HTTP Error 403: Forbidden':
                print(e)
                time.sleep(300)
                if (urls==url1):
                    urls=url2
                elif(urls==url2):
                    urls=url3
                elif(urls==url3):
                    urls=url1
                    
        except error.URLError as u:
            if str(u)=='HTTP Error 403: Forbidden':
                #     time.sleep(1800)
                # time.sleep(3600)
                time.sleep(1)
        except OSError as o:
            time.sleep(1)
        except socket.timeout as s:
            print(s)
t1= threading.Thread(target=shuayuedu,name='shua1')
t2= threading.Thread(target=shuayuedu,name='shua2')
t3= threading.Thread(target=shuayuedu,name='shua3')
t4= threading.Thread(target=shuayuedu,name='shua4')
t5= threading.Thread(target=shuayuedu,name='shua5')
tt1= threading.Thread(target=shuayuedu,name='shua11')
tt2= threading.Thread(target=shuayuedu,name='shua21')
tt3= threading.Thread(target=shuayuedu,name='shua31')
tt4= threading.Thread(target=shuayuedu,name='shua41')
tt5= threading.Thread(target=shuayuedu,name='shua51')
ttt1= threading.Thread(target=shuayuedu,name='shua12')
ttt2= threading.Thread(target=shuayuedu,name='shua22')
ttt3= threading.Thread(target=shuayuedu,name='shua32')
ttt4= threading.Thread(target=shuayuedu,name='shua42')
ttt5= threading.Thread(target=shuayuedu,name='shua52')
tttt1= threading.Thread(target=shuayuedu,name='shua13')
tttt2= threading.Thread(target=shuayuedu,name='shua23')
tttt3= threading.Thread(target=shuayuedu,name='shua33')
tttt4= threading.Thread(target=shuayuedu,name='shua43')
tttt5= threading.Thread(target=shuayuedu,name='shua53')
ttttt1= threading.Thread(target=shuayuedu,name='shua14')
ttttt2= threading.Thread(target=shuayuedu,name='shua24')
ttttt3= threading.Thread(target=shuayuedu,name='shua34')
ttttt4= threading.Thread(target=shuayuedu,name='shua44')
ttttt5= threading.Thread(target=shuayuedu,name='shua54')

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
tt1.start()
tt2.start()
tt3.start()
tt4.start()
tt5.start()
ttt1.start()
ttt2.start()
ttt3.start()
ttt4.start()
ttt5.start()
tttt1.start()
tttt2.start()
tttt3.start()
tttt4.start()
tttt5.start()
ttttt1.start()
ttttt2.start()
ttttt3.start()
ttttt4.start()
ttttt5.start()





