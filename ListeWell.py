#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font



import sys
import os
import time
import glob
import os.path as path
import getpass
import shutil
import random
import math

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class ListeWell(swing.JFrame, swing.Scrollable):

				def __init__(self, listwell):
					swing.JFrame.__init__(self, title="Well")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__listwell = listwell
					self.run()

				def run(self):
					self.size = (200, 400)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
					label=swing.JLabel("")
					label.setText("Liste des Puits")
					Panel1.add(label)
					menu = swing.JMenuBar()
					Panel1.add(menu)
					
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					self.__listwell = swing.JList(listwell)
					Panel2.add(self.__listwell)
					barre = swing.JScrollPane(self.__listwell)
					Panel2.add(barre)
					
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel3.setBorder(line)
					select = swing.JButton("Select", actionPerformed=self.__select)
					Panel3.add(select)
					close = swing.JButton("Close", size=(100, 70), actionPerformed=self.__close)
					Panel3.add(close)


					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)




				def __select(self, event):
						print self.__listwell.getSelectedValues()

						
						
				def __close(self, event):
						time.sleep(0.01) 
						self.dispose()


if __name__ == "__main__":

	listwell=[]
	well1 = ("A1")
	well2 = ("A2")
	well3 = ("A3")
	well4 = ("A4")
	well5 = ("A5")
	well6 = ("A6")
	well7 = ("A7")
	well8 = ("A8")
	well9 = ("A9")
	well10 = ("A10")
	well11 = ("A11")
	well12 = ("A12")
	

	listwell=[well1,well2,well3,well4,well5,well6,well7,well8,well9,well10,well11,well12]
	
	well = ListeWell(listwell)
	well.show()


						