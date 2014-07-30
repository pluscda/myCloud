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

class EventTest(BaseTest):
    def test_01_create_event(self): #Elaster 1.5 report event
        f = open('./EventTestReport.log', 'w')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _strEvent = """
        <Events>
            <Event>
                <userId>{0}</userId>
                <severity>info</severity>
                <id>1</id>
                <message>alexp</message>
            </Event>
            <Event>
                <userId>{1}</userId>
                <severity>error</severity>
                <id>2</id>
                <message>err</message>
            </Event>
        </Events>
        """
        _time = time.time();
        #self._id = random.choice(self.getAllUserId())
        _xml = _strEvent.format(self._id,self._id)
        retcode, retmsg = self.sendRequest(auth_str, "/api/event.create", _xml)
        _msg = _str.format(name, 'test_01_create_event', _xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        f.close()
        #print "{0}\n\n".format(retmsg)
        self.assertTrue(retcode == 200)
       
        
    def test_02_query_event(self): #Elaster 1.5
        f = open('./EventTestReport.log', 'a+')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _strQuery = """
        <Conditions>
            <Levels>
                <level>ERROR</level>
                <level>INFO</level>
            </Levels>
            <isRead>0</isRead>
            <startTime>{0}</startTime>
            <endTime>{1}</endTime>
            <limit>10</limit>
            <offset>0</offset>
        </Conditions>

        """
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = _strQuery.format(_strStartTime,_strEndTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/event.get", _xml)
        _msg = _str.format(name, 'test_02_query_event',_xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        f.close()
        #print "{0}\n\n".format(retmsg)
        self.assertTrue(retcode == 200)
       
    def test_03_set_event2Read(self):
        f = open('./EventTestReport.log', 'a+')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _strSet2Read = """
        <EventIds>
            <eventId>1</eventId>
            <eventId>2</eventId>
        </EventIds>
        """
        _xml = _strSet2Read
        retcode, retmsg = self.sendRequest(auth_str, "/api/event.setread", _xml)
        _msg = _str.format(name,'test_03_set_event2Read', _xml, retcode, len(retmsg) > 0 and retmsg or '')
        f.write(_msg)
        f.flush()
        f.close()
        #print "{0}\n\n".format(retmsg)
        self.assertTrue(retcode == 200)
        
        
    def test_09_purge_event(self): #Elaster 1.5 
        f = open('./EventTestReport.log', 'a+')
        config = ConfigParser.SafeConfigParser()
        config.read("./log_event_bill.ini")    
        name = config.get("ADMIN_ACCOUNT","name")
        password = config.get("ADMIN_ACCOUNT","password")
        auth_str = getAuthStr(name, password)
        _strPurge = """
        <Conditions>
            <userId>{0}</userId>
            <startTime>{1}</startTime>
            <endTime>{2}</endTime>
            <Severities>
                <severity>info</severity>
                <severity>error</severity>
            </Severities>
        </Conditions>
        """
        _time = time.time();
        _strEndTime = self.sec2TimeStr(_time);
        _strStartTime = _time - 60 * 60 
        _strStartTime = self.sec2TimeStr(_strStartTime)
        _xml = _strPurge.format(self._id,_strStartTime,_strEndTime)
        retcode, retmsg = self.sendRequest(auth_str, "/api/event.delete", _xml)
        _msg = _str.format(name, 'test_09_purge_event', _xml, retcode, retmsg)
        f.write(_msg)
        f.flush()
        f.close()
        #print "{0}\n\n".format(retmsg)
        self.assertTrue(retcode == 200)
       
    
if __name__ == '__main__':
    unittest.main()