from unittest import TestCase
from time import *
import time
import httplib
import ConfigParser
import base64
import random
from lxml import etree,objectify
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
config = ConfigParser.SafeConfigParser()
config.read("log_event_bill.ini")    
HOSTNAME = config.get("HTTP_CONFIG","ip")
PORT = config.get("HTTP_CONFIG","port")
CONTENT_TYPE = "application/xml"
NAME = config.get("ADMIN_ACCOUNT","name")
PASSWORD = config.get("ADMIN_ACCOUNT","password")
def getAuthStr(user,passwd):
    return 'Basic %s' % base64.encodestring(user + ":" + passwd).rstrip()

    
class BaseTest(TestCase):
    def setUp(self):
        self._arrId = self.getAllUserId()
        self._id = random.choice(self._arrId)
    def tearDown(self):
        pass
    def sendRequest(self, auth_string, url, content):
        #auth_string = getAuthStr('tcloudadmin', 'tcloud123')
        #HOSTNAME = 'localhost'  
        print "connect to {0} with port {1}".format(HOSTNAME,PORT)
        self.conn = httplib.HTTPConnection(HOSTNAME, PORT)
        headers = {"Content-type": CONTENT_TYPE, "Authorization": auth_string}
        self.conn.request("POST", url, content, headers)        
        response = self.conn.getresponse()
        retcode = int(response.status)
        data = response.read()
        self.conn.close()
        return retcode, data
        
    def sec2TimeStr(self,intTime):
            return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(intTime)))
    def getAllUserId(self):
        """
        <Users>
            <User>
                <id>BD1AE415-5D95-49CF-B859-53552DAD9CEF</id>
                <name>jack</name>
                <password>123456</password>
                <groupId>36BA74BB-A2FB-4724-95AF-43A09225FE84</groupId>
            </User>
        </Users>
        """
        _arr = []
        _auth_string = getAuthStr(NAME , PASSWORD)
        retcode, retmsg = self.sendRequest(_auth_string, "/api/account.list", '')
        if retcode == 200:
            root = objectify.fromstring(retmsg)
            for _obj in root.User:
                _arr.append(_obj.id.pyval)
        return _arr
    
            
            