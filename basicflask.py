#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[ ]:


#instantiate the Flask app
app = Flask(__name__)

@app.route('/') #that's how you specify homepage/home directory
def hello():
    return 'hello kamil, this is your app'

if __name__=='__main__':
    app.run(debug=True)


# %%
