#!/usr/bin/env python3

import requests
import os
import dotenv
from datetime import date
import logging
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'XKCDProject'))

from emailer import sendMailWithAttachement

dotenv.load_dotenv('.env')

def downloadAPOD(apiKey, date=None):
    os.makedirs('APODImages', exist_ok=True)

    baseURL = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": apiKey}

    if date:
        params["date"] = date

    response = requests.get(baseURL, params=params)
    response.raise_for_status()
    data = response.json()

    imageURL = data["url"]
    imageTitle = data["title"]

    # Download the image
    image_response = requests.get(imageURL)
    image_response.raise_for_status()

    imageName = os.path.join('APODImages', f"{imageTitle}.jpg")
    with open(imageName, "wb") as image_file:
        image_file.write(image_response.content)

    logging.info("{} has been downloaded".format(imageTitle))

def APODEmailer():
    dirPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'APODImages')
    files = os.listdir(dirPath)

    fileTimes = []

    for f in files:
        fileTime = os.path.getctime(os.path.join(dirPath, f))
        fileTime = (f, fileTime)
        fileTimes.append(fileTime)

    fileTimes.sort(key=lambda x: x[1], reverse=True)

    subject = "Today's APOD"
    body = "Here is today's APOD"
    attachmentName = fileTimes[0][0]
    attachmentPath = os.path.join(dirPath, attachmentName)

    sendMailWithAttachement(subject, body, attachmentPath, attachmentName)
    logging.info('{} emailed'.format(os.path.basename(attachmentName)))

    fileNames = [time[0] for time in fileTimes]
    if len(fileNames) > 1:
        for fileName in fileNames:
            if fileName != ".DS_Store" and fileName != attachmentName:
                os.remove('APODImages/{}'.format(fileName))
                logging.info("{} has been deleted".format(fileName))


if __name__ == "__main__":
    logDirPath = os.path.dirname(os.path.realpath(__file__))
    logFileName = os.path.join(logDirPath, 'APODLogs.log')

    logging.basicConfig(filename=logFileName,
                        encoding='utf-8',
                        format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=logging.INFO)

    api_key = os.getenv("APOD_API")
    date = date.today()

    downloadAPOD(api_key, date)
    APODEmailer()