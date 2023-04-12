import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
# from nltk.tokenize import WordPuncttokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer

sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking = nltk.RegexpParser(grammar)
parser_chunking.parse(sentence)
output = parser_chunking.parse(sentence)
output.draw()


# Sentences=['This is an example of Bag of Words model.', ' We can extract features by using Bag of Words model.']
# vector_count = CountVectorizer()
# features_text = vector_count.fit_transform(Sentences).todense()
# print(vector_count.vocabulary_)
document = ["One Geek helps Two Geeks",
            "Two Geeks help Four Geeks",
            "Each Geek helps many other Geeks at GeeksforGeeks"]
 
# Create a Vectorizer Object
vectorizer = CountVectorizer()
 
vectorizer.fit(document)
 
# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)
 
# Encode the Document
vector = vectorizer.transform(document)
 
# Summarizing the Encoded Texts
print("Encoded Document is:")
print(vector.toarray())