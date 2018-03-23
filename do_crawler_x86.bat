set softwave_path=%1%
if not exist softwave_path goto default_cd
cd %softwave_path%\crawler_scrapy
goto exec_scrapy
:default_cd
cd crawler_scrapy
:exec_scrapy
scrapy crawl test
:scrapy crawl quotes

