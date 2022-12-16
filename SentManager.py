class SentManager:
    method = ['พัสดุลงทะเบียน', 'EMS']
    price= 0
    select_sent = 0
    
           
    def __init__(self,select_sent) -> None:
        self.select_sent = select_sent
        if select_sent == 1:
            self.price = 20
            
        if select_sent == 2:
            self.price = 50