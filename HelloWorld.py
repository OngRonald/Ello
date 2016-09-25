from bottle import route, run, request

@route('/')
def hello():
    return '''
        <img src="https://cdn.meme.am/instances/500x/59171276.jpg">
        '''


@route('/search')
def search():
    return '''
        <form action ="/search" method= "post">
        Type Here: <input name="user_input" type="text"/>
        <input value = "Click Here" type="submit" />
        </form>
        '''

@route('/search', method='POST')
def do_search():
    input = request.forms.get("user_input")
    return "Output "+ "'%s'"  %(input)

run( host = 'localhost', port =8080, debug = True)
