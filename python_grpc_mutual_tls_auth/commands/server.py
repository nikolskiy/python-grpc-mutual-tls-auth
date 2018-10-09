from invoke import task
from server import serve


@task
def run(ctx):
    serve(ctx.config)

