from fastapi import FastAPI
from routes.user import user


app = FastAPI(
		title="My first Api",
		description="Esta es mi primera Api",
		version="0.0.1",
		openapi_tags=[{
			"name": "Users",
			"description": "user routes"
		}]
	)
app.include_router(user)




