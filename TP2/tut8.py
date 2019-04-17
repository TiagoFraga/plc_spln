'''
from flair.data import TaggedCorpus
from flair.data_fetcher import NLPTaskDataFetcher, NLPTask

# load your corpus
corpus: TaggedCorpus = NLPTaskDataFetcher.load_corpus(NLPTask.AG_NEWS, base_path='/resources/tasks/ag_news')

from hyperopt import hp
from flair.hyperparameter.param_selection import SearchSpace, Parameter

# define your search space
search_space = SearchSpace()
search_space.add(Parameter.EMBEDDINGS, hp.choice, options=[
    [ WordEmbeddings('en') ], 
    [ CharLMEmbeddings('news-forward'), CharLMEmbeddings('news-backward') ]
])
search_space.add(Parameter.HIDDEN_SIZE, hp.choice, options=[32, 64, 128])
search_space.add(Parameter.RNN_LAYERS, hp.choice, options=[1, 2])
search_space.add(Parameter.DROPOUT, hp.uniform, low=0.0, high=0.5)
search_space.add(Parameter.LEARNING_RATE, hp.choice, options=[0.05, 0.1, 0.15, 0.2])
search_space.add(Parameter.MINI_BATCH_SIZE, hp.choice, options=[8, 16, 32])

search_space.add(Parameter.EMBEDDINGS, hp.choice, options=[
    [ CharLMEmbeddings('news-forward'), CharLMEmbeddings('news-backward') ]
])

from flair.hyperparameter.param_selection import TextClassifierParamSelector, OptimizationValue

# create the parameter selector
param_selector = TextClassifierParamSelector(
    corpus, 
    False, 
    'resources/results', 
    'lstm',
    max_epochs=50, 
    training_runs=3,
    optimization_value=OptimizationValue.DEV_SCORE
)

# start the optimization
param_selector.optimize(search_space, max_evals=100)

'''

from flair.data import TaggedCorpus
from flair.data_fetcher import NLPTaskDataFetcher, NLPTask
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings
from flair.trainers import ModelTrainer
from typing import List

# 1. get the corpus
corpus: TaggedCorpus = NLPTaskDataFetcher.load_corpus(NLPTask.CONLL_03).downsample(0.1)
print(corpus)

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)

# 4. initialize embeddings
embedding_types: List[TokenEmbeddings] = [
    WordEmbeddings('glove'),
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)

# 6. initialize trainer
trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. find learning rate
learning_rate_tsv = trainer.find_learning_rate('resources/taggers/example-ner',
                                                    'learning_rate.tsv')

# 8. plot the learning rate finder curve
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_learning_rate(learning_rate_tsv)


from torch.optim.adam import Adam

trainer: ModelTrainer = ModelTrainer(tagger, corpus,
                                     optimizer=Adam, weight_decay=1e-4)


from flair.optim import SGDW

trainer: ModelTrainer = ModelTrainer(tagger, corpus,
                                     optimizer=SGDW, momentum=0.9)

