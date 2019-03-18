import sys
from database_updater.Types import xssed_items
import datetime
from urllib.parse import urlparse

#将爬取到的xssed文字数据切分，整合为可以使用的
#输入 lines:爬取的一行数据
#输出 类型xssed_items:切分好的数据
def crawledtext_parser(line):
    __out = xssed_items()
    split_lines = line.split('|')
    __out.full_urls = split_lines[2]
    split_urls = urlparse(__out.full_urls)
    print(split_urls)
    __out.date = datetime.datetime.strptime(split_lines[1],"%d/%m/%Y")
    return __out
    pass

if __name__ == '__main__':
    demo_xssed_mirrors = ['78603|09/08/2012|http://www.brazzers.com/series/view/episodes/%22%20onmouseover%3dprompt%28%27XSS%27%29%20bad%3d%22/i|www.brazzers.com|FIXED|',
                          '81282|18/08/2014|http://webcenters.netscape.compuserve.com/weather/find.jsp?f="><script>alert(1)</script>|webcenters.netscape.compuserve.com|UNFIXED|',
                          '81331|06/10/2014|http://www.titivillus.it/periodico.php?id=15%3Cscript%3Ealert%28document.cookie%29%3C/script%3E|www.titivillus.it|UNFIXED|',
                          '80852|05/01/2014|http://store.samsung.com/uk/camera/smart-n2x"><script>alert(document.cookie)</script></nx1010-smart-|store.samsung.com|FIXED|',
                          '80717|15/11/2013|https://auth.dhs.gov/oam/hsinlogin/?authn_try_count=0&contextType=external&username=string&ssoCookie|auth.dhs.gov|FIXED|']
    for line in demo_xssed_mirrors:
        result = crawledtext_parser(line)
        print(result)