import uvicorn
import os
import Chatmodel_server
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Chatmodel_server.app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting app on port {port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port)
