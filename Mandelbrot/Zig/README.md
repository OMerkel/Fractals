# Mandelbrot Generator in Zig

## Usage

### Any Zig version

To run `mandelbrot.zig` directly (should work on any Zig version)

``` ascii
zig run ./src/mandelbrot.zig
Generating Mandelbrot set image of size 100x30
X range: [-2.000000, 1.000000], Y range: [-1.000000, 1.000000]
@@@@@@@@@%%%%%%%%###########################oooooooooouuuu***=+==+:*uooooooo########%%%%%%%%%%%%%%%%
@@@@@@@@%%%%%%%##########################oooooooooooouuuu****=+:+=***uuoooooooo#######%%%%%%%%%%%%%%
@@@@@@@%%%%%###########################oooooooooooouuuu***=:++  .+==**uuuuoooooo#########%%%%%%%%%%%
@@@@@@%%%%##########################oooooooooooouuu******=+        +=***uuuuuooooo#########%%%%%%%%%
@@@@@%%%%########################ooooooooooouuu*********==+        +=********uuuooo#########%%%%%%%%
@@@@%%%########################oooooooouuuuu**++: +=== :+ ::.    .::+++::*****=+*uoo##########%%%%%%
@@@@%%######################oooooouuuuuuuu****=+    +                   :+++ ++:+*uoo##########%%%%%
@@@%%####################oooouuuuuuuuuuu******=+:                             .+**uuoo##########%%%%
@@%%################oooouu*uuuuuuuuu*******+.. :                             :+=***uuoo##########%%%
@@%###########oooooouu**=+*****************=+:                                 +===*uooo##########%%
@%######ooooooooouuuu***=:+++=== +===***==+:                                     :+*uoooo##########%
@####oooooooooouuuuuu****=++  : .  : +.++++                                     +=**uoooo###########
@##oooooooooouuuuuuu****+++:            ++.                                      :*uuoooo###########
@oooooooooouu*******+==++:               .                                       **uuooooo##########
@ouuuuu***********==+.                                                         =**uuuooooo##########
@                                                                           :+=***uuuooooo##########
@ouuuuu***********==+.                                                         =**uuuooooo##########
@oooooooooouu*******+==++:               .                                       **uuooooo##########
@##oooooooooouuuuuuu****+++:            ++.                                      :*uuoooo###########
@####oooooooooouuuuuu****=++  : .  : +.++++                                     +=**uoooo###########
@%######ooooooooouuuu***=:+++=== +===***==+:                                     :+*uoooo##########%
@@%###########oooooouu**=+*****************=+:                                 +===*uooo##########%%
@@%%################oooouu*uuuuuuuuu*******+.. :                             :+=***uuoo##########%%%
@@@%%####################oooouuuuuuuuuuu******=+:                             .+**uuoo##########%%%%
@@@@%%######################oooooouuuuuuuu****=+    +                   :+++ ++:+*uoo##########%%%%%
@@@@%%%########################oooooooouuuuu**++: +=== :+ ::.    .::+++::*****=+*uoo##########%%%%%%
@@@@@%%%%########################ooooooooooouuu*********==+        +=********uuuooo#########%%%%%%%%
@@@@@@%%%%##########################oooooooooooouuu******=+        +=***uuuuuooooo#########%%%%%%%%%
@@@@@@@%%%%%###########################oooooooooooouuuu***=:++  .+==**uuuuoooooo#########%%%%%%%%%%%
@@@@@@@@%%%%%%%##########################oooooooooooouuuu****=+:+=***uuoooooooo#######%%%%%%%%%%%%%%
```

### Using Zig 0.15.2

Invoking the Zig integrated build system configured in `build.zig` you can get an overview of available build steps.

``` bash
zig version
0.15.2

zig build --list-steps
  install (default)            Copy build artifacts to prefix path
  uninstall                    Remove build artifacts from prefix path
  run                          Run the Mandelbrot generator app
```

Let us run the Mandelbrot generator app

``` ascii
zig build run         
Generating Mandelbrot set image of size 100x30
X range: [-2.000000, 1.000000], Y range: [-1.000000, 1.000000]
@@@@@@@@@%%%%%%%%###########################oooooooooouuuu***=+==+:*uooooooo########%%%%%%%%%%%%%%%%
@@@@@@@@%%%%%%%##########################oooooooooooouuuu****=+:+=***uuoooooooo#######%%%%%%%%%%%%%%
@@@@@@@%%%%%###########################oooooooooooouuuu***=:++  .+==**uuuuoooooo#########%%%%%%%%%%%
@@@@@@%%%%##########################oooooooooooouuu******=+        +=***uuuuuooooo#########%%%%%%%%%
@@@@@%%%%########################ooooooooooouuu*********==+        +=********uuuooo#########%%%%%%%%
@@@@%%%########################oooooooouuuuu**++: +=== :+ ::.    .::+++::*****=+*uoo##########%%%%%%
@@@@%%######################oooooouuuuuuuu****=+    +                   :+++ ++:+*uoo##########%%%%%
@@@%%####################oooouuuuuuuuuuu******=+:                             .+**uuoo##########%%%%
@@%%################oooouu*uuuuuuuuu*******+.. :                             :+=***uuoo##########%%%
@@%###########oooooouu**=+*****************=+:                                 +===*uooo##########%%
@%######ooooooooouuuu***=:+++=== +===***==+:                                     :+*uoooo##########%
@####oooooooooouuuuuu****=++  : .  : +.++++                                     +=**uoooo###########
@##oooooooooouuuuuuu****+++:            ++.                                      :*uuoooo###########
@oooooooooouu*******+==++:               .                                       **uuooooo##########
@ouuuuu***********==+.                                                         =**uuuooooo##########
@                                                                           :+=***uuuooooo##########
@ouuuuu***********==+.                                                         =**uuuooooo##########
@oooooooooouu*******+==++:               .                                       **uuooooo##########
@##oooooooooouuuuuuu****+++:            ++.                                      :*uuoooo###########
@####oooooooooouuuuuu****=++  : .  : +.++++                                     +=**uoooo###########
@%######ooooooooouuuu***=:+++=== +===***==+:                                     :+*uoooo##########%
@@%###########oooooouu**=+*****************=+:                                 +===*uooo##########%%
@@%%################oooouu*uuuuuuuuu*******+.. :                             :+=***uuoo##########%%%
@@@%%####################oooouuuuuuuuuuu******=+:                             .+**uuoo##########%%%%
@@@@%%######################oooooouuuuuuuu****=+    +                   :+++ ++:+*uoo##########%%%%%
@@@@%%%########################oooooooouuuuu**++: +=== :+ ::.    .::+++::*****=+*uoo##########%%%%%%
@@@@@%%%%########################ooooooooooouuu*********==+        +=********uuuooo#########%%%%%%%%
@@@@@@%%%%##########################oooooooooooouuu******=+        +=***uuuuuooooo#########%%%%%%%%%
@@@@@@@%%%%%###########################oooooooooooouuuu***=:++  .+==**uuuuoooooo#########%%%%%%%%%%%
@@@@@@@@%%%%%%%##########################oooooooooooouuuu****=+:+=***uuoooooooo#######%%%%%%%%%%%%%%
```

Deeper build system help available by invocation of

``` bash
zig build --help
```
