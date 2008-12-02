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


import wx.html

class iTipAbout(wx.Dialog):
    text = u'''<html><body bgcolor="#FFFFA8">
    <center><table bgcolor="#FFFFA8" width="100%" cellspacing="0"
cellpadding="0" border="0">
<tr>
    <td align="center"><h1>iTip</h1></td>
</tr>
</table>
</center>
<p><br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>iTip</b>是个简单易用的桌面便笺软件，开放源码。
使用的所有图片素材均来自互联网，遵循自由使用协议。
</p>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>iTip</b>采用Python编写，使用wxPython开发图形界面，
后台数据库为SQLite，并应用SQLAlchemy数据ORM框架。
源码仅供学习交流，使用者均需遵循GPL协议。
</p>
<p>
更多详情请访问http://www.xsmile.net 
</p>

<p>作者：xsmile, Copyright © 2008.</p>
</body>
</html>
    '''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, '关于 iTip',
                          size=(440, 400) )

        html = wx.html.HtmlWindow(self)
        
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, u"确定")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()
