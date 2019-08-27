# -*- coding: utf-8 -*-

from googletrans import Translator
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

css = """<style type="text/css">

.entry {
  font-family: Tahoma, Batang, GulimChe, sans-serif;
  font-size: 16px;
  font-weight: bold;
  color: #dc143c;
  margin: 7px 0;
  line-height: 27px;
}
.text {
  font-family: Verdana, Geneva, Batang, GulimChe, Tahoma, sans-serif;
  font-size: 16px;
  color: #232323;
  margin: 7px 0;
  line-height: 27px;
}
.pronunciation{
  font-family: Verdana, Geneva, Batang, GulimChe, Tahoma, sans-serif;
  font-size: 15px;
  color: #c6c6c6;
  line-height: 27px;
}
.pronunciation::before {
  content: "/ ";
}
.pronunciation::after {
  content: " /";
}

</style>"""

word = input("\r\n")
print(css, '<div class="entry">' + word + '</div>')
translator = Translator()
a = translator.translate(word, src='en', dest='ku')
if a.pronunciation == None:
    pass
else:
    print(css, '<div class="pronunciation">' + a.pronunciation + '</div>')

print(css, '<div class="text">' + a.text + '</div>')

##print(a.extra_data)

print(css, "<br>")

