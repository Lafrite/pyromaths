#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Pyromaths
# Un programme en Python qui permet de créer des fiches d'exercices types de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2006 -- Jérôme Ortais (jerome.ortais@pyromaths.org)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#

import outils
from . import developpements

##
##------------------- MÉTHODE PAR COMBINAISON -------------------


def choix_valeurs(m):  # crée les valeurs du systeme de la forme a1.x+b1.y=c1 ; a2.x+b2.y=c2 et renvoie ((a1, b1, c1), (a2, b2, c2), (x, y))
    while True:
        c = [outils.valeur_alea(-m, m) for i in range(6)]
        if c[0] * c[3] - c[1] * c[2] and abs(c[0]) - 1 and abs(c[1]) - 1 and \
            abs(c[2]) - 1 and abs(c[3]) - 1 and abs(c[1] * c[2] - c[0] *
                c[3]) - 1 and abs(c[0]) - abs(c[2]) and abs(c[1]) - abs(c[3]) and \
            c[4] and c[5]:
            break

            # supprime des cas particuliers

    return ((c[0], c[1], c[0] * c[4] + c[1] * c[5]), (c[2], c[3], c[2] *
            c[4] + c[3] * c[5]), (c[4], c[5]))


def signe(a):  # retourne '+' si a est positif, '-' si a est négatif, '' si a est nul
    if a > 0:
        return '+'
    elif a < 0:
        return '-'
    else:
        return ''


def tex_systeme(v, p=None):  # renvoie l'écriture au format tex d'un système d'équations. v[] est de la forme ((a0, b0, c0), (a1, b1, c1), (x,y))
    if p == None:
        tv = (developpements.tex_coef(v[0][0], 'x'), signe(v[0][1]),
              developpements.tex_coef(abs(v[0][1]), 'y'), v[0][2],
              developpements.tex_coef(v[1][0], 'x'), signe(v[1][1]),
              developpements.tex_coef(abs(v[1][1]), 'y'), v[1][2])
        return '''\\left\\lbrace
    \\begin{array}{rcrcl}
      %s & %s & %s & = & %s \\\\\n      %s & %s & %s & = & %s
    \\end{array}
  \\right.''' % \
            tv
    else:
        tv = (
            developpements.tex_coef(v[0][0], 'x'),
            signe(v[0][1]),
            developpements.tex_coef(abs(v[0][1]), 'y'),
            v[0][2],
            '\\qquad\\hbox{\\footnotesize$\\mathit{(\\times %s)}$}' %
                developpements.tex_coef(p[0], '', bpn=1),
            developpements.tex_coef(v[1][0], 'x'),
            signe(v[1][1]),
            developpements.tex_coef(abs(v[1][1]), 'y'),
            v[1][2],
            '\\qquad\\hbox{\\footnotesize$\\mathit{(\\times %s)}$}' %
                developpements.tex_coef(p[1], '', bpn=1),
            )
        return '''\\left\\lbrace
    \\begin{array}{rcrcll}
      %s & %s & %s & = & %s & %s \\\\\n      %s & %s & %s & = & %s & %s
    \\end{array}
  \\right.''' % \
            tv


def combinaison1(v, a0, a1):
    return ((v[0][0] * a0, v[0][1] * a0, v[0][2] * a0), (v[1][0] * a1, v[1][1] *
            a1, v[1][2] * a1))


def combinaison2(v):  # renvoie les coefficients pour la somme des deux lignes
    return (v[0][0] + v[1][0], v[0][1] + v[1][1], v[0][2] + v[1][2])


def tex_comb2(v, c):
    if c[0]:
        tv = (developpements.tex_coef(v[0][0], 'x'), '\\cancel{' +
              developpements.tex_coef(v[0][1], 'y', bplus=1) + '}',
              developpements.tex_coef(v[1][0], 'x', bplus=1),
              '\\cancel{' + developpements.tex_coef(v[1][1], 'y', bplus=
              1) + '}', developpements.tex_coef(v[0][2], ''),
              developpements.tex_coef(v[1][2], '', bplus=1))
    else:
        tv = ('\\cancel{' + developpements.tex_coef(v[0][0], 'x') + '}',
              developpements.tex_coef(v[0][1], 'y', bplus=1),
              '\\cancel{' + developpements.tex_coef(v[1][0], 'x', bplus=
              1) + '}', developpements.tex_coef(v[1][1], 'y', bplus=1),
              developpements.tex_coef(v[0][2], ''), developpements.tex_coef(v[1][2],
              '', bplus=1))
    return '%s%s%s%s=%s%s' % tv


def tex_comb3(v):
    if v[0]:
        tv = (developpements.tex_coef(v[0], 'x'), developpements.tex_coef(v[2],
              ''))
    else:
        tv = (developpements.tex_coef(v[1], 'y'), developpements.tex_coef(v[2],
              ''))
    return '%s=%s' % tv


