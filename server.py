import uvicorn
from dotenv import load_dotenv
import os

# dev
load_dotenv(".env.dev")

# production
# load_dotenv(".env.production")

if __name__ == "__main__":
    env = os.environ
    uvicorn.run("src:app", host=env.get("HOST"), port=int(env.get("PORT")), reload=True)
