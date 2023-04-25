from django.http import HttpRequest, HttpResponse

class execution:
    def execute(self, command: str) -> None:
        eval(command)                  # Sink

def get_command(request) -> str:       # Missing request type
    command = request.GET["command"]   # Source
    return command

def run(request: HttpRequest):
    command = get_command(request)     # Calling source
    E = execution()
    E.execute(command)                 # Passing source to sink