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

"""DataBase Configuration
@author:xsmile
@contact:http://www.xsmile.net
"""

from sqlalchemy import *
from sqlalchemy.orm import *

import iTipInfo

#iTipDB Configuration
db=create_engine('sqlite:///iTipDB.db')
metadata=iTipInfo.Base.metadata
metadata.create_all(db,checkfirst=True)
Session=sessionmaker(bind=db)