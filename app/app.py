from fastapi import FastAPI
app = FastAPI()

todos = [
    {"id": '123', "activity": 'Go to the market', "status": False},
    {"id": '456', "activity": 'Go to the church', "status": True}
]


# minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


# get todos
@app.get('/todos', tags=['todos'])
async def get_todos() -> dict:
    return {"data": todos}


# post todo
@app.post("/todos", tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": todo, "message": "Todo added successfully"}


# update todo
@app.put('/todos/{id}', tags=['todos'])
async def update_todo(id: str, body: dict) -> dict:
    for todo in todos:
        if todo['id'] == id:
            status = todo['status']
            if 'status' in body:
                status = body['status']
            todo['activity'] = body['activity']
            todo['status'] = status
            return {
                "data": todo,
                "message": f"Todo with ID: {id} has been updated"
            }
    return {
        "data": False,
        "message": f"Todo with ID: {id} not found"
    }


# delete todo
@app.delete('/todos/{id}', tags=['todos'])
async def delete_todo(id: str) -> dict:
    for todo in todos:
        if todo['id'] == id:
            todos.remove(todo)
            return {
                "data": False,
                "message": f"Todo with ID: {id} has been deleted"
            }
    return {
        "data": False,
        "message": f"Todo with ID: {id} not found"
    }
