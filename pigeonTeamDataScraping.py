#!/usr/bin/env python
# coding: utf-8

# ## Imports & Installs

# In[7]:


pip install beautifulsoup4


# In[11]:


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


# ## Initial MVP : Get Pigeon Team Titles from html

# In[47]:


path = 'PageOneHTML.html'


# In[48]:


soup = BeautifulSoup(open(path),'html.parser')


# In[49]:


listOfH3 = soup.find_all("h3")


# In[50]:


for heading in listOfH3:
    print(heading.text.strip())


# ## Official Code Start

# In[59]:


#soup.find_all("li")[0]


# In[143]:


firstTeam = soup.find_all("li")[0]


# In[98]:


def getTeamTitle(team):
    return team.find_all("h3")[0].text.strip()

getTeamTitle(firstTeam)


# In[88]:


def getTeamLocation(team):
    return team.find_all("div", class_="team_teamLocation__YRmqX")[0].text.strip()

getTeamLocation(firstTeam)


# In[94]:


def getTeamTechStack(team):
    techStackList = team.find_all("div", class_="MuiChip-root jss16 MuiChip-colorPrimary MuiChip-sizeSmall")
    techStack = []
    for tech in techStackList:
        techStack.append(tech.text.strip())
    techStackString = ', '.join(techStack)
    return techStackString
getTeamTechStack(firstTeam)


# In[95]:


def getTeamDescription(team):
  return team.find_all("div", class_="team_descriptionText__2Blxi")[0].text.strip()

getTeamDescription(firstTeam)


# In[ ]:





# In[144]:


pd.set_option('display.max_colwidth', None) #So pandas doesn't truncate team names and descriptions


# In[150]:


pigeonTeamDB = pd.DataFrame(columns=['Team Name', "Location", "Tech Stack", "Description"])


# In[151]:


for team in soup.find_all("li"):
    teamName = getTeamTitle(team)
    location = getTeamLocation(team)
    techStack = getTeamTechStack(team)
    description = getTeamDescription(team)   
    pigeonTeamDB = pigeonTeamDB.append({'Team Name': teamName, 'Location': location, 'Tech Stack': techStack, 'Description': description}, ignore_index=True)


# In[152]:


pigeonTeamDB


# In[149]:


pigeonTeamDB.iloc[:1]


# ## Final CSV

# In[160]:


finalPath = 'allPigeonTeams.html'


# In[161]:


fullSoup = BeautifulSoup(open(finalPath),'html.parser')


# In[162]:


allPigeonTeamDB = pd.DataFrame(columns=['Team Name', "Location", "Tech Stack", "Description"])


# In[163]:


for team in fullSoup.find_all("li"):
    teamName = getTeamTitle(team)
    location = getTeamLocation(team)
    techStack = getTeamTechStack(team)
    description = getTeamDescription(team)   
    allPigeonTeamDB = allPigeonTeamDB.append({'Team Name': teamName, 'Location': location, 'Tech Stack': techStack, 'Description': description}, ignore_index=True)


# In[164]:


allPigeonTeamDB


# In[166]:


allPigeonTeamDB.to_csv('pigeonTeamsSecondRotation.csv', index=False)

