# Mandelbrot Set Generator in Rust

Mind the resulting image is rendered in a Rust-alike debug trait `impl<'a> fmt::Debug for DebugImage<'a>`

The image is self is represented as a `Vec<Vec<u8>>` of chosen size.

Depending on the maxiter you are rendering with you might have to adapt some code snippets.

## Usage

``` ascii
cargo r
   Compiling rust_mandelbrot v0.1.0 (~/private/github/Fractals/Mandelbrot/Rust)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.39s
     Running `target/debug/rust_mandelbrot`
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
