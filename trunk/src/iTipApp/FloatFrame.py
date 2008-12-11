# -*- coding: utf-8 -*-

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

import wx
import datetime
import time

import iTipApp
from iTipApp.iTipFrame import iTipFrame
from iTipApp.TaskbarFrame import iTipTaskBar
from iTipApp.iTipManageFrame import iTipManageFrame
from iTipApp.iTipCommon import AlarmTimer
from iTipApp.iTipCommon import SoundThread
from iTipApp.iTipFunction import iTipWork

class FloatFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 1107, "",
                style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)

        self.SetPosition(wx.Point(800,100))
        self.bmp = wx.BitmapFromImage(wx.Image('pic\\float.png',wx.BITMAP_TYPE_ANY))
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        self.iTipAlarmers={}
        
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

        self.SetWindowShape()
        self.SetToolTipString(u"双击新建")
        iTipSFrame=iTipManageFrame(self,1108,u'便签管理')
        self.iTipTaskBar=iTipTaskBar(self,iTipSFrame)
        self.iTipAlarmSet()
        self.ReadiTipConfig()
        self.DoOpen()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OniTipNew)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)#3 绑定窗口创建事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnFrameLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnFrameLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnFrameMotion)
        self.Bind(wx.EVT_QUERY_END_SESSION, self.OniTipExit)
        
            
    def SetWindowShape(self, evt=None):
        r = wx.RegionFromBitmap(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

    def OnClose(self, evt):
        self.SaveiTipConfig()
        if iTipApp.isiTipOpenOn:
            self.RecordOpen()
        for iTipShow in self.GetChildren():
            if type(iTipShow)==iTipFrame and iTipShow.IsShown():
                iTipShow.OniTipHide(evt)
                
        self.Destroy()
        
    def OnFrameLeftDown(self, event):
        self.CaptureMouse()
        mouse=wx.GetMousePosition()
        frame=self.GetPosition()
        self.delta=wx.Point(mouse.x-frame.x,mouse.y-frame.y)

    def OnFrameMotion(self, event):      
        if event.Dragging() and event.LeftIsDown():
            mouse=wx.GetMousePosition()
            self.Move((mouse.x-self.delta.x,\
                        mouse.y-self.delta.y))
                
    def OnFrameLeftUp(self,event):
        if self.HasCapture():
            self.ReleaseMouse()
            
    def OnRightClick(self, event):
        # only do this part the first time so the events are only bound once
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            self.popupID4 = wx.NewId()
            self.popupID5 = wx.NewId()
            self.popupID6 = wx.NewId()
            self.popupID7 = wx.NewId()
            self.Bind(wx.EVT_MENU, self.OniTipFloatHide, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OniTipShowNormal, id=self.popupID2)
            self.Bind(wx.EVT_MENU, self.OniTipShowAlarm, id=self.popupID3)
            self.Bind(wx.EVT_MENU, self.OniTipShowAll, id=self.popupID4)
            self.Bind(wx.EVT_MENU, self.OniTipCloseAll, id=self.popupID5)
            self.Bind(wx.EVT_MENU, self.OniTipManage, id=self.popupID6)
            self.Bind(wx.EVT_MENU, self.OniTipExit, id=self.popupID7)
        menu = wx.Menu()
        menu.Append(self.popupID1, u"隐藏")
        menu.AppendSeparator()
        menu.Append(self.popupID2, u"显示普通便笺")
        menu.Append(self.popupID3, u"显示提醒便笺")
        menu.Append(self.popupID4, u"显示所有便笺")
        menu.Append(self.popupID5, u"关闭所有显示")
        menu.AppendSeparator()
        menu.Append(self.popupID6, u"便笺管理")
        menu.Append(self.popupID7, u"退出")
        self.PopupMenu(menu, event.GetPosition())
        menu.Destroy()
        
    def OniTipNew(self,event):
        iTipShow=iTipFrame(self,-1,"")
        iTipShow.Show()
        th=SoundThread('sound\\new.wav',iTipApp.isiTipSoundOn)
        th.start()
    
    def OniTipShowNormal(self,event):
        self.OniTipCloseAll(event)
        for iTip in iTipApp.iTipAll:
            if iTip.isRead:
                iTipShow=wx.FindWindowById(1108).showiTip(iTip)
                iTipShow.Show()

    def OniTipShowAlarm(self,event):
        self.OniTipCloseAll(event)
        for iTip in iTipApp.iTipAll:
            if not iTip.isRead:
                iTipShow=wx.FindWindowById(1108).showiTip(iTip)
                iTipShow.Show()
    
    def OniTipShowAll(self,event):
        for iTip in iTipApp.iTipAll:
            iTipShow=wx.FindWindowById(1108).showiTip(iTip)
            iTipShow.Show()
    
    def OniTipCloseAll(self,event):
        wx.FindWindowById(1108).OniTipCloseAll(event)

    
    def OniTipFloatHide(self,event):
        self.Hide()
        
    def OniTipManage(self,event):
        iTipManage=wx.FindWindowById(1108)
        iTipManage.Show()
    
    def OniTipExit(self,event):
        self.iTipTaskBar.Destroy()
        self.Close()

    def iTipAlarmSet(self):
        for iTip in iTipWork().checkAlarm():
            self.addiTipAlarmer(iTip,True)
        for iTip in iTipWork().setAlarm():
            self.addiTipAlarmer(iTip)
            
    def addiTipAlarmer(self,iTip,alarm=False):
        if alarm:
            times=1
        else:
            alarmday=(iTip.alarm-datetime.datetime(*time.localtime()[:6])).days
            alarmsecond=(iTip.alarm-datetime.datetime(*time.localtime()[:6])).seconds
            times=(alarmday*86400+alarmsecond)*1000
        self.iTipAlarmers[iTip.id]=AlarmTimer(iTip.id)
        self.iTipAlarmers[iTip.id].Start(times,oneShot=True)
        
    def deleteiTipAlarmer(self,id):
        if self.iTipAlarmers.get(id)!=None:
            if self.iTipAlarmers[id].IsRunning():
                self.iTipAlarmers[id].Stop
            del self.iTipAlarmers[id]
            
    def ReadiTipConfig(self):
        self.cfg = wx.Config('iTipConfig')
        if self.cfg.Exists('isRun'):
            temp=self.cfg.ReadInt('isRun')
            if temp==1:
                self.iTipTaskBar.Destroy()
                self.Destroy()  
            else:
                self.cfg.WriteInt('isRun',1)    
        else:
            self.cfg.WriteInt('isRun',1)
        if self.cfg.Exists('sound'):
            iTipApp.isiTipSoundOn=self.cfg.ReadBool('sound')
        if self.cfg.Exists('open'):
            iTipApp.isiTipOpenOn=self.cfg.ReadBool('open')
        if self.cfg.Exists('colour'):
            iTipApp.isiTipColourRandom=self.cfg.ReadBool('colour')
        if self.cfg.Exists('rgb'):
            rgb=self.cfg.Read('rgb')
            r,g,b=rgb.split('|')
            iTipApp.MarkColourR=int(r)
            iTipApp.MarkColourG=int(g)
            iTipApp.MarkColourB=int(b)
            iTipApp.iColour=wx.Colour(iTipApp.MarkColourR,\
                                      iTipApp.MarkColourG,\
                                      iTipApp.MarkColourB)           
                        
    def SaveiTipConfig(self):
        self.cfg.WriteBool('sound',iTipApp.isiTipSoundOn)
        self.cfg.WriteBool('open',iTipApp.isiTipOpenOn)
        self.cfg.WriteBool('colour',iTipApp.isiTipColourRandom)
        r,g,b=iTipApp.iColour.Get()
        self.cfg.Write('rgb',str(r)+'|'+str(g)+'|'+str(b))
        self.cfg.WriteInt('isRun',0)
        
    def RecordOpen(self):
        iTipOpens=[]
        for iTipShow in self.GetChildren():
            if type(iTipShow)==iTipFrame and iTipShow.id!=-1 and iTipShow.IsShown():
                iTipOpens.append(str(iTipShow.id))
                iTipOpenList='|'.join(iTipOpens)
                self.cfg.Write('openlist',iTipOpenList)
    
    # the code can't work while Systm ShutDown!          
    #def RecordOpen(self):
    #    iTipOpens=[]
    #    for iTipShow in self.GetChildren():
    #        if type(iTipShow)==iTipFrame and iTipShow.id!=-1 and iTipShow.IsShown():
    #            iTipOpens.append(str(iTipShow.id))
    #    iTipOpenList='|'.join(iTipOpens)
    #    self.cfg.Write('openlist',iTipOpenList)
    

    def DoOpen(self):
        if iTipApp.isiTipOpenOn:
            iTipids=[]
            temp=self.cfg.Read('openlist')
            if temp!='':
                iTipids=temp.split('|')
                for id in iTipids:
                    iTip=iTipWork().find(int(id))
                    iTipShow=wx.FindWindowById(1108).showiTip(iTip)
                    iTipShow.Show()
            
        