"""Gera index.html (versão pública, sem login) a partir da página do painel publicada no Claude."""
import sys, re
src = open(sys.argv[1], encoding="utf-8").read()
# remove um eventual esqueleto já presente
m = re.search(r"<body[^>]*>(.*)</body>", src, flags=re.S)
if m: src = m.group(1)
head = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="robots" content="noindex">'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
        '</head><body>')
open("index.html", "w", encoding="utf-8").write(head + src + "</body></html>")
print("index.html gerado", len(src), "bytes")
