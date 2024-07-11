import string
text = """
Got this panda plush toy for my daughter's birthday, 
who loves it and takes it everywhere. It's soft and 
super cute, and its face has a friendly look. It's 
a bit small for what I paid though. I think there 
might be other options that are bigger for the 
same price. It arrived a day earlier than expected, 
so I got to play with it myself before I gave it 
to her.
"""
def wordcount(text):
    text=text.translate(str.maketrans('','',string.punctuation))
    text=text.lower()
    words=text.split()
    count={}
    for word in words:
        count[word]=count.get(word,0)+1
    return count

text="""Hello world!  
This is an example.  
Word count is fun.  
Is it fun to count words?  
Yes, it is fun!"""
result=wordcount(text)
print(result)