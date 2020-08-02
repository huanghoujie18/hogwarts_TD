from test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,secret):
        # 加载yaml文件
        wework_data=self.yaml_load('../api/wework.yaml')
        self.params['corpsecret']=secret
        # 请求token，并且取出返回，后面的请求都需要使用token
        return self.send_api(wework_data['get_token'])['access_token']  # 只有时json格式才可以这样取值





