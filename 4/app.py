from aiohttp import web

TASKS = [
    {
        'name': 'This is first',
        'finished': True
    },
    {
        'name': 'This is second',
        'finished': False
    }
]


def get_all_todos(request):
    return web.json_response([
        {'id': idx, **todo} for idx, todo in enumerate(TASKS)
    ])


def get_one_todo(request):
    id = int(request.match_info['id'])
    if id >= len(TASKS):
        return web.json_response({'error': 'Todo not found'}, status=404)
    return web.json_response({'id': id, **TASKS[id]})


def remove_todo(request):
    id = int(request.match_info['id'])
    if id >= len(TASKS):
        return web.json_response({'error': 'Todo not found'})
    del TASKS[id]
    return web.Response(status=204)


def setup_routes(app):
    app.router.add_get('/todos/', get_all_todos, name='all_todos')
    app.router.add_get('/todos/{id:\d+}', get_one_todo, name='one_todo')
    app.router.add_delete('/todos/{id:\d+}', remove_todo, name='remove_todo')


def app_factory(args=()):
    app = web.Application()
    setup_routes(app)
    return app
