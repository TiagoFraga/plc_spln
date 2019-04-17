from flair.data import TaggedCorpus
from pathlib import Path
from flair.data_fetcher import NLPTaskDataFetcher, NLPTask

'''

# define columns
columns = {0: 'text', 1: 'pos', 2: 'ner'}

# this is the folder in which train, test and dev files reside
data_folder = '/path/to/data/folder'

# retrieve corpus using column format, data folder and the names of the train, dev and test files
corpus: TaggedCorpus = NLPTaskDataFetcher.load_column_corpus(data_folder, columns,
                                                              train_file='train.txt',
                                                              test_file='test.txt',
                                                              dev_file='dev.txt')


len(corpus.train)

print(corpus.train[0].to_tagged_string('pos'))
print(corpus.train[0].to_tagged_string('ner'))

from flair.data_fetcher import NLPTaskDataFetcher


# use your own data path
data_folder = Path('/resources/tasks/imdb')

# load corpus containing training, test and dev data
corpus: TaggedCorpus = NLPTaskDataFetcher.load_classification_corpus(data_folder,
                                                                     test_file='test.txt',
                                                                     dev_file='dev.txt',
                                                                     train_file='train.txt')


corpus: TaggedCorpus = NLPTaskDataFetcher.load_corpus(NLPTask.IMDB)
'''


original_corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_ENGLISH)

downsampled_corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_ENGLISH).downsample(0.1)

print("--- 1 Original ---")
print(original_corpus)

print("--- 2 Downsampled ---")
print(downsampled_corpus)


# create tag dictionary for a PoS task
corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_ENGLISH)
print(corpus.make_tag_dictionary('upos'))

# create tag dictionary for an NER task
#corpus = NLPTaskDataFetcher.load_corpus(NLPTask.CONLL_03_DUTCH)
#print(corpus.make_tag_dictionary('ner'))

# create label dictionary for a text classification task
#corpus = NLPTaskDataFetcher.load_corpus(NLPTask.TREC_6)
#print(corpus.make_label_dictionary())

stats = corpus.obtain_statistics()
print(stats)


'''
##### MultiCorpus
english_corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_ENGLISH)
german_corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_GERMAN)
dutch_corpus = NLPTaskDataFetcher.load_corpus(NLPTask.UD_DUTCH)

multi_corpus = MultiCorpus([english_corpus, german_corpus, dutch_corpus])
'''



