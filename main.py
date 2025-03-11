from fastapi import FastAPI  # ya fastapi ki class hai jis ma sara api ka method hai
import random

# create fastapi instence and variable name app is recommended
app= FastAPI()

# we will build two simple get endpoints
# side_hustles     ya hama btay gi ka kon konsa kam ham kar sakta hai 
# money_quotes  


side_hustles = [
    "Freelance Web Development",
    "Graphic Design Services",
    "Content Writing & Blogging",
    "Social Media Management",
    "Online Tutoring & Coaching"
]



money_qotes = [
    "Money often costs too much. – Ralph Waldo Emerson",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "The more you learn, the more you earn. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn"
]

# this is a route handler
@app.get("/side_husteles")
async def get_side_hustles(api_key: str):
    """Returns a random side hustle idea"""
    if api_key != "123456789":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)} # object hi return karway ga 


@app.get("/money_quotes")
def get_money_quotes(api_key: str):
    """Returns a random money quotes """
    if api_key != "123456789":
        return {"error": "Invalid API key"}
    return{"money_quote" : random.choice(money_qotes)}

