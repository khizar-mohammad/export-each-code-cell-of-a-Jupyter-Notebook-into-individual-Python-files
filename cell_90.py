#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os

# Mount Google Drive (if not already mounted)
from google.colab import drive
drive.mount('/content/drive')

# Get the notebook's filename
notebook_filename = 'Randomcodes.ipynb' # Replace with your notebook's name

# Find the notebook's full path
notebook_path = '' # Initialize to empty string

for root, dirs, files in os.walk('/content/drive/MyDrive/Colab Notebooks'): #Change '/content/drive/MyDrive/Colab Notebooks' to your google colab default directory if different
  for name in files:
    if name == notebook_filename:
      notebook_path = os.path.join(root, name)
      break
  if notebook_path:
    break

if notebook_path:
  # Get the notebook's directory
  notebook_directory = os.path.dirname(notebook_path)

  # Print the directory
  print("Current Google Colab notebook's directory:", notebook_directory)
else:
  print("Notebook not found in the specified directory")

