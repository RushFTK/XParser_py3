import json
import re


class json_switcher(object):
    def __init__(self,source_object):
        self.target_object = source_object
    def object_to_json(self):
        return json.dumps(self.target_object.__dict__)

if __name__ == '__main__':
    t = re.search('php','index.php?page=add-to-your-blog.php')
    print(t)
