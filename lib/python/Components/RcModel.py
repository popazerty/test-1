from boxbranding import getBoxType
from Tools.StbHardware import getFPVersion
import os

class RcModel:
	def __init__(self):
		pass

	def rcIsDefault(self):
		if self.getRcFolder() != 'dmm0':
			return False
		return True

	def readFile(self, target):
		fp = open(target, 'r')
		out = fp.read()
		fp.close()
		for x in out:
			return out.split()[0]
		return False
		
	def getRcFolder(self):
		remotefolder = 'dmm0'
		rc = self.readFile('/proc/stb/ir/rc/type')
		if os.path.exists('/etc/enigma2/EtRcType'):
			model = self.readFile('/etc/enigma2/EtRcType')
			if model == 'et6500':
				remotefolder = 'et6500'
			elif model == 'et9500':
				remotefolder = 'et9500'
			elif model == 'et8000' or model == 'et8500':
				remotefolder = 'et8000'
			elif model == 'et9000' or model == 'et9200':
				remotefolder = 'et9x00'
			elif model == 'et4000':
				remotefolder = 'et4x00'
			elif model == 'et6000':
				remotefolder = 'et6x00'
			elif model == 'et7000' or model == 'et7500':
				remotefolder = 'et7x00'
			return remotefolder
		
		else:
			if getBoxType() in ('et6500') and rc == '9':
				remotefolder = 'et6500'
			elif getBoxType() in ('et9500') and rc == '9':
				remotefolder = 'et9500'
			elif getBoxType() in ('et8000', 'et10000') and rc == '9':
				remotefolder = 'et8000'
			elif rc == '5':
				remotefolder = 'et9x00'
			elif rc == '7':
				remotefolder = 'et6x00'
			elif rc == '13':
				remotefolder = 'et4x00'
			elif rc == '11':
				remotefolder = 'et9x00'
			elif rc == '17':
				remotefolder = 'et8000'
			elif rc == '16':
				remotefolder = 'et7x00'

		return remotefolder

	def getRcLocation(self):
		baselocation = '/usr/share/enigma2/rc_models/'
		remotefolder = self.getRcFolder()
		return baselocation + remotefolder + '/'

rc_model = RcModel()
