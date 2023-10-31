from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
import httpx
import base64
from httpx import Headers



api_keys = [
    "my_api_key"
]

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
@app.get("/protected")
def protected_route(api_key: str = Security(get_api_key)):
    # Process the request for authenticated usersresponse = httpx.get(url, headers=custom_headers)
    return {"message": "Access granted!"}
    
def get_credentials():
    # Debes proporcionar un nombre de usuario y una contraseña para la autenticación básica.
    username = "iesmontsia"
    password = "61ff361db31270a88ccf36de2fe87947"

    # Codificar las credenciales en base64
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    return credentials
    

@app.get("/peticionotraapi")
async def hacer_peticion(api_key: str = Security(get_api_key)):
    # URL de la API externa a la que deseas hacer la solicitud
    url = "https://api.picanova.com/api/beta/countries"

    async with httpx.AsyncClient() as client:
        auth_header = Headers({"Authorization": f"Basic {get_credentials()}"})
        response = httpx.get(url, headers=auth_header)        

        if response.status_code == 200:
            # La solicitud se realizó con éxito, puedes manejar los datos de la respuesta aquí.
            data = response.json()
            # names = []
            # for item in data:
            #     names.append(item["data"])
            names = [item["name"] for item in data["data"]]
            return(names)
        
        else:
            # Maneja los errores si la solicitud no fue exitosa
            return {"error": "No se pudo realizar la solicitud a la API externa"}
        
@app.get("/test")
def read_test():
    return {"La API funciona"}