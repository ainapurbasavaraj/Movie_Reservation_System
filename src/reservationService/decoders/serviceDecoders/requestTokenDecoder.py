
from logging import exception
from reservationService.decoders.decoder import Decoder

class RequesTokenDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)
        self.data=dict()

    def decode(self, request):
        #decode the header and fetch the bearer token
        auth=request.headers.get('Authorization')
        auth_list=auth.split()
        if "Bearer" != auth_list[0]:
            return False
        token=auth_list[1]
        #decode the payload and fetch the userid
        userid=request.get_json()
        self.data.update({'token':token})
        self.data.update({'userid':userid.get('userid',None)})
        service_content=self.get_content()
        service_content.set_request(request)
        service_content.set_content(self.data)


