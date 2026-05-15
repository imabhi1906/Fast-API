from fastapi import FastAPI

# fake DB
user_db = []

app = FastAPI()

@app.get('/')
async def home():
    return "Hello World !!"


@app.get('/users')
async def get_users():
    return user_db


@app.post("/users")
async def create_user(user: dict):

    new_user = {
        "id": len(user_db) + 1,
        "name": user["name"]
    }

    user_db.append(new_user)

    return {
        "message": "User created",
        "user": new_user
    }


@app.get("/users/{id}")
async def get_user(id: int):

    for user in user_db:
        if user["id"] == id:
            return user

    return {"message": "User not found"}

@app.get("/search")
async def search(q: str):

    results = []

    for user in user_db:

        if q.lower() in user["name"].lower():
            results.append(user)

    return results
    
