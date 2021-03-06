#!/usr/bin/env python 

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# file: main.py
# description: Implementation of a Simple MVC in Python 
#              that computes arithmetic operations.
# date: 15-05-14
# author: Victor Neville

from MVC.model import Model
from MVC.view import View
from MVC.controller import Controller

# Entry Point 
if __name__ == '__main__':
    Controller(View(), Model())
