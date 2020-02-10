'''
Just generates the index.html file.
I want to mention that I know some people will say 'using Python is overkill, just use sed or bash', but really, fuck scripting in bash.
'''

html_template = '''<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png">
    <link rel="manifest" href="/favicon/site.webmanifest">

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Popcorn Stand</title>
    <style type="text/css">
        body {
            margin: 40px auto;
            max-width: 650px;
            line-height: 1.6;
            font-size: 22px;
            color: #444;
            padding: 0 10px
        }
        h1,
        h2,
        h3 {
            line-height: 1.2
        }

        a {
            text-decoration: none;
        }


    </style>
    <script>
        
        window.addEventListener("load", function(){
            var a = document.getElementsByClassName('links'),
                length = a.length;

            for(var i=0; i< length; i++){
                a[i].href += 'http://' + a[i].id + ".${URL}";
            }

        });

    </script>
</head>

<body>
    <header>
        <h1>🍿The Popcorn Stand</h1>
        <aside>Welcome home!</aside>
    </header>
    <h2>Links</h2>
    <ul>
        <li><a class="links" target="_blank" id="plex">🎬Plex - Watch stuff</a></li>
        <li><a class="links" target="_blank" id="movies">🎥Radarr - Organise your movies</a></li>
        <li><a class="links" target="_blank" id="series">📺Sonarr - Organise your tv series</a></li>
        <li><a class="links" target="_blank" id="transmission">⛵Transmission - Download torrent files</a></li>
        <li><a class="links" target="_blank" id="jackett">🤖Jackett - API support for Torrent trackers</a></li>
        <li><a class="links" target="_blank" id="calibre">📚Calibre - Organise your books</a></li>
    </ul>
    
</body>

</html>
'''

env_vars = {}

with open(".env", "r") as fin:
    for line in fin:
        key, val = line.split("=")
        env_vars[key] = val.strip()

with open("web/index.html", "w") as fout:
    fout.write(html_template.replace('${URL}', env_vars['URL']))