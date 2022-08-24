#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[22]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[23]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[24]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[25]:


slide_elem


# In[26]:


slide_elem.find('div', class_='content_title')


# In[27]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[28]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[29]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[30]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[31]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[32]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[33]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[34]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.head()


# In[35]:


# df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[36]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[37]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[38]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css('a.product-item img')

for i in range(len(links)):
    
    # create an empty dictionary to store img an title for each hemisphere
    hemisphere = {}
    
    # find img and click through the next page
    browser.find_by_css('a.product-item img')[i].click()
    
    #find sample image and extract
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # get the title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # append list with dictionary
    hemisphere_image_urls.append(hemisphere)
    
    # we need to navigate back to the start page
    browser.back()
        
    


# In[19]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[39]:


# 5. Quit the browser
browser.quit()


# In[ ]:




