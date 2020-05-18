from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class Base16Style(Style):
    base00 = '#2a3b4d'
    base01 = '#3d566f'
    base02 = '#4b6988'
    base03 = '#55799c'
    base04 = '#7e90a3'
    base05 = '#9fa2a6'
    base06 = '#d6d7d9'
    base07 = '#ffffff'
    base08 = '#c4676c'
    base09 = '#ff9966'
    base0a = '#cfd05d'
    base0b = '#5de561'
    base0c = '#4b8f77'
    base0d = '#1ae1dc'
    base0e = '#9c6cd3'
    base0f = '#bb64a9'

    default_style = ''

    background_color = base00
    highlight_color = base02

    styles = {
        Text: base05,
        Error: base08,  # .err

        Comment: base03,  # .c
        Comment.Preproc: base0f,  # .cp
        Comment.PreprocFile: base0b,  # .cpf

        Keyword: base0e,  # .k
        Keyword.Type: base08,  # .kt

        Name.Attribute: base0d,  # .na
        Name.Builtin: base0d,  # .nb
        Name.Builtin.Pseudo: base08,  # .bp
        Name.Class: base0d,  # .nc
        Name.Constant: base09,  # .no
        Name.Decorator: base09,  # .nd
        Name.Function: base0d,  # .nf
        Name.Namespace: base0d,  # .nn
        Name.Tag: base0e,  # .nt
        Name.Variable: base0d,  # .nv
        Name.Variable.Instance: base08,  # .vi

        Number: base09,  # .m

        Operator: base0c,  # .o
        Operator.Word: base0e,  # .ow

        Literal: base0b,  # .l

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: base0c,  # .sr
        String.Symbol: base09,  # .ss
    }


from string import capwords  # noqa: E402
Base16Style.__name__ = 'Base16{}Style'.format(
    capwords('eva-dim', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
