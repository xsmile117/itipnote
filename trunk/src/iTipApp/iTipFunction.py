#coding=gbk

#   Programmer: xsmile
#   E-mail:     xsmile117@gmail.com
#
#
#   Distributed under the terms of the GPL (GNU Public License)
#
#   iTip is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import datetime,time
from iTipDB.iTipDBwork import iTipDB
from iTipDB import iTipInfo

import iTipApp


class iTipWork():
    def __init__(self):
        self.ctime=datetime.datetime(*time.localtime()[:6])
        
    def isAlarmValid(self,date,hour,min,ctime):
        year,month,day=date.split('-')
        alarmtime=datetime.datetime(int(year),int(month),\
                                    int(day),int(hour),int(min))
        
        if alarmtime>ctime:
            self.alarm=alarmtime
            return True
        else:
            return False
        
        
    
    def add(self,content,date='1900-11-11',hour='1',min='1'):
        isalarm=False
        newiTip=iTipInfo.Info()
        style=iTipInfo.Style()
        newiTip.style=style
        if self.isAlarmValid(date, hour, min, self.ctime):
            newiTip.alarm=self.alarm
            newiTip.isRead=False
            newiTip.alarmstring='|'.join((date,hour,min))
            isalarm=True
        else:
            newiTip.alarm=self.ctime
        newiTip.content=content
        if len(content)<=10:
            newiTip.brief=content
        else:
            newiTip.brief=content[:10]
        newiTip.createdate=self.ctime
        id=iTipDB().Create(newiTip)
        iTipApp.iTipAll=iTipWork().search()
        return isalarm
        
    def search(self,key=''):
        return iTipDB().Research(key)
    
    def find(self,id):
        return iTipDB().Find(id)
    
    def delete(self,iTip):
        iTipDB().Delete(iTip)
        iTipApp.iTipAll=iTipWork().search()
        
    def save(self,iTip,content,date='1900-11-11',hour='1',min='1'):
        isalarm=False
        if self.isAlarmValid(date, hour, min, self.ctime):
            iTip.alarm=self.alarm
            iTip.alarmstring='|'.join((date,hour,min))
            iTip.isRead=False
            isalarm=True
        else:
            iTip.isRead=True
        iTip.content=content
        if len(content)<=10:
            iTip.brief=content
        else:
            iTip.brief=content[:10]
        iTip.createdate=self.ctime
        iTipDB().Update(iTip)
        iTipApp.iTipAll=iTipWork().search()
        return isalarm
    
    def saveStyle(self,iTip):
        iTipDB().Update(iTip)
        iTipApp.iTipAll=iTipWork().search()
    
    
    def checkAlarm(self):
        """检查是否有过期提醒"""
        invalidAlarm=[]
        for iTip in iTipApp.iTipAll:
            if iTip.isRead==False and iTip.alarm<=self.ctime:              
                invalidAlarm.append(iTip)
        return invalidAlarm
    
    def setAlarm(self):
        """检查是否有提醒需要设置"""
        setAlarm=[]
        for iTip in iTipApp.iTipAll:
            if iTip.isRead==False and iTip.alarm>self.ctime:
                setAlarm.append(iTip)
        return setAlarm

    