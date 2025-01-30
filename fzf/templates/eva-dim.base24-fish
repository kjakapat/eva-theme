# Scheme name: Eva Dim
# Scheme system: 
# Scheme author: kjakapat (https://github.com/kjakapat)
# Template author: Tinted Theming (https://github.com/tinted-theming)

set -l FZF_NON_COLOR_OPTS

for arg in (echo $FZF_DEFAULT_OPTS | tr " " "\n")
    if not string match -q -- "--color*" $arg
        set -a FZF_NON_COLOR_OPTS $arg
    end
end

set -Ux FZF_DEFAULT_OPTS "$FZF_NON_COLOR_OPTS"\
" --color=bg:#2a3b4d,fg:#9fa2a6,hl:#ff9966"\
" --color=bg+:#4b6988,fg+:#,hl+:#"\
" --color=info:#9c6cd3,border:#9c6cd3,prompt:#5de561"\
" --color=pointer:#1ae1dc,marker:#,spinner:#,header:#c4676c"
