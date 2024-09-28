# word = send(whatsapp, +201223048371, hi ahmed how are you)

class comminty:
    def __init__(self, statment):
        self.result = self.detct_comminty(statment)
        return self.result

    def detct_comminty(self,statment):
        comminty = statment.split(',')[0]
        if comminty == 'whatsapp':
           rcvphone = statment.split(',')[1]
           msg = statment.split(',')[2]
           return f'Sended to {rcvphone}'