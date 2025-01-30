(progn
  ;; Base16 Eva Dim
  ;; Author: kjakapat (https://github.com/kjakapat)

  (stumpwm:set-fg-color "#7e90a3")
  (stumpwm:set-bg-color "#2a3b4d")
  (stumpwm:set-border-color "#55799c")
  (stumpwm:set-focus-color "#7e90a3")
  (stumpwm:set-unfocus-color "#2a3b4d")

  (setf stumpwm:*mode-line-foreground-color* "#9c6cd3"
	stumpwm:*mode-line-background-color* "#3d566f"
	stumpwm:*mode-line-border-color* "#55799c")

  ;; Set *colors*
  ;; Currently only the black and white colors are changed
  (setf (car stumpwm:*colors*) "#2a3b4d"
	(car (last stumpwm:*colors*)) "#55799c")
  ;; Toggle the mode line so that changes are applied
  (stumpwm:toggle-mode-line (stumpwm:current-screen) (stumpwm:current-head))
  (stumpwm:toggle-mode-line (stumpwm:current-screen) (stumpwm:current-head)))
       
