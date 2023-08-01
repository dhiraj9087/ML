#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[11]:


import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford","nokia"],
  'passings': [3, 7, 2,4]
}

myvar=pandas.DataFrame(mydataset)           ###dataframe is collection of series
print(myvar)


# In[8]:


import pandas as pd
print(pd.__version__)


# In[24]:


a=[1,2,5]
myar=pd.Series(a)
print(myar)


# In[16]:


print(myar[1])


# In[21]:


a=[1,7,2]
my=pd.Series(a,index=["x","y","z"])        ##index for inserting
print(my)


# In[22]:


a=[1,7,2]
my=pd.Series(a,index=[["x","y","z"],["r","e","t"]])
print(my)


# In[25]:


print(my["y"])


# In[26]:


print(my["e"])


# In[3]:


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# In[31]:


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories,index=["day1","day2"])

print(myvar)


# import pandas as pd
# 
# calories = {"day1": 420, "day2": 380, "day3": 390}
# 
# myvar = pd.Series(calories,index=["day1","day2"])
# 
# print(myvar)

# In[7]:


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories,index=["day1","day","day4"])

print(myvar)
print(myvar[0])


# In[33]:


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


# In[38]:


print(df.loc[0])


# In[44]:


print(df.loc[[0,1]])


# In[50]:


import pandas as pd

data={
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

print(
# In[52]:


print(df.loc["day2"])


# In[56]:


df=pd.read_csv('data.csv')


# In[57]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())


# In[55]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())


# In[60]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df)
print(pd.options.display.max_rows)


# In[63]:


print(pd.options.display.max_rows)


# In[64]:


pd.options.display.max_rows=99999        ##increseing system number


# In[65]:


print(df)


# In[66]:


import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())


# In[70]:


import pandas as pd

df = pd.read_json('world.json')

print(df)


# In[73]:


import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)


# In[74]:


import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "6":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)


# In[79]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))


# In[80]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())


# In[81]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.tail(10))


# In[82]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())


# In[83]:


print(df.info())


# In[84]:


##cleaning data


# In[85]:


import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())


# In[87]:


print(new_df.info())


# In[88]:


print(df.info())


# In[89]:


print(df.duplicated())   ####return true for duplicate


# In[90]:


print(df.drop_duplicates(inplace=True))


# In[92]:


print(df.duplicated())


# In[96]:


df=pd.read_csv('data123.csv')


# In[97]:


df.corr


# In[98]:


df=pd.read_csv('data123.csv')
df.corr


# In[101]:


print(df.DataFrame)


# In[102]:


df=pd.read_csv('data123.csv')


# In[105]:


df.corr()


# In[106]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()


# In[14]:


import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("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")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        code = request.form["code"]
        lang = request.form["lang"]
        lang_conv = request.form["lang_conv"]
        response = openai.Completion.create(
        model="code-davinci-002",
        prompt=generate_prompt(lang, code, lang_conv),
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/test_writer", methods=("GET", "POST"))
def test_writer():
    if request.method == "POST":
        code = request.form["code"]
        lang = request.form["lang"]
        response = openai.Completion.create(
        model="code-davinci-002",
        prompt=generate_unit_test(lang, code),
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
        )
        return redirect(url_for("test_writer", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("test_writer.html", result=result)

@app.route("/code_explainer", methods=("GET", "POST"))
def code_explainer():
    if request.method == "POST":
        code = request.form["code"]
        response = openai.Completion.create(
        model="code-davinci-002",
        prompt=generate_general_prompt(code),
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
        )
        return redirect(url_for("code_explainer", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("code_explainer.html", result=result)

@app.route("/code_rewriter", methods=("GET", "POST"))
def code_rewriter():
    if request.method == "POST":
        code = request.form["code"]
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_general_prompt(code),
        temperature=0.2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return redirect(url_for("code_rewriter", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("code_rewriter.html", result=result)

@app.route("/arduino_code_writer", methods=("GET", "POST"))
def arduino_code_writer():
    if request.method == "POST":
        code_description = request.form["code_description"]
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_arduino_code_prompt(code_description),
        temperature=0.2,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return redirect(url_for("arduino_code_writer", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("arduino_code_writer.html", result=result)

@app.route("/problematic_code", methods=("GET", "POST"))
def problematic_code():
    if request.method == "POST":
        code = request.form["code"]
        behaviour = request.form["behaviour"]
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt_code_problem(code, behaviour),
        temperature=0.2,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return redirect(url_for("problematic_code", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("problematic_code.html", result=result)

def generate_prompt(lang, code, lang_conv):
    try:
        return """##### Translate this function from C++ into Python

### {}
{}
### {}
""".format(lang, code, lang_conv)
    except KeyError:
        return "Invalid C++ code"


def generate_unit_test(lang, code):
    try:
        return """# {}
{}

# Unit test""".format(lang, code)

    except KeyError:
        return "Invalid code"

def generate_general_prompt(code):
    try:
        return """{}""".format(code)

    except KeyError:
        return "Invalid code"

def generate_arduino_code_prompt(code_description):
    return """/* Write the Arduino Code to:
{} */""".format(code_description)

def generate_prompt_code_problem(code, behaviour):
    return """Why is the following code not working?
{}
It should: {}""".format(code, behaviour)


# In[ ]:




