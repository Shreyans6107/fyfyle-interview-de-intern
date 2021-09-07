# Your imports go here
import logging
import re
import os
import json

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

	logger.info('extract_amount called for dir %s', dirpath)

	for x in os.listdir(dirpath):
		if 'ocr' in x:
			with open(os.path.join(dirpath, x)) as f:
				data = json.load(f)
	prices = []
	for x in data['Blocks']:
		if x.get('Text'):
			if re.search(r'[0-9]*\.[0-9][0-9]', x['Text']):
				prices.append(float(re.sub("[^0-9.]", '', x['Text'])))
	return max(prices)
