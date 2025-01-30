;;; doom-base16-theme.el -*- no-byte-compile: t; -*-
;; Based on the doom one theme (https://github.com/hlissner/emacs-doom-themes)
;; released under the MIT License, copyright (c) 2016-2020 Henrik Lissner.

;;; Authors:
;; Scheme: kjakapat (https://github.com/kjakapat)
;; Template: Marcel Arpogaus

;;; License
;; The MIT License (MIT)

;; Copyright (c) 2021 Marcel Arpogaus

;; Permission is hereby granted, free of charge, to any person obtaining
;; a copy of this software and associated documentation files (the
;; "Software"), to deal in the Software without restriction, including
;; without limitation the rights to use, copy, modify, merge, publish,
;; distribute, sublicense, and/or sell copies of the Software, and to
;; permit persons to whom the Software is furnished to do so, subject to
;; the following conditions:

;; The above copyright notice and this permission notice shall be
;; included in all copies or substantial portions of the Software.

;; THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
;; EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
;; MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
;; IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
;; CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
;; TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
;; SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

(require 'doom-themes)
(require 'kurecolor)
;;
(defgroup doom-base16-theme nil
  "Options for doom-themes"
  :group 'doom-themes)

(defcustom doom-base16-brighter-modeline nil
  "If non-nil, more vivid colors will be used to style the mode-line."
  :group 'doom-base16-theme
  :type 'boolean)

(defcustom doom-base16-brighter-comments nil
  "If non-nil, comments will be highlighted in more vivid colors."
  :group 'doom-base16-theme
  :type 'boolean)

(defcustom doom-base16-comment-bg doom-base16-brighter-comments
  "If non-nil, comments will have a subtle, darker background. Enhancing their
legibility."
  :group 'doom-base16-theme
  :type 'boolean)

(defcustom doom-base16-padded-modeline doom-themes-padded-modeline
  "If non-nil, adds a 4px padding to the mode-line. Can be an integer to
determine the exact padding."
  :group 'doom-base16-theme
  :type '(choice integer boolean))

(if (< (kurecolor-hex-get-brightness "#2a3b4d") 0.5)
    (def-doom-theme doom-base16
      "A dark theme inspired by Atom One Dark"
      ;; name        default   256       16
      ((bg         '("#2a3b4d" nil       nil            ))
       (bg-alt     `(,(doom-darken (car bg) 0.3) nil       nil            ))
       (base0      `(,(doom-darken (car bg-alt) 0.3) "black"   "black"        ))
       (base1      `(,(doom-darken (car bg-alt) 0.2) "#1e1e1e" "brightblack"  ))
       (base2      `(,(doom-darken (car bg-alt) 0.1) "#2e2e2e" "brightblack"  ))
       (base3      '("#3d566f" "#262626" "brightblack"  ))
       (base4      '("#4b6988" "#3f3f3f" "brightblack"  ))
       (base5      '("#55799c" "#525252" "brightblack"  ))
       (base6      '("#7e90a3" "#6b6b6b" "brightblack"  ))
       (base7      '("#9fa2a6" "#979797" "brightblack"  ))
       (base8      '("#ffffff" "#dfdfdf" "white"        ))
       (fg         '("#d6d7d9" "#bfbfbf" "brightwhite"  ))
       (fg-alt     '("#55799c" "#2d2d2d" "white"        ))

       (grey       base4)
       (red        '("#c4676c" "#c4676c" "red"          ))
       (orange     '("#ff9966" "#dd8844" "brightred"    ))
       (green      '("#5de561" "#5de561" "green"        ))
       (teal       `(,(doom-lighten (car green) 0.2) "#44b9b1" "brightgreen"  ))
       (yellow     '("#bb64a9" "#bb64a9" "yellow"       ))
       (blue       '("#1ae1dc" "#1ae1dc" "brightblue"   ))
       (dark-blue  `(,(doom-lighten (car blue) 0.51) "#a0bcf8" "blue"         ))
       (magenta    '("#9c6cd3" "#9c6cd3" "magenta"      ))
       (violet     `(,(doom-lighten (car magenta) 0.2) "#b751b6" "brightmagenta"))
       (cyan       '("#4b8f77" "#4b8f77" "brightcyan"   ))
       (dark-cyan  `(,(doom-lighten (car cyan) 0.2) "#005478" "cyan"         ))

       ;; face categories -- required for all themes
       (highlight      blue)
       (vertical-bar   (doom-darken base1 0.1))
       (selection      dark-blue)
       (builtin        magenta)
       (comments       (if doom-base16-brighter-comments dark-cyan base5))
       (doc-comments   (doom-lighten (if doom-base16-brighter-comments dark-cyan base5) 0.25))
       (constants      violet)
       (functions      magenta)
       (keywords       blue)
       (methods        cyan)
       (operators      blue)
       (type           yellow)
       (strings        green)
       (variables      (doom-lighten magenta 0.4))
       (numbers        orange)
       (region         `(,(doom-lighten (car bg-alt) 0.15) ,@(doom-lighten (cdr base1) 0.35)))
       (error          red)
       (warning        yellow)
       (success        green)
       (vc-modified    orange)
       (vc-added       green)
       (vc-deleted     red)

       ;; custom categories
       (hidden     `(,(car bg) "black" "black"))
       (-modeline-bright doom-base16-brighter-modeline)
       (-modeline-pad
        (when doom-base16-padded-modeline
          (if (integerp doom-base16-padded-modeline) doom-base16-padded-modeline 4)))

       (modeline-fg     fg)
       (modeline-fg-alt base5)

       (modeline-bg
        (if -modeline-bright
            (doom-darken blue 0.475)
          `(,(doom-darken (car bg-alt) 0.15) ,@(cdr base0))))
       (modeline-bg-l
        (if -modeline-bright
            (doom-darken blue 0.45)
          `(,(doom-darken (car bg-alt) 0.1) ,@(cdr base0))))
       (modeline-bg-inactive   `(,(doom-darken (car bg-alt) 0.1) ,@(cdr bg-alt)))
       (modeline-bg-inactive-l `(,(car bg-alt) ,@(cdr base1))))


      ;; --- extra faces ------------------------
      ((elscreen-tab-other-screen-face :background "#353a42" :foreground "#1e2022")

       (evil-goggles-default-face :inherit 'region :background (doom-blend region bg 0.5))

       ((line-number &override) :foreground base4)
       ((line-number-current-line &override) :foreground fg)

       (font-lock-comment-face
        :foreground comments
        :background (if doom-base16-comment-bg (doom-lighten bg 0.05)))
       (font-lock-doc-face
        :inherit 'font-lock-comment-face
        :foreground doc-comments)

       (mode-line
        :background modeline-bg :foreground modeline-fg
        :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg)))
       (mode-line-inactive
        :background modeline-bg-inactive :foreground modeline-fg-alt
        :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-inactive)))
       (mode-line-emphasis
        :foreground (if -modeline-bright base8 highlight))

       (solaire-mode-line-face
        :inherit 'mode-line
        :background modeline-bg-l
        :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-l)))
       (solaire-mode-line-inactive-face
        :inherit 'mode-line-inactive
        :background modeline-bg-inactive-l
        :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-inactive-l)))

       ;; Doom modeline
       (doom-modeline-bar :background (if -modeline-bright modeline-bg highlight))
       (doom-modeline-buffer-file :inherit 'mode-line-buffer-id :weight 'bold)
       (doom-modeline-buffer-path :inherit 'mode-line-emphasis :weight 'bold)
       (doom-modeline-buffer-project-root :foreground green :weight 'bold)

       ;; ivy-mode
       (ivy-current-match :background dark-blue :distant-foreground base0 :weight 'normal)

       ;; --- major-mode faces -------------------
       ;; css-mode / scss-mode
       (css-proprietary-property :foreground orange)
       (css-property             :foreground green)
       (css-selector             :foreground blue)

       ;; LaTeX-mode
       (font-latex-math-face :foreground green)

       ;; markdown-mode
       (markdown-markup-face :foreground base5)
       (markdown-header-face :inherit 'bold :foreground red)
       ((markdown-code-face &override) :background (doom-lighten base3 0.05))

       ;; org-mode
       (org-hide :foreground hidden)
       (solaire-org-hide-face :foreground hidden))

      ;; --- extra variables ---------------------
      ()
      )
  (def-doom-theme doom-base16
    "A light theme inspired by Atom One"

    ;; name        default   256       16
    ((bg         '("#2a3b4d" nil       nil            ))
     (bg-alt     '("#3d566f" nil       nil            ))
     (base0      '("#3d566f" "#3d566f" "white"        ))
     (base1      '("#4b6988" "#4b6988" "brightblack"  ))
     (base2      `(,(doom-darken (car base1) 0.1) "#dfdfdf" "brightblack"  ))
     (base3      `(,(doom-darken (car base2) 0.1) "#c6c7c7" "brightblack"  ))
     (base4      '("#55799c" "#55799c" "brightblack"  ))
     (base5      '("#9fa2a6" "#424242" "brightblack"  ))
     (base6      '("#d6d7d9" "#2e2e2e" "brightblack"  ))
     (base7      `(,(doom-darken (car base6) 0.1) "#1e1e1e" "brightblack"  ))
     (base8      '("#ffffff" "black"   "black"        ))
     (fg         '("#9fa2a6" "#424242" "black"        ))
     (fg-alt     '("#55799c" "#c7c7c7" "brightblack"  ))

     (grey       base4)
     (red        '("#c4676c" "#c4676c" "red"          ))
     (orange     '("#ff9966" "#dd8844" "brightred"    ))
     (green      '("#5de561" "#5de561" "green"        ))
     (teal       `(,(doom-lighten (car green) 0.2) "#44b9b1" "brightgreen"  ))
     (yellow     '("#bb64a9" "#bb64a9" "yellow"       ))
     (blue       '("#1ae1dc" "#1ae1dc" "brightblue"   ))
     (dark-blue  `(,(doom-lighten (car blue) 0.51) "#a0bcf8" "blue"         ))
     (magenta    '("#9c6cd3" "#9c6cd3" "magenta"      ))
     (violet     `(,(doom-lighten (car magenta) 0.2) "#b751b6" "brightmagenta"))
     (cyan       '("#4b8f77" "#4b8f77" "brightcyan"   ))
     (dark-cyan  `(,(doom-lighten (car cyan) 0.2) "#005478" "cyan"         ))

     ;; face categories -- required for all themes
     (highlight      blue)
     (vertical-bar   (doom-darken base2 0.1))
     (selection      dark-blue)
     (builtin        magenta)
     (comments       (if doom-base16-brighter-comments cyan base4))
     (doc-comments   (doom-darken comments 0.15))
     (constants      violet)
     (functions      magenta)
     (keywords       red)
     (methods        cyan)
     (operators      blue)
     (type           yellow)
     (strings        green)
     (variables      (doom-darken magenta 0.36))
     (numbers        orange)
     (region         `(,(doom-darken (car bg-alt) 0.1) ,@(doom-darken (cdr base0) 0.3)))
     (error          red)
     (warning        yellow)
     (success        green)
     (vc-modified    orange)
     (vc-added       green)
     (vc-deleted     red)

     ;; custom categories
     (-modeline-bright doom-base16-brighter-modeline)
     (-modeline-pad
      (when doom-base16-padded-modeline
        (if (integerp doom-base16-padded-modeline) doom-base16-padded-modeline 4)))

     (modeline-fg     nil)
     (modeline-fg-alt (doom-blend violet base4 (if -modeline-bright 0.5 0.2)))

     (modeline-bg
      (if -modeline-bright
          (doom-darken base2 0.05)
        base1))
     (modeline-bg-l
      (if -modeline-bright
          (doom-darken base2 0.1)
        base2))
     (modeline-bg-inactive (doom-darken bg 0.1))
     (modeline-bg-inactive-l `(,(doom-darken (car bg-alt) 0.05) ,@(cdr base1))))

    ;; --- extra faces ------------------------
    ((centaur-tabs-unselected :background bg-alt :foreground base4)
     (font-lock-comment-face
      :foreground comments
      :background (if doom-base16-comment-bg base0))
     (font-lock-doc-face
      :inherit 'font-lock-comment-face
      :foreground doc-comments
      :slant 'italic)

     ((line-number &override) :foreground (doom-lighten base4 0.15))
     ((line-number-current-line &override) :foreground base8)

     (doom-modeline-bar :background (if -modeline-bright modeline-bg highlight))

     (mode-line
      :background modeline-bg :foreground modeline-fg
      :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg)))
     (mode-line-inactive
      :background modeline-bg-inactive :foreground modeline-fg-alt
      :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-inactive)))
     (mode-line-emphasis
      :foreground (if -modeline-bright base8 highlight))

     (solaire-mode-line-face
      :inherit 'mode-line
      :background modeline-bg-l
      :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-l)))
     (solaire-mode-line-inactive-face
      :inherit 'mode-line-inactive
      :background modeline-bg-inactive-l
      :box (if -modeline-pad `(:line-width ,-modeline-pad :color ,modeline-bg-inactive-l)))

     ;; magit
     (magit-blame-heading     :foreground orange :background bg-alt)
     (magit-diff-removed :foreground (doom-darken red 0.2) :background (doom-blend red bg 0.1))
     (magit-diff-removed-highlight :foreground red :background (doom-blend red bg 0.2) :bold bold)

     ;; --- major-mode faces -------------------
     ;; css-mode / scss-mode
     (css-proprietary-property :foreground orange)
     (css-property             :foreground green)
     (css-selector             :foreground blue)

     ;; markdown-mode
     (markdown-markup-face     :foreground base5)
     (markdown-header-face     :inherit 'bold :foreground red)
     ((markdown-code-face &override)       :background base1)
     (mmm-default-submode-face :background base1)

     ;; org-mode
     ((outline-1 &override) :foreground red)
     ((outline-2 &override) :foreground orange)
     ((org-block &override) :background base1)
     ((org-block-begin-line &override) :foreground fg :slant 'italic)
     (org-ellipsis :underline nil :background bg     :foreground red)
     ((org-quote &override) :background base1)

     ;; helm
     (helm-candidate-number :background blue :foreground bg)

     ;; selectrum
     (selectrum-current-candidate :background base1)

     ;; web-mode
     (web-mode-current-element-highlight-face :background dark-blue :foreground bg)

     ;; wgrep
     (wgrep-face :background base1)

     ;; ediff
     (ediff-current-diff-A        :foreground red   :background (doom-lighten red 0.8))
     (ediff-current-diff-B        :foreground green :background (doom-lighten green 0.8))
     (ediff-current-diff-C        :foreground blue  :background (doom-lighten blue 0.8))
     (ediff-current-diff-Ancestor :foreground teal  :background (doom-lighten teal 0.8))

     ;; tooltip
     (tooltip :background base1 :foreground fg)

     ;; posframe
     (ivy-posframe               :background base0)

     ;; lsp
     (lsp-ui-doc-background      :background base0)
     (lsp-face-highlight-read    :background (doom-blend red bg 0.3))
     (lsp-face-highlight-textual :inherit 'lsp-face-highlight-read)
     (lsp-face-highlight-write   :inherit 'lsp-face-highlight-read)
     )

    ;; --- extra variables ---------------------
    ()
    )
  )

;;; doom-base16-theme.el ends here
