"""
FastAPI authentication server with multiple authentication methods like AWS, Google, Facebook, etc.

"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

# Get general settings from config.py
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event"""
    # tudo que ficar antes do comando yield é executado antes de iniciar o servidor
    # busca a conexão com o servidor de autenticação da MSAL (Microsoft Authentication Library)
    print("Starting up the server...")
    try :
      app.auth_client = "biblioteca mSAL"  # await get_msal_client()
    except Exception as e:
      print(f"Error connecting to MSAL: {e}")
      raise e

    app.settings = settings
    yield
    # everything after yield is executed after the server stops
    print("Shutting down the server...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.get("/")
async def root():
    """root access to the services"""
    return {"status": "ok"}

@app.get("/login")
async def login(req: Request):
  """
  Login endpoint
  """
  print(f"login requet received{ 4 }")
  [ print( (k, v) ) for k, v in req.headers.items() ]
  return {"status": "ok"}
