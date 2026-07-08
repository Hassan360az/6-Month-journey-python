# class UserOut(BaseModel):

# Yeh alag class kyun banayi? Yeh hamara Output Filter Sancha hai. Iske andar humne password ki field rakhi hi nahi hai.

# @app.post("/register", response_model=UserOut)

# response_model=UserOut: Yeh decorator ke andar sab se zaroori syntax hai. Hum FastAPI ko hukam de rahe hain ke "Is function se jo bhi response baher nikle, usay UserOut ke sanchay se guzaar kar filter karna!"

# Notice Placement: Yeh function ke argument mein nahi, balki decorator @app.post ke brackets ke andar likha jata hai.

# return user (Function ke andar):

# Andar toh password maujood tha! Function toh user return kar raha hai jisme password maujood tha. Lekin kyunke response_model=UserOut laga hua hai, FastAPI return hone wale data ko UserOut ke andar daal kar password ko gayab kar de gi.