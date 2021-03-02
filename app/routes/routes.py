"""
App routes
"""

# from app import test

from urllib.parse import urljoin
import itty3

app = itty3.App()

################# Statics ##################################
app.static_url_path = '/static/'
app.static_root = 'app/public'
url = urljoin(
    app.static_url_path, "<any:asset_path>"
)
app.add_route("GET", url, app.render_static)
############################################################


@app.get('/')
def index(request):
    return app.render(request,
                      open('app/public/index.html', 'r').read()
    )


@app.get('/<any:offset>')
def index(request, offset):
    return app.render(request,
                      open('app/public/index.html', 'r').read()
    )
