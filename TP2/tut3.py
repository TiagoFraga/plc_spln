from flair.embeddings import WordEmbeddings
from flair.data import Sentence
'''
# init embedding
glove_embedding = WordEmbeddings('glove')

# create sentence.
sentence = Sentence('The grass is green .')

# embed a sentence using glove.
glove_embedding.embed(sentence)

# now check out the embedded tokens.
for token in sentence:
    print(token)
    print(token.embedding)


pt_embedding = WordEmbeddings('pt')

'''

############

from flair.embeddings import CharacterEmbeddings

# init embedding
embedding = CharacterEmbeddings()

# create a sentence
sentence = Sentence('The grass is green .')

# embed words in sentence
embedding.embed(sentence)


###


from flair.embeddings import BytePairEmbeddings

# init embedding
embedding = BytePairEmbeddings('en')

# create a sentence
sentence = Sentence('The grass is green .')

# embed words in sentence
embedding.embed(sentence)

###



from flair.embeddings import WordEmbeddings, CharacterEmbeddings

# init standard GloVe embedding
glove_embedding = WordEmbeddings('glove')

# init standard character embeddings
character_embeddings = CharacterEmbeddings()



from flair.embeddings import StackedEmbeddings

# now create the StackedEmbedding object that combines all embeddings
stacked_embeddings = StackedEmbeddings(embeddings=[glove_embedding, character_embeddings])

sentence = Sentence('The grass is green .')

# just embed a sentence using the StackedEmbedding as you would with any single embedding.
stacked_embeddings.embed(sentence)

# now check out the embedded tokens.
for token in sentence:
    print(token)
    print(token.embedding)


