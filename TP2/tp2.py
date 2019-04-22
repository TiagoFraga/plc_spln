from flair.models import SequenceTagger
from flair.data import Sentence

print("#####################################")
print("############    NER   ###############")
print("#####################################")

# load ner model
tagger = SequenceTagger.load('ner')

# example sample
sentence = Sentence('George Washington went to Washington .')

# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
print(sentence.to_tagged_string())

for entity in sentence.get_spans('ner'):
    print(entity)

print(sentence.to_dict(tag_type='ner'))




#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################





print("#####################################")
print("##########    FRAME   ###############")
print("#####################################")

# load frame model
tagger = SequenceTagger.load('frame')

# make sentence
sentence_1 = Sentence('George returned to Berlin to return his hat .')
sentence_2 = Sentence('He had a look at different hats .')

# predict NER tags
tagger.predict(sentence_1)
tagger.predict(sentence_2)

# print sentence with predicted tags
print(sentence_1.to_tagged_string())
print(sentence_2.to_tagged_string())






#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################





print("#####################################")
print("##########  TAGGER    ###############")
print("#####################################")


# your text of many sentences
text = "This is a sentence. This is another sentence. I love Berlin."

# use a library to split into sentences
from segtok.segmenter import split_single
sentences = [Sentence(sent, use_tokenizer=True) for sent in split_single(text)]

# predict tags for list of sentences
tagger: SequenceTagger = SequenceTagger.load('ner')
tagger.predict(sentences)

for sentence in sentences:
    print("###")
    print(sentence.to_tagged_string())

    for entity in sentence.get_spans('ner'):
        print(entity)

    print(sentence.to_dict(tag_type='ner'))









#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################






print("#####################################")
print("##########  EMOTIONS   ##############")
print("#####################################")

from flair.models import TextClassifier

# load sentiment model
classifier = TextClassifier.load('en-sentiment')

# example sentence
sentence = Sentence('Porto wins. I am happy')

# predict NER tags
classifier.predict(sentence)

# print sentence with predicted labels
print(sentence.labels)




