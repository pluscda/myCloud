#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest 
from BaseTest import *
from time import *
import base64
import ConfigParser
import time
import random
_str = """
        \nTesting the [{0}] account [ {1} ] the log:\n
        Request Msg: {2}\n
        Response code: {3}\n
        Response msg:{4}\n
        """

class LogTest(BaseTest):
    def test_01_queryLoggingWithAdminAccount(self):
        f = open('./LogTestReport.log', 'w')
        reqMsg = """
        <Conditions>
            <Levels>
                <level>DEBUG</level>
                <level>INFO</level>
                <level>WARNING</level>
                <level>ERROR</level>
                <level>CRITICAL</level>
            </Levels>
            <startTime>{0}</startTime>
            <endTime>{1}</endTime>
            <limit>10</limit>
            <offset>0</offset>
        </Conditions>
        """
        
        reqMsg2 = """
        <Conditions>
            <limit>10</limit>
        </Conditions>
        """
        
        reqMsg3 = """
        <Conditions>
            <limit>1000</limit>
        </Conditions>
        """
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 * 120
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = reqMsg.format(_strStartTime,_strEndTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", _xml)
        _msg = _str.format(name,'test_01_queryLoggingWithAdminAccount', _xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        print "{0}\n\n".format(retmsg)
        
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", reqMsg2)
        _msg = _str.format(name, 'test_01_queryLoggingWithAdminAccount',reqMsg2, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        print "{0}\n\n".format(retmsg)
        
        #should return max 500 records
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", reqMsg3)
        _msg = _str.format(name, 'test_01_queryLoggingWithAdminAccount',reqMsg2, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        print "{0}\n\n".format(retmsg)
        f.close()
        
    def test_02_queryLoggingWithValidUser(self):
        f = open('./LogTestReport.log', 'a+')
        reqMsg = """
        <Conditions>
            <Levels>
                <level>DEBUG</level>
                <level>INFO</level>
                <level>WARNING</level>
                <level>ERROR</level>
                <level>CRITICAL</level>
            </Levels>
            <startTime>{0}</startTime>
            <endTime>{1}</endTime>
            <limit>10</limit>
            <offset>0</offset>
        </Conditions>
        """
        
        reqMsg2 = """
        <Conditions>
            <limit>10</limit>
        </Conditions>
        """
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("INVALID_NORMAL_USER","name")
        password = config.get("INVALID_NORMAL_USER","password")
        auth_str = getAuthStr(name, password)
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 * 120
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = reqMsg.format(_strStartTime,_strStartTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", _xml)
        _msg = _str.format(name, 'test_02_queryLoggingWithValidUser',_xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        print "{0}\n\n".format(retmsg)
        
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", reqMsg2)
        _msg = _str.format(name, 'test_02_queryLoggingWithValidUser',reqMsg2, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 200)
        print "{0}\n\n".format(retmsg)
        f.close()
        
    def test_03_queryLoggingWithNotValidUser(self):
        f = open('./LogTestReport.log', 'a+')
        reqMsg = """
        <Conditions>
            <Levels>
                <level>DEBUG</level>
                <level>INFO</level>
                <level>WARNING</level>
                <level>ERROR</level>
                <level>CRITICAL</level>
            </Levels>
            <startTime>{0}</startTime>
            <endTime>{1}</endTime>
            <limit>10</limit>
            <offset>0</offset>
        </Conditions>
        """
        
        
        reqMsg2 = """
        <Conditions>
            <limit>10</limit>
        </Conditions>
        """
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("VALID_NORMAL_USER","name")
        password = config.get("VALID_NORMAL_USER","password")
        auth_str = getAuthStr(name, password)
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 * 120
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = reqMsg.format(_strStartTime,_strStartTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", _xml)
        _msg = _str.format(name, 'test_03_queryLoggingWithNotValidUser',_xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 500)
        print "{0}\n\n".format(retmsg)
        
        retcode, retmsg = self.sendRequest(auth_str, "/api/logging.get", reqMsg2)
        _msg = _str.format(name,'test_03_queryLoggingWithNotValidUser', reqMsg2, retcode, retmsg)
        f.write(_msg)
        f.flush()
        self.assertTrue(retcode == 500)
        print "{0}\n\n".format(retmsg)
        f.close()
        
if __name__ == '__main__':
    unittest.main()
    
    