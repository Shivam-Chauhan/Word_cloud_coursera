#!/usr/bin/env python
# coding: utf-8

# In[22]:


import wordcloud
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_pattern():
    
    # Random words and made from these 54 alphabets 
    text=list('abcderfghijklmnopqrstuvwxyjABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    lengthcaptcha=8
    sentence=""
    # Character length is made to 8 
    while lengthcaptcha:
        indx=random.randint(0,53)  # Choosing random interger from 0 to length of list - 1
        random.shuffle(text)   # Shuffling of the list of aplhabets 
        sentence+=text[indx]   
        lengthcaptcha-=1

    # Wordcloud is generated with specified dimensions        
    wordcloud=WordCloud(width=50,height=50,background_color='white',min_font_size=1).generate(sentence) 
    # Plotting the patterns using matplotlib library
    plt.figure(figsize=(2,2), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    
    
if __name__=='__main__':
    generate_pattern()

