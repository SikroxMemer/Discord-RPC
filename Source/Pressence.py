from pypresence import Presence
import time

class RPC(Presence):
    def __init__(self, client_id) -> None:
        super().__init__(client_id)
    def Start(self):
        self.connect()
    def disconnect(self):
        self.close()
    def Update(
            self , 
            State:str ,
            Details:str , 
            Large_image:str , 
            Large_text:str  , 
            Small_image:str  , 
            Small_text:str ,
            Party:list ,
            Buttons:list[dict]
        ):
        if Party[0] == 0:
            Party[0] = 1
        self.update(
           state=State,
           details=Details,
           large_image=Large_image,
           large_text=Large_text,
           small_image=Small_image,
           small_text=Small_text,
           party_size=Party,
           buttons=Buttons
        )
    