from PIL import Image
import os

def convertImage(originName, method = 'binary',inverted = False):
	datOut = ''
	img = Image.open(originName) 
	if method == 'binary':
		img = img.convert('1')
	else:
		img = img.convert('L')
	
	for j in range(img.size[1]):
		for i in range(img.size[0]):
			if not inverted:
				datOut += str(img.getpixel( (i, j) )) + ' '
			else:
				datOut += str(255 - img.getpixel( (i, j) )) + ' '
		datOut += '\n'
	return datOut
	
def createDatFile(originName, method = 'binary',inverted = False):
	data = convertImage(file, method, isInverted)
	f = open(originName + '.dat', 'w')
	f.write(data)
	f.close()
if __name__ == '__main__':
	method = raw_input('method: ')
	isInverted = raw_input('reverted: y/n: ') == 'y'
	files = os.listdir(os.getcwd())
	for f in files:
		if file.endswith('.bmp'):
			createDatFile(f, method, isInverted)

	
