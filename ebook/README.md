title: Whole In One FRamework
author: Bouarfa Mahi
rights: Creative Commons Non-Commercial Share Alike 4.0
language: en-US ...

See the User’s Guide for more information about these fields.

Now run pandoc to make the ebook, using our title page and modified chapter files as sources:

pandoc -o ebook.epub title.txt
01-Conjecture/01-article1.md
A-code/A-code.md
--css=theme/epub/epub.css
--epub-cover-image cover.jpg
--toc