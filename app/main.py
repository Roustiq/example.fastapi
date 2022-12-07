# uvicorn app.main:app --reload
# the code above used to run the app
# video to carryone https://www.youtube.com/watch?v=0sOvCWFmrtA   Time:11:10:15

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote





# create model for the database:
# commented out due to alembic doing all the job. Dont need this anymore
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# addidng CORS
# when give specific site it will be restricted to this site. If you put * it will work on all sites.
# origins = ['https://www.google.com']
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello THE World!!!!!"}





