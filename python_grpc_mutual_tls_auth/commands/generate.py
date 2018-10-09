from invoke import task


@task
def server(ctx):
    cmd = "openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout {key} -subj '/CN={cn}' -out {crt}".format(
        key=ctx.config['credentials']['server']['key'],
        crt=ctx.config['credentials']['server']['cert'],
        cn=ctx.config['credentials']['server']['host']
    )
    ctx.run(cmd)


@task
def client(ctx):
    cmd = "openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout {key} -subj '/CN=localhost' -out {crt}".format(
        key=ctx.config['credentials']['client']['key'],
        crt=ctx.config['credentials']['client']['cert'],
    )
    ctx.run(cmd)
