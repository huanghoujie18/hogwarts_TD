import requests

def test_timeout():
    url = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13909161860'
    r=requests.get(url=url,timeout=1)
    print(r.text)
# 轮循
def test_files():
    # 携程上传用户头像
    for i in range(0,10):
        try:
            url='https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx'
            cookies={'cookie': '_abtest_userid=5ad34330-9666-4c2c-ba6e-517a121ba747; _ga=GA1.2.1590610106.1570536462; _RGUID=2e161c19-5732-47d4-9102-18b3ce8ef37b; _RDG=284156a9cca3f72df1017ef804d7693d5c; _RSG=KVaCNb17Mu2xDlZEFB6249; _RF1=112.96.40.137; _gid=GA1.2.270266470.1591430170; MKT_CKID=1591430170314.cpcoh.5e4w; MKT_CKID_LMT=1591430170317; MKT_Pagesource=PC; Session=SmartLinkCode=U155950&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; MKT_OrderClick=ASID=4897155950COr76YLc7OkCFdKbvAodrRAKCw760791534264291820687965387034&AID=4897&CSID=155950&OUID=pinP&CT=1591430348596&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155950%26allianceid%3D4897%26ouid%3DpinP%26keywordid%3D87965387034%26bd_vid%3D7607915342642918206%26ds_rl%3D1284915%26gclid%3DCOr76YLc7OkCFdKbvAodrRAKCw%26gclsrc%3Dds&VAL={"pc_vid":"1570536459116.2387ve"}; cticket=D84DE625EF040AECBB1091C1F2B0229783FA10DF4B7456D4D441072DBD098DE4; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojDHPoOhstn/r5nMmI80RW9K0/Aj871wZMefSitNVdW3gkxfBhfO+4Gj7jGoJsQACMe3zHaZ7sFexrd/YFQIIiHXlfuOHCZnWBoooG3tW+68bnDF92lNff80NFcHBqExItlpYDkt55YSPxBOOYwD0Q2MLurC6sN9SUK0EewBQxxROol1BYcSuNKA0o/N47NUGD5FegNyv73bF9Qp29QNpMP9M+3k8A1vDs+W10ekrF2RB8OVgWhKJggY1IfyPum4u2UGTgXXXq1gg=; DUID=u=8893658AACB8CA3172241B946B23E887&v=0; IsNonUser=F; UUID=597EAD53915E4ABAB7043A64FEBADF7A; IsPersonalizedLogin=F; Union=OUID=pinP&AllianceID=4897&SID=155950&SourceID=&createtime=1591431464&Expires=1592036264066; _jzqco=%7C%7C%7C%7C1591430170621%7C1.131066986.1591430170278.1591430348612.1591431464097.1591430348612.1591431464097.0.0.0.5.5; __zpspc=9.3.1591430348.1591431464.2%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _gcl_dc=GCL.1591431464.COr76YLc7OkCFdKbvAodrRAKCw; _gat=1; ASP.NET_SessionSvc=MTAuMjUuMTY3LjQ4fDkwOTB8b3V5YW5nfGRlZmF1bHR8MTU4OTAwNDc3NDM0NA; ASP.NET_SessionId=v3b3ywa3ifzblfmtfh51ga1h; MyCtripDescription=UID=246B35A856B8103B8EFB6D2AAB58B4E5&IsClub140=F&IsHoliday=F&CorpMileage=F; _bfa=1.1570536459116.2387ve.1.1570536459116.1591430167278.2.10; _bfs=1.9; _bfi=p1%3D100013%26p2%3D100021%26v1%3D10%26v2%3D9'}
            files={'uploadFile_852':('Markdown.jpg',open('D:\\Markdown.jpg','rb'),'image/png')}
            r=requests.post(url=url,files=files,verify=False,cookies=cookies,timeout=0.25)
            print(r.text)
        except:
            print('运行出错')
