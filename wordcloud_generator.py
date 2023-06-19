from wordcloud import WordCloud
import matplotlib.pyplot as plt

# The text for the word cloud
text = """
Python is a powerful programming language that is used for various applications.
Python is widely used in data science, web development, automation, and much more.
With Python, you can analyze data, create web applications, automate repetitive tasks, etc.
Python is known for its simplicity and readability, which makes it a popular choice for beginners.
"""

# Generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated image using matplotlib
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()