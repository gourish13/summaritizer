"""
App routes
"""

# from app import test
from app.controllers.post_controller import (
    new_post,
    show_post,
    delete_post,
    update_post,
)

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

@app.post('/create')
def create(request):
    author  = request.POST['author']
    hours   = int(request.POST['hours'])
    mins    = int(request.POST['minutes'])
    email   = request.POST['email']
    content = request.POST['content']
    data = new_post(author, hours, mins, email, content)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.post('/read/<int:_id>/<uuid:_uuid')
def read(request, _id, _uuid):
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = show_post(_id, _uuid)
    )


@app.post('/update/<int:_id>/<uuid:_uuid')
def update(request, _id, _uuid):
    author  = request.POST['author']
    content = request.POST['content']
    key     = request.POST['key']
    data = update_post(_id, _uuid, author, content, key)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.post('/delete/<int:_id>/<uuid:_uuid')
def delete(request, _id, _uuid):
    key     = request.POST['key']
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = delete_post(_id, _uuid, key)
    )

    
@app.post('/delete-expired')
def delete_expired(request):
    key     = request.POST['key']


@app.get('/test')
def test(request):
    print(request.GET)
    send_email(
        'sadhu2gourish@gmail.com',
        'https://summaritizer.herokuapp.com',
        1,
        3,
        'djsnfusfnsjnc342'
    )
    return app.render_json(request, content_type = itty3.JSON, data = dict(status = 'ok'))


@app.get('/')
def index(request):
    return app.render(request,
                      open('app/public/index.html', 'r').read()
    )


@app.get('/<any:offset>')
def index_with_offset(request, offset):
    return app.render(request,
                      open('app/public/index.html', 'r').read()
    )
