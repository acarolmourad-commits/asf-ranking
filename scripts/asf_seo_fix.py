# -*- coding: utf-8 -*-
"""ASF SEO fix: substitui o H1 dinamico (placar de XP) por <div>, preservando id/JS. Idempotente."""
p = 'index.html'
s = open(p, encoding='utf-8').read()
old = '<h1 id="my" style="text-align:center;font-size:3rem;color:var(--roxo)">0</h1>'
new = '<div id="my" style="text-align:center;font-size:3rem;color:var(--roxo);font-weight:bold">0</div>'
if old in s:
    open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    print('H1 dinamico corrigido')
else:
    print('Nada a corrigir.')