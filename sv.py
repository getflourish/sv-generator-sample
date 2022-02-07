# This Python script replicates some features of Small Victories.
# It converts Markdown files to HTML files.

# We can create a HTML template for the page layout. In it, we can add 
# placeholder text (#content, #navigation). The script will replace these 
# text markers with the content of each page and a list of links.

# We need a folder with Markdown files, a destination folder where the HTML 
# files are saved. That destination folder should contain all assets including
# CSS, fonts, and the /links folder with images.

# To use this script, place it in the folder with your Markdown files.
# Create a /dist folder
# Move /links and assets into the /dist folder

# Install the markdown package:
# pip install markdown

# Open Terminal:
# cd /path/to/your/folder
# python sv.py

###############################################################################

# pathlib requires Python > 3.4
from pathlib import Path

# pip install markdown
import markdown

###############################################################################

# 1. Define variables
templatePath = "_template.html"
destinationFolder = "./dist/";

###############################################################################

# Function that reads all markdown files in the folder
# ["01_Coding.md", "02_Typo.md", ...]

def getFiles():
  files = []
  for file in Path('.').glob('*.md'):
      files.append(file)
  return files

# Function that constructs a HTML navigation as a list 
# <ul>
#   <li>
#     <a href="..."></a>
#   </li>
#   <li>
#     <a href="..."></a>
#   </li>
# </ul>

def getNavigation(files):
  html = "<ul>"
  for file in files:
    url = file.name.replace(".md", ".html")
    html += '<li><a href="' + url + '">' + file.name + '</a></li>'
  html += "</ul>"
  return html

# Function that reads the HTML template that is used for each page
def getTemplate(path):
  template = open(path, "r")
  return template.read()

# Function that used the Python Markdown parser to convert Markdown to HTML
# This function also replaces #content with the page content and #navigation with
# the generated navigation.
def convertMarkdownFileToHTML(file, template, navigation):
  # convert
  html = markdown.markdown(file.read_text())

  # replace placeholders
  withContent = template.replace("#content", html)
  withContentAndNavigation = withContent.replace("#navigation", navigation)

  return withContentAndNavigation

###############################################################################
  
# 2. Get Markdown files
files = getFiles()

# 3. Get the navigation with links to all pages
navigation = getNavigation(files)

# 4. Read the HTML Template which should include placeholders (#content, #navigation) in the <body>
template = getTemplate(templatePath)

# 5. Read each Markdown file, convert its contents to HTML and use the Template to create a website
for file in files:

  # Convert Markdown to HTML
  html = convertMarkdownFileToHTML(file, template, navigation)

  # Save each .html file to the destination folder
  outputFilename = destinationFolder + file.name.replace(".md", ".html")
  file = open(outputFilename, 'w')
  file.write(html)
  file.close()

