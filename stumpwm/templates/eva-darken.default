(progn
  ;; Base16 Eva Darken
  ;; Author: kjakapat (https://github.com/kjakapat)

  (stumpwm:set-fg-color "#7f8992")
  (stumpwm:set-bg-color "#193145")
  (stumpwm:set-border-color "#5e707f")
  (stumpwm:set-focus-color "#7f8992")
  (stumpwm:set-unfocus-color "#193145")

  (setf stumpwm:*mode-line-foreground-color* "#a277e3"
	stumpwm:*mode-line-background-color* "#2b4458"
	stumpwm:*mode-line-border-color* "#5e707f")

  ;; Set *colors*
  ;; Currently only the black and white colors are changed
  (setf (car stumpwm:*colors*) "#193145"
	(car (last stumpwm:*colors*)) "#5e707f")
  ;; Toggle the mode line so that changes are applied
  (stumpwm:toggle-mode-line (stumpwm:current-screen) (stumpwm:current-head))
  (stumpwm:toggle-mode-line (stumpwm:current-screen) (stumpwm:current-head)))
       
