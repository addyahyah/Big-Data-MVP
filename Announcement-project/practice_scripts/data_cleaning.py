from bs4 import BeautifulSoup
import re
# If the stopwords set does not exist, run the lines below
# import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords


# This function is from Kaggle Bag of Words Meets Bags of Popcorn
def email_to_words( raw_email ):
	#remove newline characters
	review_text = BeautifulSoup(raw_email).get_text()
	# 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
     # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split() 
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english")) 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))  