from django.http import HttpRequest, HttpResponse

class execution:
    def execute(self, command: str) -> None:
        eval(command)                  # Sink

def get_command(request: HttpRequest) -> str:
    command = request.GET["command"]   # Source
    return command

def run(request: HttpRequest):
    command = get_command(request)     # Calling Source
    E = execution()
    COMMAND = "Do_What_I_Say"
    E.execute(COMMAND)                 # Source not passed to sink