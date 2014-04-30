 # -*- coding: utf-8 -*-
import urllib
import requests 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class RefreshWork:

    def __init__(self, proxies=None):
        
        self.login_url = "http://3g.51job.com/my/login.php"
        self.refresh_url = "http://3g.51job.com/my/refreshresume.php"

        self.proxies = proxies
        self.session = requests.Session()
        self.User_Agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36'
        self.headers = {'User-Agent':self.User_Agent, 
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Connection': 'keep-alive',
                'Host':'3g.51job.com',
                'Referer':'http://3g.51job.com'}


    def getUrl(self, url, timeout=8):
        try:
            return 1, self.session.get(url, headers=self.headers, proxies=self.proxies, verify=False, timeout=timeout )
        except requests.exceptions.RequestException, e:
            print 'HTTPError = ', e
        except requests.exceptions.ConnectionError, e:
            print 'URLError = '
        except requests.exceptions.HTTPError, e:
            print 'URLError = '
            return 0, e.response
        except requests.exceptions.TooManyRedirects, e:
            print 'URLError = '
        except:
            print '\nSome error/exception occurred.(%s)' % url 
        return 0,""
        
    def postUrl(self, url, data=None):
        try:
            return 1, self.session.post(url, data=data, headers=self.headers, proxies=self.proxies, verify=False )
        except requests.exceptions.RequestException, e:
            print 'HTTPError = ' , e
        except requests.exceptions.ConnectionError, e:
            print 'URLError = ' , e
        except requests.exceptions.HTTPError, e:
            print 'URLError = ' , e
            return 0, e.response
        except requests.exceptions.TooManyRedirects, e:
            print 'URLError = ' , e
        except:
            print '\nSome error/exception occurred.'
        return 0,""
        
    def postFileUrl(self, url, files=None, data=None, headers=None):
        try:
            return 1, requests.post(url, files=files, data=data, proxies=self.proxies, headers=headers, verify=False )
        except requests.exceptions.RequestException, e:
            print 'HTTPError = ' , e
        except requests.exceptions.ConnectionError, e:
            print 'URLError = ' , e
        except requests.exceptions.HTTPError, e:
            print 'URLError = ' , e
            return 0, e.response
        except requests.exceptions.TooManyRedirects, e:
            print 'URLError = ' , e
        except:
            print '\nSome error/exception occurred.'
        return 0,""
        
    def login(self, username, passworld):
        #return True
       
        formdata =[("act","login"), 
        ("fromurl", "http://3g.51job.com/"), 
        ("username", username),
        ("password", passworld),
        ("autologin", "1")
        ]
        formdata = urllib.urlencode(formdata)
        r, res = self.postUrl(self.login_url, formdata)
        if r and res.status_code == 200:
            return res.text.find("logout.php") >= 0
        return False 
        
    def refresh(self):
        r, res = self.getUrl(self.refresh_url)
        if r and res.status_code == 200:
            return True
        return False     
        
if __name__ == '__main__':
    refreshWork = RefreshWork()
    if refreshWork.login('username', 'password'):
        print "Login succeed."
        if refreshWork.refresh():
            print "refresh ok."
