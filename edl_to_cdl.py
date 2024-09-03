#!/usr/bin/env python 
_version = "1.2"
import os
import re
import sys


print ("EDL-to-CDL Conversion Utility version "+_version)

from PyQt5 import QtWidgets
from EDLtoCDLUi import Ui_EDL_TO_CDL

class EDL_TO_CLD(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		
		self.ui = Ui_EDL_TO_CDL()
		self.ui.setupUi(self)
		self.setWindowTitle('EDL TO CDL')

		self.edl_file = None
		self.export_folder = None
		self.export_type = self.set_export_type()

		self.ui.buttonBox.accepted.connect(self.Export)
		self.ui.buttonBox.rejected.connect(self.close)
		self.ok_button = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
		self.ok_button.setEnabled(False)
		self.ui.comboBox.currentIndexChanged.connect(self.set_export_type)

		self.ui.toolButton.released.connect(self.get_cdl)
		self.ui.toolButton_3.released.connect(self.get_export_folder)

	def set_export_type(self):
		self.export_type = self.ui.comboBox.currentText()
		return self.export_type
	
	def get_cdl(self):
        
        # Open file dialog with the custom filter
		file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select CDL File", "", "CMX3600-like Edit Decision List (EDL) file (*.edl)")

		if file_path:
			self.edl_file = file_path
		else:
			self.export_folder = None

		self.ui.lineEdit.setText(self.edl_file)
		self.check_ready()
		return self.edl_file
	
	
	def check_ready(self):
		if self.edl_file and self.export_folder:
			self.ok_button.setEnabled(True)
		else:
			self.ok_button.setEnabled(False)


	def get_export_folder(self):
		folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
		if folder_path:
			self.export_folder = folder_path
		else:
			self.export_folder = None

		self.check_ready()
		self.ui.lineEdit_3.setText(self.export_folder)
		return self.export_folder
	
	def Export(self):
		
		camre = re.compile(r"[*]\sFROM\sCLIP\sNAME:\s+.*(?P<name>[A-Z][0-9]{3}[_]?C[0-9]{3})")
		camre0 = re.compile(r"[*]\sFROM\sCLIP\sNAME:\s+(?P<name>.{63})")
		camre1 = re.compile(r"[*]\s(?P<name>.*)")
		input_desc, viewing_desc = None, "EDL2CDL script by Walter Arrighetti"
		tapere = re.compile(r"[*]\sFROM\sCLIP\sNAME:\s+(?P<name>[A-Za-z0-9-_,.]|\s{8,32})")
		cdl1re = re.compile(r"[*]\sASC[_]SOP\s+[(]\s?(?P<sR>[-]?\d+[.]\d{4,6})\s+(?P<sG>[-]?\d+[.]\d{4,6})\s+(?P<sB>[-]?\d+[.]\d{4,6})\s?[)]\s?[(]\s?(?P<oR>[-]?\d+[.]\d{4,6})\s+(?P<oG>[-]?\d+[.]\d{4,6})\s+(?P<oB>[-]?\d+[.]\d{4,6})\s?[)]\s?[(]\s?(?P<pR>[-]?\d+[.]\d{4,6})\s+(?P<pG>[-]?\d+[.]\d{4,6})\s+(?P<pB>[-]?\d+[.]\d{4,6})\s?[)]\s?")
		cdl2re = re.compile(r"[*]\sASC[_]SAT\s+(?P<sat>\d+[.]\d{4,6})")

		ln = 0

		CCC, IDs = [], []

		def writeCDL(CCCid, SOPnode, SATnode):
			CCC.append( {
				'id': CCCid,
				'slope': SOPnode[0],
				'offset':SOPnode[1],
				'power': SOPnode[2],
				'SAT':   SATnode
			} )
			IDs.append(CCCid)

		if (self.export_type in ["CDL","CC"]) and ((not os.path.exists(self.export_folder)) or (not os.path.isdir(self.export_folder))):
			try:	os.mkdir(self.export_folder)
			except:
				print (" * ERROR!: Unable to create output folder : "+self.export_folder)
				sys.exit(2)
		tapename, CDLevent, thisCDL, thisSAT = None, False, None, 0
		try:	EDL = open(self.edl_file,"r").readlines()
		except:
				print (" * ERROR!: Unable to read input EDL file : "+self.edl_file)
				sys.exit(3)
		for n in range(len(EDL)):
			line = EDL[n].strip()
			if camre.match(line):
				CDLevent, L = True, camre.match(line)
				if thisCDL:
					writeCDL(tapename,thisCDL,thisSAT)
					thisCDL, thisSAT = None, 0
				tapename = L.group("name")
				if tapename in IDs:	tapename, CDLevent = None, False
			elif camre0.match(line) and n<len(EDL)-1 and camre1.match(EDL[n+1]):
				n += 1
				line = line + camre1.match(EDL[n]).group("name")
				L = camre.match(line)
				if not L:
					writeCDL(tapename,thisCDL,thisSAT)
					thisCDL, thisSAT = None, 0
				else:	CDLevent = True
				tapename = L.group("name")
				if tapename in IDs:	tapename, CDLevent = None, False
				if thisCDL:
					thisCDL, thisSAT = None, 0
			elif tapere.match(line):
				CDLevent, L = True, tapere.match(line)
				if thisCDL:
					writeCDL(tapename,thisCDL,thisSAT)
					thisCDL, thisSAT = None, 0
				tapename = L.group("name")
				if tapename in IDs:	tapename, CDLevent = None, False
			elif CDLevent and cdl1re.match(line):
				L = cdl1re.match(line)
				thisCDL = ( tuple(map(float,(L.group("sR"),L.group("sG"),L.group("sB")))), tuple(map(float,(L.group("oR"),L.group("oG"),L.group("oB")))), tuple(map(float,(L.group("pR"),L.group("pG"),L.group("pB")))) ) 
				thisSAT = 0
			elif CDLevent and thisCDL and cdl2re.match(line):
				L = cdl2re.match(line)
				thisSAT = float(L.group("sat"))
				writeCDL(tapename,thisCDL,thisSAT)
				tapename, CDLevent, thisCDL, thisSAT = None, False, None, 0
		if thisCDL:
			writeCDL(tapename,thisCDL,thisSAT)
			tapename, CDLevent, thisCDL, thisSAT = None, False, None, 0
		if not CCC:
			print ("No Color Decision(s) found in EDL file :"+os.path.split(self.edl_file)[1]+". Quitting.")
			sys.exit(0)
		print (" * "+ str(len(CCC)) + "Color Decision(s) found in EDL file : "+os.path.split(self.edl_file)[1])

		if self.export_type=="CCC":
			try:	CCCout = open(outfile,"w")
			except:
				print (" * ERROR!: Unable to create output CCC file : "+outfile)
				sys.exit(3)
			buf = []
			buf.append('<?xml version="1.0" encoding="UTF-8"?>')
			buf.append('<ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.01">')
			if input_desc:	buf.append('\t<InputDescription>%s</InputDescription>'%input_desc)
			if viewing_desc:	buf.append('\t<ViewingDescription>%s</ViewingDescription>'%viewing_desc)
			for n in range(len(CCC)):
				buf.append('\t<ColorCorrection id="%s">'%CCC[n]['id'])
				buf.append('\t\t<SOPNode>')
				buf.append('\t\t\t<Slope>%.05f %.05f %.05f</Slope>'%CCC[n]['slope'])
				buf.append('\t\t\t<Offset>%.05f %.05f %.05f</Offset>'%CCC[n]['offset'])
				buf.append('\t\t\t<Power>%.05f %.05f %.05f</Power>'%CCC[n]['power'])
				buf.append('\t\t</SOPNode>')
				buf.append('\t\t<SatNode>')
				buf.append('\t\t\t<Saturation>%.05f</Saturation>'%CCC[n]['SAT'])
				buf.append('\t\t</SatNode>')
				buf.append('\t</ColorCorrection>')
			buf.append('</ColorCorrectionCollection>')
			CCCout.write('\n'.join(buf))
			CCCout.close()
			print (" * "+str(len(CCC)) +" CDL(s) written in CCC file : "+os.path.split(outfile)[1])
		elif self.export_type in ["CC","CDL"]:
			for n in range(len(CCC)):
				outfile = os.path.join(self.export_folder,CCC[n]['id'])
				if self.export_type=="CDL":	outfile += ".cdl"
				else:	outfile += ".cc"
				try:	CDLout = open(outfile,"w")
				except:
					print (" * ERROR!: Unable to create output CDL file : "+outfile)
				buf = []
				if self.export_type=="CDL":
					buf.append('<?xml version="1.0" encoding="UTF-8"?>')
					buf.append('<ColorDecisionList xmlns="urn:ASC:CDL:v1.01">')
					tab = '\t'
				else:	tab = ''
				buf.append(tab+'<ColorCorrection id="%s">'%CCC[n]['id'])
				if input_desc:	buf.append(tab+'\t<InputDescription>%s</InputDescription>'%input_desc)
				if viewing_desc:	buf.append(tab+'\t<ViewingDescription>%s</ViewingDescription>'%viewing_desc)
				buf.append(tab+'\t<SOPNode>')
				buf.append(tab+'\t\t<Slope>%.05f %.05f %.05f</Slope>'%CCC[n]['slope'])
				buf.append(tab+'\t\t<Offset>%.05f %.05f %.05f</Offset>'%CCC[n]['offset'])
				buf.append(tab+'\t\t<Power>%.05f %.05f %.05f</Power>'%CCC[n]['power'])
				buf.append(tab+'\t</SOPNode>')
				buf.append(tab+'\t<SatNode>')
				buf.append(tab+'\t\t<Saturation>%.05f</Saturation>'%CCC[n]['SAT'])
				buf.append(tab+'\t</SatNode>')
				buf.append(tab+'</ColorCorrection>')
				if self.export_type=="CDL":
					buf.append('</ColorDecisionList>')
				CDLout.write('\n'.join(buf))
				CDLout.close()
			print (" * "+str(len(CCC))+" individual "+self.export_type+"(s) written in folder "+self.export_folder+".")
		else:
			print (" * ERROR!: Invalid Color Decision List mode '"+self.export_type+"'; quitting.")
			sys.exit(9)

app = QtWidgets.QApplication(sys.argv)
application = EDL_TO_CLD()
application.show()
sys.exit(app.exec_())