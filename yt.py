import argparse
import youtube_dl
import ffmpeg

def getm3u8(url):
	print(url)
	yl = youtube_dl.YoutubeDL({'format': 'best'})
	quality = yl.extract_info(url, download=False)

	m3u8 = quality['url']
	return m3u8

def downloadVideo(filename, m3u8):
	stream = ffmpeg.input(m3u8)
	stream = ffmpeg.output(stream, filename)
	ffmpeg.run(stream)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", dest='url', help="url")
	parser.add_argument("-f", dest='filename', help="filename")
	args = parser.parse_args()

	if args.url:
		m3u8 = getm3u8(args.url)

	if args.filename:
		downloadVideo(args.filename, m3u8)

if __name__ == '__main__':
	main()
