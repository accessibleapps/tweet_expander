import re
import twitlonger
import twishort

class TweetExpander(object):

	def __init__(self):
		self.twitlonger_API = twitlonger.TwitLongerAPI()
		self.twishort_API = twishort.TwishortAPI()

	def retrieve_text(self, url):
		for (regexp, processor) in self.matches.iteritems():
			if not regexp.search(url):
				continue
			return processor(self, url)

	def is_shortened(self, url):
		for regexp in self.matches.iterkeys():
			if regexp.search(url):
				return True
		return False

	def expand_twishort(self, url):
		return self.twishort_API.get_text(url)

	def expand_twitlonger(self, url):
		return self.twitlonger_API.get_text(url)

	matches = {
		re.compile(r'^http://(?:www\.)?twishort.com/\w+$'): expand_twishort,
		re.compile(r'^http://(?:www\.)?tl.gd/\w+$'): expand_twitlonger,
		re.compile(r'^http://(?:www\.)?twitlonger.com/show/\w+$'): expand_twitlonger,
	}
