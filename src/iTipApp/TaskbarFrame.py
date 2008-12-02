# -*- coding: utf-8 -*-
#!/usr/bin/python

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

from iTipApp.AboutFrame import iTipAbout
class iTipTaskBar(wx.TaskBarIcon):
    def __init__(self, frame,sframe):
        wx.TaskBarIcon.__init__(self)

        self.frame = frame
        self.sframe = sframe
        
        self.SetIcon(wx.Icon('pic\\iTip.png', wx.BITMAP_TYPE_PNG), 'iTip')
        self.Bind(wx.EVT_MENU, self.OniTipActivate, id=1)
        #self.Bind(wx.EVT_MENU, self.OniTipDeactivate, id=2)
        self.Bind(wx.EVT_MENU, self.OniTipAbout, id=4)
        self.Bind(wx.EVT_MENU, self.OniTipClose, id=5)
        self.Bind(wx.EVT_MENU, self.OniTipSetShow, id=3)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, u'悬浮显示')
        #menu.Append(2, u'隐藏')
        menu.AppendSeparator() 
        menu.Append(3, u'便笺管理')
        menu.Append(4, u'关于')
        menu.AppendSeparator() 
        menu.Append(5, u'退出')
        return menu

    def OniTipClose(self, event):
        
        self.frame.Close()
        self.Destroy()


    def OniTipActivate(self, event):
        if not self.frame.IsShown():
            self.frame.Show()
        else:
            self.frame.Raise()
            

    def OniTipDeactivate(self, event):
        if self.frame.IsShown():
            self.frame.Hide()
    
    def OniTipSetShow(self,event):
        if not self.sframe.IsShown():
            self.sframe.Show()
        else:
            self.sframe.Raise()
            
    def OniTipAbout(self,event):
        about=iTipAbout(None)
        about.ShowModal()
        about.Destroy()

