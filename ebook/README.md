OK! Now we’re almost ready to make an ebook. We have the chapters, each in its own file, but we still need a title. Create a file, title.txt, with a pandoc YAML metadata block:


---
title: Whole In One Framework \
author: Bouarfa Mahi \
rights:  Creative Commons Non-Commercial Share Alike 4.0 \
language: en-US
...

See the User’s Guide for more information about these fields.

Now run pandoc to make the ebook, using our title page and modified chapter files as sources:

pandoc -o ebook.epub title.txt \
  01-article/01-article1.md \
  02-article/01-article2.md \
  03-article/01-article3.md \
  04-article/01-article4.md \
  05-article/01-article5.md \
  06-article/01-article6.md \
  07-article/01-article7.md \
  08-article/01-article8.md \
  09-article/01-article9.md \
  10-article/01-article10.md \
  11-article/01-article11.md \
  12-article/01-article12.md \
  13-article/01-article13.md \
  14-article/01-article14.md \
  15-article/01-article15.md \
  16-article/01-article16.md \
  17-article/01-article17.md \
  18-article/01-article18.md \
  19-article/01-article19.md \
  A-code/A-code.md \
  --css=theme/epub/epub.css \
  --epub-cover-image cover.png \
  --toc

 
