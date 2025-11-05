/*
 * A simple Rust program to generate and display a Mandelbrot set image in the console.
 * The image is represented as a 2D array of pixel values, where each pixel's value
 * indicates the number of iterations before escape.
 * The program includes functions to generate the Mandelbrot set and display it.
 * 🐻
 * 
 * Author: Oliver Merkel
 * Date: 2025-11-01
 * License: MIT
 * 
 * Usage:
 * - Compile and run the program to see the Mandelbrot set displayed in the console.
 */

fn generate_mandelbrot_set(
    width: usize, height: usize,
    x_range_min: f64, x_range_max: f64,
    y_range_min: f64, y_range_max: f64,
    max_iter: u8
) -> Vec<Vec<u8>> {
    /*
     * Generate a Mandelbrot set image.
     * Each pixel's value represents the number of iterations before escape.
     * The image is represented as a 2D array of pixel values.
     * 
     * Parameters:
     * - width: Width of the image.
     * - height: Height of the image.
     * - x_range_min: Minimum x-coordinate in the complex plane.
     * - x_range_max: Maximum x-coordinate in the complex plane.
     * - y_range_min: Minimum y-coordinate in the complex plane.
     * - y_range_max: Maximum y-coordinate in the complex plane.
     * - max_iter: Maximum number of iterations.
     * Returns: A 2D vector representing the Mandelbrot set image.
     */
    println!("Generating Mandelbrot set image of size {}x{}", width, height);
    print!("X range: [{x_range_min:.6}, {x_range_max:.6}], ");
    println!("Y range: [{y_range_min:.6}, {y_range_max:.6}]");

    let mut img: Vec<Vec<u8>> = vec![vec![0; width]; height];

    for y in 0..height {
        for x in 0..width {
            let cx = (x as f64 / width as f64) * (x_range_max - x_range_min) + x_range_min;
            let cy = (y as f64 / height as f64) * (y_range_max - y_range_min) + y_range_min;
            let mut zx = 0.0;
            let mut zy = 0.0;
            let mut iter: u8 = 0;

            while zx * zx + zy * zy < 4.0 && iter < max_iter {
                let tmp = zx * zx - zy * zy + cx;
                zy = 2.0 * zx * zy + cy;
                zx = tmp;
                iter += 1;
            }

            img[y][x] = iter;
        }
    }

    img
}

fn display_image(image: &Vec<Vec<u8>>) {
    /*
     * Display the Mandelbrot set image in the console.
     * Each pixel value is mapped to a character for visualization.
     * 
     * Parameters:
     * - image: A 2D vector representing the Mandelbrot set image.
     * Returns: Nothing.
     */
    for row in image {
        for pixel in row {
            let shade = match pixel {
                0..=1 => '@',
                2 => '%',
                3 => '#',
                4 => 'o',
                5 => 'u',
                6..=8 => '*',
                9..=10 => '=',
                11..=15 => '+',
                16..=20 => ':',
                21..=25 => '.',
                _ => ' ',
            };
            print!("{}", shade);
        }
        println!();
    }
}

fn main() {
    /*
     * Main function to generate and display the Mandelbrot set image.
     */
    let image = generate_mandelbrot_set(
        100, 30,
        -2.0, 1.0,
        -1.0, 1.0,
        100
    );
    display_image(&image);
}
