import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class = HTMLResponse)
def get_contact():
    # return { 'name': 'GaboStore' }
    return """
        <h1>Soy una página</h1>
        <p>Esto es un párrafo que desmuestra que es un html genuino</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()