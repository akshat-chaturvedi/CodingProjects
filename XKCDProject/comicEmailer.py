#!/usr/bin/env python3

import bs4
from urllib.request import urlopen, Request
from emailer import sendMailWithAttachement
import logging
import os
import hashlib
from websiteChecker import read_last_hash, save_hash

def comicDownloader():
    url = "https://xkcd.com/"

    os.makedirs('xkcdComics', exist_ok=True)

    comicPage = Request(url)
    response = str(urlopen(comicPage).read())

    comicHTML = bs4.BeautifulSoup(response, 'html.parser')

    comicElement = comicHTML.select('#comic img')

    if comicElement == []:
        logging.info('Comic not found')

    else:
        comicURL = 'https:' + comicElement[0].get('src')
        comicImagePage = Request(comicURL)
        comicImagePage = urlopen(comicImagePage).read()

        dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'xkcdComics')
        fileName = os.path.join(dirPath, os.path.basename(comicURL))

        imageFile = open(fileName, 'wb')
        imageFile.write(comicImagePage)
        imageFile.close()
        logging.info('{} comic downloaded'.format(os.path.basename(comicURL)))

def webChecker(url: str, fileName: str):
    url = Request(url)
    response = urlopen(url).read()

    currentHash = hashlib.sha224(response).hexdigest()

    lastHash = read_last_hash(fileName)

    if currentHash == lastHash:
        logging.info('No new comic today')
        counter = 0

    else:
        save_hash(fileName, currentHash)
        counter = 1

    return counter

def comicEmailer():
    dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'xkcdComics')
    files = os.listdir(dirPath)

    fileTimes = []

    for f in files:
        fileTime = os.path.getctime(os.path.join(dirPath, f))
        fileTime = (f, fileTime)
        fileTimes.append(fileTime)

    fileTimes.sort(key=lambda x: x[1], reverse=True)

    subject = "Today's XKCD comic"
    body = "Here is today's XKCD comic"
    attachmentName = fileTimes[0][0]
    attachmentPath = os.path.join(dirPath, attachmentName)

    sendMailWithAttachement(subject, body, attachmentPath, attachmentName)
    logging.info('{} comic emailed'.format(os.path.basename(attachmentName)))

def main():
    hashDir = os.path.dirname(os.path.realpath(__file__))
    fileName = os.path.join(hashDir, 'XKCDHash.txt')

    updateStatus = webChecker("https://xkcd.com/", fileName)

    if updateStatus == 0:
        pass
    else:
        comicDownloader()
        comicEmailer()


if __name__ == '__main__':
    logDirPath = os.path.dirname(os.path.realpath(__file__))
    logFileName = os.path.join(logDirPath, 'comicLogs.log')

    logging.basicConfig(filename=logFileName,
                        encoding='utf-8',
                        format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=logging.INFO)
    main()