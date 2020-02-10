env_vars = {}

with open(".env", "r") as fin:
    for line in fin:
        key, val = line.split("=")
        env_vars[key] = val.strip()

with open("web/index.html.example", "r") as fin:
    with open("web/index.html", "w") as fout:
        for line in fin:
            fout.write(line.replace('${URL}', env_vars['URL']))
