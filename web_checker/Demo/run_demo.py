# 运行一个演示过程，对目标网页进行1层深度的爬取，

import run_crawler as cralwer_runner

target_url = "http://tester1.409dostastudio.work/"
source_vector = ["<>","<script>alter('XSS')</script>"]
cralwer_runner.run_crawler(target_url)

