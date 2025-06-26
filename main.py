from fastapi import FastAPI

from routes import session, user , auth

app = FastAPI()


@app.get("/")
def root():
    return "Server is running..."

@app.get("/auth/login")
def login():
    pass

app.include_router(user.router,prefix="/users")
app.include_router(session.router,prefix="/session")
app.include_router(auth.router,prefix="/auth")
app.include_router(session.router,prefix="/qr_code")

# for qr code 

@app.get("/scan")

@app.get("attendance/me")
@app.get("attendance/session/{id}")
@app.get("attendance/day/{date}")


