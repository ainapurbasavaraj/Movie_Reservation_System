
class Content:

    def __init__(self) -> None:
        self.content=None
        self.res_content=None
        self.request=None
        self.response=None
    
    def set_content(self,data):
        self.content=data
        #print(f'self.content --> {self.content}')

    def get_content(self):
        return self.content

    def set_res_content(self,data):
        self.res_content=data

    def get_res_content(self):
        return self.res_content

    def set_request(self,data):
        self.request=data

    def get_request(self):
        return self.request

    def set_response(self,data):
        self.response=data

    def get_response(self):
        return self.response



    