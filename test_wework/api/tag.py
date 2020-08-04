from test_wework.api.wework import WeWork


class Tag(WeWork):
    def __init__(self):
        # 首先获取token
        secret='oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
        # 获取token，实际上是替换tag.yaml中access_token
        self.params['access_token']=self.get_token(secret)
        # 加载yaml文件
        self.tag_data=self.yaml_load('../api/tag.yaml')

    def get(self):
        self.send_api(self.tag_data['get'])


    # def add(self):
    #     self.send_api(self.tag_data['add'])

    def add_tag(self,tagname=[],tagid=[]):
        self.params['tagname'] =tagname
        self.params['tagid']=tagid
        self.send_api(self.tag_data['add'])

    def delete(self,tagid=[]):
        self.params['tagid']=tagid
        self.send_api(self.tag_data['delete'])


    def update_tag(self,tagid=[],tagname=[]):
        self.params['tagid']=tagid
        self.params['tagname'] =tagname
        self.send_api(self.tag_data['update'])

