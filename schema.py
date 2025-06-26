from pydantic import  BaseModel , EmailStr

class DBStudent(BaseModel):
    name : str 
    address : str
    phone_num : int
    email : EmailStr
    batch : int
    