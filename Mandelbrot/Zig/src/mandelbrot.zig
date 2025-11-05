//! Mandelbrot set generator and ASCII visualizer in Zig
//! This program generates a Mandelbrot set image and displays it in the console using ASCII characters.
//! It demonstrates basic numerical computation and console output in Zig.
//! 🐻
//!
//! Author: Oliver Merkel
//! Date: 2025-11-01
//! License: MIT
//!
//! Usage:
//! - Compile and run the program to see the Mandelbrot set displayed in the console.
const std = @import("std");

// Mandelbrot set parameters
const WIDTH: usize = 100;
const HEIGHT: usize = 30;
const X_MIN: f64 = -2.0;
const X_MAX: f64 = 1.0;
const Y_MIN: f64 = -1.0;
const Y_MAX: f64 = 1.0;
const MAX_ITER: u8 = 100;

/// Generate Mandelbrot set image as a 2D array of iteration counts
///
/// parameters:
///     width: image width
///     height: image height
///     x_min, x_max: range of x values
///     y_min, y_max: range of y values
///     max_iter: maximum number of iterations
/// returns:
///     2D array of iteration counts
fn generateMandelbrotSet(width: usize, height: usize, x_min: f64, x_max: f64, y_min: f64, y_max: f64, max_iter: u8) [HEIGHT][WIDTH]u8 {
    std.debug.print("Generating Mandelbrot set image of size {}x{}\n", .{ width, height });
    std.debug.print("X range: [{d:.6}, {d:.6}], ", .{ x_min, x_max });
    std.debug.print("Y range: [{d:.6}, {d:.6}]\n", .{ y_min, y_max });

    var img: [HEIGHT][WIDTH]u8 = [_][WIDTH]u8{[_]u8{0} ** WIDTH} ** HEIGHT;
    var y: usize = 0;
    while (y < height) : (y += 1) {
        var x: usize = 0;
        while (x < width) : (x += 1) {
            const cx = (@as(f64, @floatFromInt(x)) / @as(f64, @floatFromInt(width))) * (x_max - x_min) + x_min;
            const cy = (@as(f64, @floatFromInt(y)) / @as(f64, @floatFromInt(height))) * (y_max - y_min) + y_min;
            var zx: f64 = 0.0;
            var zy: f64 = 0.0;
            var iter: u8 = 0;
            while (zx * zx + zy * zy < 4.0 and iter < max_iter) : (iter += 1) {
                const tmp = zx * zx - zy * zy + cx;
                zy = 2.0 * zx * zy + cy;
                zx = tmp;
            }
            img[y][x] = iter;
        }
    }
    return img;
}

/// Display Mandelbrot set image in ASCII characters in the console.
///
/// parameters:
///     img: 2D array of iteration counts
/// returns:
///     void
fn displayImage(img: *const [HEIGHT][WIDTH]u8) void {
    var y: usize = 0;
    while (y < HEIGHT) : (y += 1) {
        var x: usize = 0;
        while (x < WIDTH) : (x += 1) {
            const pixel = img[y][x];
            const shade: u8 = switch (pixel) {
                0, 1 => '@',
                2 => '%',
                3 => '#',
                4 => 'o',
                5 => 'u',
                6, 7, 8 => '*',
                9, 10 => '=',
                11...15 => '+',
                16...20 => ':',
                21...25 => '.',
                else => ' ',
            };
            std.debug.print("{c}", .{shade});
        }
        std.debug.print("\n", .{});
    }
}

/// Main function
pub fn main() void {
    const img = generateMandelbrotSet(WIDTH, HEIGHT, X_MIN, X_MAX, Y_MIN, Y_MAX, MAX_ITER);
    displayImage(&img);
}
