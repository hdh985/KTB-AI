import uvicorn
import os
import Chatmodel_server

app = Chatmodel_server.app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
