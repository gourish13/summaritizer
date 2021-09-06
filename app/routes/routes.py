"""
App routes
"""
from app.utils.email import send_email
from app.controllers.post_controller import (
    new_post,
    show_post,
    delete_post,
    update_post,
)

import itty3

app = itty3.App()

@app.post('/create')
def create(request):
    author  = request.POST['author']
    hours   = int(request.POST['hours'])
    mins    = int(request.POST['minutes'])
    email   = request.POST['email']
    content = request.POST['content']
    data    = new_post(author, hours, mins, email, content)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.get('/read/<str:_id>')
def read(request, _id):
    _uuid   = _id[ _id.find('-') + 1 : ]
    _id     = int(_id[ : _id.find('-') ])
    data    = show_post(_id, _uuid)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.post('/update/<str:_id>')
def update(request, _id):
    _uuid   = _id[ _id.find('-') + 1 : ]
    _id     = int(_id[ : _id.find('-') ])
    author  = request.POST['author']
    content = request.POST['content']
    key     = request.POST['key']
    data    = update_post(_id, _uuid, author, content, key)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.post('/delete/<str:_id>')
def delete(request, _id):
    _uuid   = _id[ _id.find('-') + 1 : ]
    _id     = int(_id[ : _id.find('-') ])
    key     = request.POST['key']
    data    = delete_post(_id, _uuid, key)
    return app.render_json(
        request,
        content_type = itty3.JSON,
        data = data
    )


@app.get('/<str:path>')
@app.get('/')
def index_or_catchall(request, path = None):
    return app.render_json(request, 
                               content_type = itty3.JSON, 
                               data = { 
                                'response': { 
                                    'message': 'Welcome to summaritizer api' ,
                                    'endpoints': {
                                            '/api/v1/create': 'Create Post',
                                            '/api/v1/read/<id>': 'Fetch Post by Id',
                                            '/api/v1/update/<id>': 'Update Post by Id',
                                            '/api/v1/delete/<id>': 'Delete Post by Id'
                                     }
                                }
                               }
                          )
