class Content:
    id = 1
    def __init__(self,first_name:str,last_name:str,phone_number:str):
        self.id = Content.id
        Content.id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
