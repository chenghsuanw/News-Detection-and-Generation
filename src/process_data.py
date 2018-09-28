import json
import os
import numpy as np

def process_news(path='../data/news/2018_content.json'):
	print('Processing news data...')

	with open(path) as f:
		json_data = json.load(f)

	news_list = []
	for year in json_data.keys():
		for month in json_data[year].keys():
			for day in json_data[year][month].keys():
				for news in json_data[year][month][day]:
					news_list.append(news)

	np.save('../data/news.npy', news_list)
	print('There are {} news in the corpus.'.format(len(news_list)))

def process_gossips(directory='../data/ptt-Gossiping'):
	print('Processing gossips data...')

	files = os.listdir(directory)
	files.sort()

	gossips_list = []
	for path in files:
		print('file: {}'.format(path))

		try:
			with open('{}/{}'.format(directory, path)) as f:
				json_data = json.load(f)
		except Exception:
			continue

		articles = json_data['articles']
		for article in articles:
			# 404 not found
			if 'error' in article:
				continue

			title = article['article_title']

			if title != None:
				if title.find('Re:') < 0 and title.find('[爆卦]') == 0:
					gossip = dict()
					gossip['title'] = title[4:].strip()
					gossip['content'] = article['content']
					gossip['date'] = article['date']
					gossip['author'] = article['author']
					gossips_list.append(gossip)

	np.save('../data/gossips.npy', gossips_list)
	print('There are {} gossips in the corpus.'.format(len(gossips_list)))

def main():
	process_news()
	process_gossips()

if __name__ == '__main__':
	main()

