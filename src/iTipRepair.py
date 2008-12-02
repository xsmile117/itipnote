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


class iTipRepair(wx.App):
    def OnInit(self):
        config=wx.Config("iTipConfig")
        if config.Exists("isRun"):
            config.Write('openlist',"")
            run=config.ReadInt("isRun")
            if run==1:
                config.WriteInt("isRun",0)
                
                dlg = wx.MessageDialog(None, u'修复成功，请不要非法关闭iTip!',
                               u'提示',
                               wx.OK | wx.ICON_INFORMATION
                               )
                dlg.ShowModal()
                dlg.Destroy()
            else:
                dlg = wx.MessageDialog(None, u'iTip正常，无需修复!',
                               u'提示',
                               wx.OK | wx.ICON_INFORMATION
                               )
                dlg.ShowModal()
                dlg.Destroy()
        else:
            dlg = wx.MessageDialog(None, u'您还未运行iTip!',
                               u'提示',
                               wx.OK | wx.ICON_INFORMATION
                               )
            dlg.ShowModal()
            dlg.Destroy()
        return 1


# end of class iTipApp

if __name__ == "__main__":
    iTip = iTipRepair(0)