import glob
import os


def combine(ext):
	try:
		os.remove("combined."+ext)
	except:
		pass

	globSearch = "*." + ext
	
	f = open("combined."+ext,'wb')
	for file in sorted(glob.glob(globSearch)):
		g = open(file,'r')
		f.write(g.read())
		g.close()
	f.close()

def main():
	combine("gcode")
	
if __name__ == "__main__": main()