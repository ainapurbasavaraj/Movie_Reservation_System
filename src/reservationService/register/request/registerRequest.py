class RegisterRequest:
    def __init__(self) -> None:
        self.request=dict()

    def set_request(self,req):
        if isinstance(req,dict):
            self.request=req
        else:
            raise TypeError

    def get_request(self):
        return self.request