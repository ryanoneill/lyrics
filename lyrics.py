import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

english_stops = set(stopwords.words('english'))
tokenizer = RegexpTokenizer('\s+', gaps=True)

def print_freq_dist(name, filename):
  input_file = open(filename)
  lyrics = input_file.read()
  input_file.close()

  words = tokenizer.tokenize(lyrics)
  lower_words = [word.lower() for word in words]
  fdist = FreqDist(lower_words)

  print name, 'Lyrics Frequency Distribution:'
  print fdist

  filtered_stop_words = [word for word in lower_words if word not in english_stops]
  filtered_stop_fdist = FreqDist(filtered_stop_words)

  print name, 'Lyrics StopWords Filtered Frequency Distribution:'
  print filtered_stop_fdist

  filtered_contraction_words = [word for word in filtered_stop_words if word.find("'") == -1]
  filtered_contraction_fdist = FreqDist(filtered_contraction_words)

  print name, 'Lyrics Contractions Filtered Frequency Distribution:'
  print filtered_contraction_fdist
  print 


print_freq_dist('Bad Brains', 'BadBrainsLyrics.txt')
print_freq_dist('Cro-Mags', 'Cro-MagsLyrics.txt')
print_freq_dist('Gorilla Biscuits', 'GorillaBiscuitsLyrics.txt')