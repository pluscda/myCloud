#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest 
from BaseTest import *
from time import *
import base64
import ConfigParser
import time
import random
###############
#import tloud libs
##################

_str = """
        \nTesting the [{0}] account [ {1} ] the log:\n
        Request Msg: {2}\n
        Response code: {3}\n
        Response msg:{4}\n
        """
class ResourceBillingTests(BaseTest):
    def test_01_admin_query(self):
        f = open('./ResourceBillingTestReport.log', 'w')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _strAllType = """
        <Query>
            <User>
                <id>{0}</id>
                <Types>
                    <type>0</type>
                </Types>
                <startTime>{1}</startTime>
                <endTime>{2}</endTime>
                <limit>10</limit>
                <offset>0</offset>
            </User>
        </Query>
        """
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 * 120
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = _strAllType.format(self._id, _strStartTime,_strStartTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/resourceusage.get", _xml)
        _msg = _str.format(name, 'test_01_admin_query', _xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
       
        self.assertTrue(retcode == 200)
        #print "{0}\n\n".format(retmsg)
        
        _stVmCpu = """
        <Query>
            <User>
                <id>{0}</id>
                <Types>
                    <type>10</type>
                </Types>
                <limit>10</limit>
            </User>
        </Query>
        """
        _stVmCpu = _stVmCpu.format(self._id)
        retcode, retmsg = self.sendRequest(auth_str, "/api/resourceusage.get", _stVmCpu)
        _msg = _str.format(name, 'test_01_admin_query',_stVmCpu, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        #print "{0}\n\n".format(retmsg)
        
        _stNonExistType = """
        <Query>
            <User>
                <id>{0}</id>
                <Types>
                    <type>-9999</type>
                </Types>
                <limit>10</limit>
            </User>
        </Query>
        """
        
        _stNonExistType = _stNonExistType.format(self._id)
        retcode, retmsg = self.sendRequest(auth_str, "/api/resourceusage.get", _stNonExistType)
        _msg = _str.format(name, 'test_01_admin_query',_stNonExistType, retcode, retmsg)
        f.write(_msg)
        f.flush()
        f.close()
        self.assertTrue(retcode == 500)
        #print "{0}\n\n".format(retmsg)
        
    def test_02_non_admin_query(self):# should fail
        f = open('./ResourceBillingTestReport.log', 'a+')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("VALID_NORMAL_USER","name")
        password = config.get("VALID_NORMAL_USER","password")
        auth_str = getAuthStr(name, password)
        _strAllType = """
        <Query>
            <User>
                <id>{0}</id>
                <Types>
                    <type>0</type>
                </Types>
                <limit>10</limit>
                <offset>0</offset>
            </User>
        </Query>
        """
        _time = time.time();
        _xml = _strAllType.format(self._id)
        retcode, retmsg = self.sendRequest(auth_str, "/api/resourceusage.get", _xml)
        _msg = _str.format(name, 'test_02_non_admin_query',_xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        f.close()
        self.assertTrue(retcode == 500)
        #print "{0}\n\n".format(retmsg)
        
if __name__ == '__main__':
    unittest.main()
   