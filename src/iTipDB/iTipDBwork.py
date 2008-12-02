# coding=gbk

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


"""数据库操作封装
@author:xsmile
@contact:http://www.xsmile.net
"""

from iTipDB import Session
import iTipInfo
from sqlalchemy.orm import join
class iTipDB():
    """数据库基本操作"""  
    def Create(self,iTipInfo):
        """添加一个iTipInfo到数据库"""
        session=Session()
        session.add(iTipInfo)
        session.commit()
        session.close()
        
    def Research(self,content=''):
        """按内容关键字查找，并返回iTipInfo的集合"""
        session=Session()
        key=content
        results=session.query(iTipInfo.Info).filter(iTipInfo.Info.content.like('%'+key+'%')).all()
        session.close()
        return results
    
    def Update(self,iTipInfo):
        """更新iTipInfo"""
        session=Session()
        session.update(iTipInfo)
        session.commit()
        session.close()
        
    def Delete(self,iTipInfo):
        """删除iTipInfo"""
        session=Session()
        session.delete(iTipInfo)
        session.commit()
        session.close()
        
    def Find(self,iTipId):
        """按iTipInfo的id查找"""
        session=Session()
        id=iTipId
        result=session.query(iTipInfo.Info).filter(iTipInfo.Info.id==id).first()
        session.close()
        return result
        
