import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json
import time
from requests.models import Response


def get_replies(com):
    try:
        res=com['replies']
        return res
    except:
        return False


def get_reply_content(c):
    rep=c['replies']
    pid=c['id']
    for r in rep:
        cid=r['id']
        date=r['postDate']
        author=r['author']['id']
        obj=str(pid)+','+str(cid)+','+str(date)+','+str(author)
        with open('kaggle_competition_comment.csv','a',encoding='utf-8') as wp:
            wp.write(obj)
            wp.write('\n')
        if get_replies(r):
            get_reply_content(r)


s=requests.Session()
id_list=[]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36','x-xsrf-token': 'CfDJ8LdUzqlsSWBPr4Ce3rb9VL9Mg7x1JU2W4mfabtpgRF8Jg_gt1iytgeWBIe6E8Boz8STFyjOQeZLOripiu01-BHrD1rqQ2yGaWc64da_uDPPNwqtojAiqrdeMFvTaz3fLerdfVp_wgwqFiZDfyxoZWAlJloBcKlJurzWg8kvH8YBTEr8mNYiJbDQUiQ729Z8JDg','cookie':'ka_sessionid=c3567ab91804f1bdaf4558d15606d6ce; _ga=GA1.2.305529517.1633880491; .ASPXAUTH=9FF98407376602E02CA67262F25A34D06292078F8EB2D7A844AF225B9B40AEA551222C697791B52FFE8C087429483FD0062DFBC5D09BCEAC9F8FF6FEDFB0F7808590274A280A7411AE1D282FC258F48520DC7189; CSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL9sjQ3mSmNBrQ-KPpYFQ7lA6LijO-Kx97Mwb2mpaG_XLJKoasKd_PdCRAxoAmq8Ix1AUw-JDwg6PwKvhlVjW65EN3xKI_Lmc8hydqto7fsX9ubBd8meknPkAjCQ_3vsdgg; GCLB=CJ-JwuG06quylQE; _gid=GA1.2.1723726490.1636015510; _gat_gtag_UA_12629138_1=1; XSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL9Mg7x1JU2W4mfabtpgRF8Jg_gt1iytgeWBIe6E8Boz8STFyjOQeZLOripiu01-BHrD1rqQ2yGaWc64da_uDPPNwqtojAiqrdeMFvTaz3fLerdfVp_wgwqFiZDfyxoZWAlJloBcKlJurzWg8kvH8YBTEr8mNYiJbDQUiQ729Z8JDg; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiJjc3V4aXFpIiwibmJ0IjoiMjAyMS0xMS0wNFQwODo0NToxNS45MjE5NjkzWiIsImlhdCI6IjIwMjEtMTEtMDRUMDg6NDU6MTUuOTIxOTY5M1oiLCJqdGkiOiIxMWJmNDczMi01ZGI5LTRkYjAtOTFhOS03NzhiNjdkZTQxM2IiLCJleHAiOiIyMDIxLTEyLTA0VDA4OjQ1OjE1LjkyMTk2OTNaIiwidWlkIjo4MjM2OTg0LCJkaXNwbGF5TmFtZSI6IlhpIFFpIiwiZW1haWwiOiI2MDMzMTI5MTdAcXEuY29tIiwidGllciI6Ik5vdmljZSIsInZlcmlmaWVkIjpmYWxzZSwicHJvZmlsZVVybCI6Ii9jc3V4aXFpIiwidGh1bWJuYWlsVXJsIjoiaHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2thZ2dsZS1hdmF0YXJzL3RodW1ibmFpbHMvZGVmYXVsdC10aHVtYi5wbmciLCJmZiI6WyJHaXRIdWJQcml2YXRlQWNjZXNzIiwiRG9ja2VyTW9kYWxTZWxlY3RvciIsIkdjbG91ZEtlcm5lbEludGVnIiwiS2VybmVsRWRpdG9yQ29yZ2lNb2RlIiwiVHB1VW51c2VkTnVkZ2UiLCJDYWlwRXhwb3J0IiwiQ2FpcE51ZGdlIiwiS2VybmVsc0ZpcmViYXNlTG9uZ1BvbGxpbmciLCJLZXJuZWxzUHJldmVudFN0b3BwZWRUb1N0YXJ0aW5nVHJhbnNpdGlvbiIsIktlcm5lbHNQb2xsUXVvdGEiLCJLZXJuZWxzUXVvdGFNb2RhbHMiLCJEYXRhc2V0c0RhdGFFeHBsb3JlclYzVHJlZUxlZnQiLCJBdmF0YXJQcm9maWxlUHJldmlldyIsIkRhdGFzZXRzRGF0YUV4cGxvcmVyVjNDaGVja0ZvclVwZGF0ZXMiLCJEYXRhc2V0c0RhdGFFeHBsb3JlclYzQ2hlY2tGb3JVcGRhdGVzSW5CYWNrZ3JvdW5kIiwiS2VybmVsc1N0YWNrT3ZlcmZsb3dTZWFyY2giLCJLZXJuZWxzTWF0ZXJpYWxMaXN0aW5nIiwiRGF0YXNldHNNYXRlcmlhbERldGFpbCIsIkRhdGFzZXRzTWF0ZXJpYWxMaXN0Q29tcG9uZW50IiwiQ29tcGV0aXRpb25EYXRhc2V0cyIsIkRpc2N1c3Npb25zVXB2b3RlU3BhbVdhcm5pbmciLCJUYWdzTGVhcm5BbmREaXNjdXNzaW9uc1VJIiwiS2VybmVsc1N1Ym1pdEZyb21FZGl0b3IiLCJOb1JlbG9hZEV4cGVyaW1lbnQiLCJOb3RlYm9va3NMYW5kaW5nUGFnZSIsIkRhdGFzZXRzRnJvbUdjcyIsIlRQVUNvbW1pdFNjaGVkdWxpbmciLCJFbXBsb3llckluZm9OdWRnZXMiLCJFbWFpbFNpZ251cE51ZGdlcyIsIktNTGVhcm5EZXRhaWwiLCJCb29rbWFya3NVSSIsIkJvb2ttYXJrc0NvbXBzVUkiLCJGcm9udGVuZENvbnNvbGVFcnJvclJlcG9ydGluZyIsIktlcm5lbFZpZXdlckhpZGVGYWtlRXhpdExvZ1RpbWUiLCJLZXJuZWxWaWV3ZXJWZXJzaW9uRGlhbG9nV2l0aFBhcmVudEZvcmsiLCJEYXRhc2V0TGFuZGluZ1BhZ2VSb3RhdGluZ1NoZWx2ZXMiLCJMb3dlckRhdGFzZXRIZWFkZXJJbWFnZU1pblJlcyIsIk5ld0Rpc2N1c3Npb25zTGFuZGluZyIsIkRpc2N1c3Npb25MaXN0aW5nSW1wcm92ZW1lbnRzIiwiU2NoZWR1bGVkTm90ZWJvb2tzIiwiU2NoZWR1bGVkTm90ZWJvb2tzVHJpZ2dlciIsIlRhZ1BhZ2VzRGVwcmVjYXRlIiwiRmlsdGVyRm9ydW1JbWFnZXMiLCJQaG9uZVZlcmlmeUZvckNvbW1lbnRzIiwiUGhvbmVWZXJpZnlGb3JOZXdUb3BpYyIsIk5hdkNyZWF0ZUJ1dHRvbiIsIk5ld05hdkJlaGF2aW9yIl0sImZmZCI6eyJLZXJuZWxFZGl0b3JBdXRvc2F2ZVRocm90dGxlTXMiOiIzMDAwMCIsIkZyb250ZW5kRXJyb3JSZXBvcnRpbmdTYW1wbGVSYXRlIjoiMC4xMCIsIkVtZXJnZW5jeUFsZXJ0QmFubmVyIjoie1wiYmFubmVyc1wiOiBbIHsgXCJ1cmlQYXRoUmVnZXhcIjogXCJeKC9jLy4qfC9jb21wZXRpdGlvbnMvPylcIiwgIFwibWVzc2FnZUh0bWxcIjogICAgICAgICBcIldlIGFyZSBoYXZpbmcgZGVncmFkZWQgcGVyZm9ybWFuY2Ugb24gY29tcGV0aXRpb25zLiBXZSBhcmUgd29ya2luZyBvbiBpdFwiLCAgICAgICBcImJhbm5lcklkXCI6IFwiMjAyMS0xMS0wMS1jb21wcy1kZWdyYWRlZFwiIH0gXSB9In0sInBpZCI6ImthZ2dsZS0xNjE2MDciLCJzdmMiOiJ3ZWItZmUiLCJzZGFrIjoiQUl6YVN5QTRlTnFVZFJSc2tKc0NaV1Z6LXFMNjU1WGE1SkVNcmVFIiwiYmxkIjoiY2I3ZmZiYjk4OGUxYmEzY2JhY2RlZmUzMWQ4YjllMTg4NzIyZjU3MiJ9.'}
# * 获取id列表
url='https://www.kaggle.com/requests/DiscussionsService/GetTopicListByForumId'
for i in range(1,15):
    payload={"category":"all","group":"all","customGroupingIds":[],"author":"unspecified","myActivity":"unspecified","recency":"unspecified","filterCategoryIds":[],"searchQuery":"","sortBy":"hot","page":i,"forumId":883273}
    response=s.post(url,headers=headers,json=payload)
    page=json.loads(response.text)
    res=page['result']['topics']
    for t in res:
        id_list.append(str(t['id'])+','+str(t['authorUser']['id'])+','+str(t['postDate'])+'\n')
print(len(id_list))
with open('id_list.txt','w',encoding='utf-8') as wp:
    wp.writelines(id_list)
'''
# * 以下针对每个topic_id进行提取
url='https://www.kaggle.com/requests/DiscussionsService/GetForumTopicById'
for topic in id_list:
    payload={"forumTopicId":topic,"includeComments":True,"readMask":None}
    response=s.post(url,headers=headers,json=payload)
    page=json.loads(response.text)
    comment=page['result']['forumTopic']['comments']
    for c in comment:
        cid=c['id']
        date=c['postDate']
        author=c['author']['id']
        obj=str(topic)+','+str(cid)+','+str(date)+','+str(author)
        with open('kaggle_competition_comment.csv','a',encoding='utf-8') as wp:
            wp.write(obj)
            wp.write('\n')
        if get_replies(c):
            get_reply_content(c)
    print(f'{topic}完成')
    time.sleep(2)
print('圆满完成')
'''