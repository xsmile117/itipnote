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
import threading


class AlarmTimer(wx.Timer):
    def __init__(self, iTip, sound='sound\\remind.wav',isPlay=True):
        wx.Timer.__init__(self)
        self.iTip=iTip
        self.sound=sound
        self.isPlay=isPlay
        
    def Notify(self):     
        iTipShow=wx.FindWindowById(1108).showiTip(self.iTip)
        iTipShow.shineTimer.Start(500)
        iTipShow.Show()
        iTipShow.Raise()
        th=SoundThread(self.sound,self.isPlay)
        th.start()
        
        
        
class SoundThread(threading.Thread):
    def __init__(self,sound,isPlay=True):
        threading.Thread.__init__(self)
        self.sound=sound
        self.isPlay=isPlay
        
    def run(self):
        if self.isPlay:
            PlaySound(self.sound).play()



class PlaySound:
    def __init__(self,wav=''):
        self.wav=wav
        
    def play(self):
        try:
            sound = wx.Sound(self.wav)
            sound.Play(wx.SOUND_SYNC)
        except NotImplementedError, v:
            pass
        
        