def tex_comb4(v):
    if v[0]:
        tv = (developpements.tex_coef(1, 'x'), v[2], v[0],
              developpements.tex_coef(v[2] // v[0], ''))
    else:
        tv = (developpements.tex_coef(1, 'y'), v[2], v[1],
              developpements.tex_coef(v[2] // v[1], ''))
    return '%s=\\frac{%s}{%s}=%s' % tv


def tex_equation(v, c):
    tv = (developpements.tex_coef(v[0][0], 'x'), developpements.tex_coef(v[0][1],
          'y', bplus=1), v[0][2])
    t = '    $%s%s=%s\\quad\\text{et}\\quad ' % tv
    if c[0]:
        t = t + 'x=%s\\quad\\text{donc :}$\n' % v[2][0]
        tv = (developpements.tex_coef(v[0][0], ''), developpements.tex_coef(v[2][0],
              '', bpn=1), developpements.tex_coef(v[0][1], 'y', bplus=1),
              v[0][2])
        t = t + '    \\[%s\\times %s %s=%s\\]\n' % tv
    else:
        t = t + 'y=%s\\quad\\text{donc :}$\n' % v[2][1]
        tv = (developpements.tex_coef(v[0][0], 'x'), developpements.tex_coef(v[0][1],
              '', bplus=1), developpements.tex_coef(v[2][1], '', bpn=1),
              v[0][2])
        t = t + '    \\[%s %s\\times %s=%s\\]\n' % tv
    return t


def tex_eq2(v, c):
    if c[0]:
        tv = (developpements.tex_coef(v[0][1], 'y'), developpements.tex_coef(v[0][2],
              ''), developpements.tex_coef(-v[0][0] * v[2][0], '', bplus=
              1))
        t = '%s=%s%s' % tv
    else:
        tv = (developpements.tex_coef(v[0][0], 'x'), developpements.tex_coef(v[0][2],
              ''), developpements.tex_coef(-v[0][1] * v[2][1], '', bplus=
              1))
        t = '%s=%s%s' % tv
    return t


def tex_eq3(v, c):
    if c[0]:
        tv = (developpements.tex_coef(1, 'y'), developpements.tex_coef(v[0][2] -
              v[0][0] * v[2][0], ''), developpements.tex_coef(v[0][1],
              ''), developpements.tex_coef(v[2][1], ''))
        t = '%s=\\frac{%s}{%s}=%s' % tv
    else:
        tv = (developpements.tex_coef(1, 'x'), developpements.tex_coef(v[0][2] -
              v[0][1] * v[2][1], ''), developpements.tex_coef(v[0][0],
              ''), developpements.tex_coef(v[2][0], ''))
        t = '%s=\\frac{%s}{%s}=%s' % tv
    return t


def tex_verification(v):  # renvoie la vérification de lasolution du système d'équations.
    tv = (
        developpements.tex_coef(v[0][0], '\\times %s' % developpements.tex_coef(v[2][0],
                                '', bpn=1)),
        developpements.tex_coef(v[0][1], '\\times %s' % developpements.tex_coef(v[2][1],
                                '', bpn=1), bplus=1),
        developpements.tex_coef(v[0][0] * v[2][0], ''),
        developpements.tex_coef(v[0][1] * v[2][1], '', bplus=1),
        v[0][2],
        developpements.tex_coef(v[1][0], '\\times %s' % developpements.tex_coef(v[2][0],
                                '', bpn=1)),
        developpements.tex_coef(v[1][1], '\\times %s' % developpements.tex_coef(v[2][1],
                                '', bpn=1), bplus=1),
        developpements.tex_coef(v[1][0] * v[2][0], ''),
        developpements.tex_coef(v[1][1] * v[2][1], '', bplus=1),
        v[1][2],
        )
    return '''\\left\\lbrace
    \\begin{array}{l}
      %s %s=%s %s=%s \\\\\n      %s %s=%s %s=%s
    \\end{array}
  \\right.''' % \
        tv


def systemes(f0, f1, v):
    a = outils.ppcm(v[0][0], v[1][0])
    b = outils.ppcm(v[0][1], v[1][1])
    (a0, a1, b0, b1) = (a // v[0][0], -a // v[1][0], b // v[0][1], -b // v[1][1])
    if a0 < 0:
        (a0, a1) = (-a0, -a1)
    if b0 < 0:
        (b0, b1) = (-b0, -b1)
    if min(abs(a0), abs(a1)) > min(abs(b0), abs(b1)):
        (a0, a1) = (b0, b1)
    f0.write('  $%s$\n' % tex_systeme(v))
    f1.write('  $%s$\n' % tex_systeme(v, (a0, a1)))

    #outils.ecrit_tex(f1,tex_systeme(v, (a0, a1)), thenocalcul='',tabs=1)

    c1 = combinaison1(v, a0, a1)
    f1.write('''  \\vspace{2ex}
  \\begin{multicols}{2}\\noindent
''')
    outils.ecrit_tex(f1, tex_systeme(c1) +
                     '\\quad\\text{\\footnotesize On ajoute les deux lignes}',
                     thenocalcul='', tabs=2)
    c2 = combinaison2(c1)
    outils.ecrit_tex(f1, tex_comb2(c1, c2), thenocalcul='', tabs=2)
    outils.ecrit_tex(f1, tex_comb3(c2), thenocalcul='', tabs=2)
    outils.ecrit_tex(f1, tex_comb4(c2), thenocalcul='', tabs=2, cadre=1)
    f1.write('  \\columnbreak\\par\n')
    f1.write(tex_equation(v, c2))
    outils.ecrit_tex(f1, tex_eq2(v, c2), thenocalcul='', tabs=2)
    outils.ecrit_tex(f1, tex_eq3(v, c2), thenocalcul='', tabs=2, cadre=1)
    f1.write('  \\end{multicols}\n')
    f1.write("  \\underline{La solution de ce syst\xe8me d'\xe9quations est $(x;~y)=(%s;~%s)$.}\\par\n" %
             v[2])
    f1.write('  {V\xe9rification : $' + tex_verification(v) + '$}\n')


