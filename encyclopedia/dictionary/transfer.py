import logging
import sys
import re
from django.core.files import File
from konlpy.tag import Kkma, Twitter, Mecab, Komoran


reload(sys)
sys.setdefaultencoding('utf-8')
morphsMaker = Twitter()

genesisFirst = []

logger = logging.getLogger(__name__)
PATH = "/usr/local/web/encyclopedia/dictionary/"

def flat(content):
	return ["{}/{}".format(word, tag) for (word, tag) in content]

def flatOne(content):
	return ["{}".format(tag) for (word, tag) in content]

with open(PATH+"genesis1.txt","r") as holyBible:
	for item in holyBible:
		item = item.strip()
		item = re.sub("\d+","",item)
		item = re.sub("[.,\/#!$%\^&\*;:{}=\-_`~()]","",item)
		genesisFirst.append(item)	

genesisChunks = []
for item in genesisFirst:
	if len(item) != 0:
		genesisChunks.append(morphsMaker.pos(item))
	
with open(PATH+"genesis1p.txt","w") as pholyBible:
	pholyBible.seek(0)
	for item in genesisChunks:
		pholyBible.write(' '.join(flat(item)))
		pholyBible.write("\n")	

with open(PATH+"genesis2p.txt","w") as pholyBible:
	pholyBible.seek(0)
	for item in genesisChunks:
		pholyBible.write(' '.join(flatOne(item)))
		pholyBible.write("\n")

