from bottle import route, run

@route('/todo/')
def todo_list():
    return { "success" : False, "paths" : [], "error" : "list not implemented yet" }

@route('/todo/get/<name>', method='GET')
def todo_show( name="my todo" ):
    return { "success" : False, "path" : "/PTH/TO/XML/"+name+".xml", "error" : "show not implemented yet" }

@route('/todo/delete/<name>', method='DELETE' )
def todo_delete( name="my todo" ):
    return { "success" : False, "error" : "delete not implemented yet" }

@route('/todo/put/<name>', method='PUT')
def todo_save( name="my todo" ):
    return { "success" : False, "path" : "/PTH/TO/XML/"+name+".xml", "error" : "save not implemented yet" }

run(host='localhost', port=8080, debug=True)