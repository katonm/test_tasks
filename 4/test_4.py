from aiohttp import web

TODOS = [
    {
        'name': 'Start this tutorial',
        'finished': True
    },
    {
        'name': 'Finish this tutorial',
        'finished': False
    }
]

def get_all_todos(request):
    return web.json_response([
        {'id': idx, **todo} for idx, todo in enumerate(TODOS)
    ])


def get_one_todo(request):
    id = int(request.match_info['id'])

    if id >= len(TODOS):
        return web.json_response({'error': 'Todo not found'}, status=404)

    return web.json_response({'id': id, **TODOS[id]})

def create_app(loop):
    app = web.Application(loop=loop)
    app.router.add_get('/todos/{id}', get_one_todo, name='one_todo')
    return app

async def test_get_one_todo(test_client):
    client = await test_client(create_app)
    resp = await client.get('/todos/1')
    assert resp.status == 200
    data = await resp.json()
    name = data.get('name')
    assert 'Finish this tutorial' == name