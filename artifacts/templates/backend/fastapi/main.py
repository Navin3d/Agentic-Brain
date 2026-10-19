from uvicorn import run

if __name__ == "__main__":
    run("src.app:app", reload=True, host="0.0.0.0", port=8000)
