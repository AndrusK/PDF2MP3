import argparse
import pyttsx3
import PyPDF2

pdf = ""
mp3 = ""
start_page = ""

parser = argparse.ArgumentParser(description='Generates .mp3 from .pdf files.')
parser.add_argument("--pdf","-i", action='store', dest='pdf')
parser.add_argument("--mp3","-o", action='store', dest='mp3')
parser.add_argument("--start","-p", action='store', dest='start_page')
args = parser.parse_args()

if args.pdf is None or args.mp3 is None or args.start_page is None:
    parser.error("One or more of the arguments were not used corretly.")
if ".pdf" in args.pdf:
    pdf = args.pdf
else:
    parser.error("PFD file must have the extension '.pdf'")
if ".mp3" in args.mp3:
    mp3 = args.mp3
else:
    mp3 = args.mp3 + ".mp3"
if args.start_page.strip().isdigit():
    start_page = int(args.start_page) - 1
else:
    parser.error('Page number was not properly formatted.')

book = open(pdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init('nsss')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')  

whole_book_txt = ""

for num in range(start_page, pages):
    whole_book_txt += pdfReader.getPage(num).extractText()
speaker.save_to_file(whole_book_txt, mp3)
speaker.runAndWait()
