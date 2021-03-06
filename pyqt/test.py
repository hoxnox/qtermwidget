#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PyQt4 bindings for th QTermWidget project.
#
# Copyright (C) 2009 Piotr "Riklaunim" Maliński <riklaunim@gmail.com>,
#                    Alexander Slesarev <alex.slesarev@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, signal
from PyQt5 import QtCore,QtWidgets

import QTermWidget

signal.signal(signal.SIGINT, signal.SIG_DFL)
a = QtWidgets.QApplication(sys.argv)

w = QTermWidget.QTermWidget()
w.finished.connect(a.quit)
w.show()

a.exec_()