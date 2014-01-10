from PIL import Image
import os

def convertImage(originName, method = 'binary'):
	datOut = ''
	img = Image.open(originName) 
	if method == 'binary':
		img = img.convert('1')
	else:
		img = img.convert('L')

	for j in range(img.size[1]):
		for i in range(img.size[0]):
			datOut += str(img.getpixel( (i, j) )) + ' '
		datOut += '\n'
	
	f = open(originName + '.dat', 'w')
	f.write(datOut)
	f.close()
	
if __name__ == '__main__':
	method = raw_input('method: ')
	files = os.listdir(os.getcwd())
	for f in files:
		if file.endswith('.bmp'):
			convertImage(file, method)

	
