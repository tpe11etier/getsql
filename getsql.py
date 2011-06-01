#!/usr/bin/env python

from __future__ import print_function

#file = 'y:\\logs\\SQLLog.txt'
file = 'c:\\logs\\SQLLog.txt'
outfile = 'c:\\logs\SQLOut.txt'

def readfile():
	file_handle = open(file, "rb")
	outfile_handle = open(outfile, "wb")
	lines = file_handle.readlines()
	
	endIndex = len(lines)	
	startIndex = endIndex - 20
	lines = lines[startIndex:endIndex]
	outfile_handle.write(''.join(lines))
	print(lines)
	file_handle.close
	outfile_handle.close
	

def main():
	readfile()

		
if __name__ == '__main__':
	main()


