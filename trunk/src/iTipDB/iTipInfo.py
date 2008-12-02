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


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relation, backref


import datetime,time

Base=declarative_base()

class Style(Base):
    """declarative of the Style object"""
    
    __tablename__ = 'iTipStyle'
    id = Column(Integer, primary_key=True)
    iTipsize_height = Column(Integer)
    iTipsize_width = Column(Integer)
    iTippos_x = Column(Integer)
    iTippos_y = Column(Integer)
    iTipfont = Column(String)
    isiTipMark = Column(Boolean)
    isiTipTop = Column(Boolean)
    isiTipChange = Column(Boolean)
    iTip_id = Column(Integer, ForeignKey('Information.id'))
    
    def __init__(self, iTipsize_height=0,iTipsize_width=0,iTippos_x=0,iTippos_y=0,iTipfont='',isiTipMark=False,isiTipTop=False,isiTipChange=False):
        self.iTipsize_height=iTipsize_height
        self.iTipsize_width=iTipsize_width
        self.iTippos_x=iTippos_x
        self.iTippos_y=iTippos_y
        self.iTipfont=iTipfont
        self.isiTipMark=isiTipMark
        self.isiTipTop=isiTipTop
        self.isiTipChange=isiTipChange


class Info(Base):
    
     """declarative of the Info object"""

     __tablename__ = 'Information'
     id = Column(Integer, primary_key=True)
     brief = Column(String(20))
     content = Column(Text)
     createdate = Column(DateTime)
     alarm = Column(DateTime)
     isRead =Column(Boolean)
     alarmstring = Column(String)
     style = relation(Style, uselist=False, backref="iTipStyle",cascade="all, delete-orphan",lazy=False, join_depth=2)
    
     def __init__(self, brief='', content='', \
                  createdate=datetime.datetime(*time.localtime()[:6]),\
                  alarm=datetime.datetime(*time.localtime()[:6]),isRead=True,alarmstring=''):
         self.brief = brief
         self.content = content
         self.createdate = createdate
         self.alarm = alarm
         self.isRead = isRead
         self.alarmstring=alarmstring
         
   