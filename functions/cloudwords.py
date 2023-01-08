import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

def show_wordcloud(text):
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='blue', collocations=False, stopwords = STOPWORDS).generate(text)
    # text is the input to the generate() method
    #draw the figure
    #Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis 
    plt.axis("off")
    plt.show()