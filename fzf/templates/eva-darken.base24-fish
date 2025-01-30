# Scheme name: Eva Darken
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
" --color=bg:#193145,fg:#a6a6a6,hl:#ff9966"\
" --color=bg+:#43596c,fg+:#,hl+:#"\
" --color=info:#a277e3,border:#a277e3,prompt:#66ff66"\
" --color=pointer:#16d2ce,marker:#,spinner:#,header:#df676a"
