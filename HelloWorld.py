from bottle import route, run, request

@route('/')
def hello():
    return '''
        <img src="https://cdn.meme.am/instances/500x/59171276.jpg">
        '''


@route('/search')
def search():
    return '''
        <html>
        <head>
        <style>
        input[type=text] {
        width: 130px;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
        background-color: white;
        background-image: url('searchicon.png');
        background-position: 10px 10px;
        background-repeat: no-repeat;
        padding: 12px 20px 12px 40px;
        -webkit-transition: width 0.4s ease-in-out;
        transition: width 0.4s ease-in-out;
        }
        
        input[type=text]:focus {
        width: 30%;
        }
        </style>
        </head>
        <body>
        
        <p>Ello Search:</p>
        <form action ="/search" method= "post">
        Type Here: <input name="user_input" type="text"/>
        <input value = "Click Here" type="submit" />
        </form>
        
        </body>
        </html>
        '''

@route('/search', method='POST')
def do_search():
    input = request.forms.get("user_input")
    return "Output "+ "'%s'"  %(input)

run( host = 'localhost', port =8080, debug = True)
