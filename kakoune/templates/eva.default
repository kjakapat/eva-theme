## base16-kakoune (https://github.com/leira/base16-kakoune)
## by Leira Hua
## Eva scheme by kjakapat (https://github.com/kjakapat)

evaluate-commands %sh{
    base00='rgb:2a3b4d'
    base01='rgb:3d566f'
    base02='rgb:4b6988'
    base03='rgb:55799c'
    base04='rgb:7e90a3'
    base05='rgb:9fa2a6'
    base06='rgb:d6d7d9'
    base07='rgb:ffffff'
    base08='rgb:c4676c'
    base09='rgb:ff9966'
    base0A='rgb:ffff66'
    base0B='rgb:66ff66'
    base0C='rgb:4b8f77'
    base0D='rgb:15f4ee'
    base0E='rgb:9c6cd3'
    base0F='rgb:bb64a9'

    ## code
    echo "
        face global value ${base09}
        face global type ${base0A}+b
        face global identifier ${base08}
        face global string ${base0B}
        face global keyword ${base0E}+b
        face global operator ${base05}
        face global attribute ${base0C}
        face global comment ${base03}
        face global meta ${base0D}
        face global builtin ${base0D}+b
    "

    ## markup
    echo "
        face global title ${base0D}+b
        face global header ${base0D}+b
        face global bold ${base0A}+b
        face global italic ${base0E}
        face global mono ${base0B}
        face global block ${base0C}
        face global link ${base09}
        face global bullet ${base08}
        face global list ${base08}
    "

    ## builtin
    echo "
        face global Default ${base05},${base00}
        face global PrimarySelection ${base06},${base0D}
        face global SecondarySelection ${base06},${base0F}
        face global PrimaryCursor ${base00},${base05}
        face global SecondaryCursor ${base06},${base0C}
        face global LineNumbers ${base02},${base00}
        face global LineNumberCursor ${base0A},${base00}
        face global MenuForeground ${base00},${base0D}
        face global MenuBackground ${base00},${base0C}
        face global MenuInfo ${base02}
        face global Information ${base00},${base0A}
        face global Error ${base00},${base08}
        face global StatusLine ${base04},${base01}
        face global StatusLineMode ${base0B}
        face global StatusLineInfo ${base0D}
        face global StatusLineValue ${base0C}
        face global StatusCursor ${base00},${base05}
        face global Prompt ${base0D},${base01}
        face global MatchingChar ${base06},${base02}+b
        face global BufferPadding ${base03},${base00}
    "
}
