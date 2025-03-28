## Installation
❗This PDK has only been tested on Windows 11. If you're using a different operating system, such as macOS or Linux, you'll need to troubleshoot issues on your own.
1. Install Anaconda (https://www.anaconda.com).
2. Create a new environment.
3. Install all dependencies in the new environment.
4. Download this PDK from GitHub (https://github.com/chungyuhsu/pdk).
5. Decompress the ZIP file to any place you want.
6. Enjoy it!

### Dependencies
- **python 3.8.20**\
Newer version is not supported.
- **gdspy 1.6.12**\
Download and install it directly from GitHub (https://github.com/heitzmann/gdspy/releases/tag/v1.6.12).
- **numpy**

## Tutorial

### Component List
| Name | Description |
|-|-|
| Component | Basic template for the other components|
| Mmi1x2 | 1×2 MMI |
| Mmi2x2 | 2×2 MMI |
| Waveguide | Waveguide |
| Bend_euler ||
| Gc_fully ||
| Gc_partially ||
| Template ||

### Layer Information
- This is just for reference. You can define your own layer.
- Datatype must be zero for non-zero layer.

| Layer | Datatype | Description |
| - | - | - |
| 0 | 0 | Port labels |
| 0 | 1 | Chip |
| 0 | 2 | Fields |
| 10 | 0 | Fully etched layer: low dosage |
| 11 | 0 | Fully etched layer: medium dosage |
| 12 | 0 | Fully etched layer: high dosage |
| 13 | 0 | Fully etched layer: ultra dosage |
| 20 | 0 | Partially etched layer |
| 30 | 0 | Heater layer |
| 40 | 0 | Wiring layer |

## Build Your Own Components
- For convenience, we only use one cell named 'cell'.
- Each component has its folder. Each folder with a component inside is a package.
- It is necessary to create documents for your component. So people can understand how to use it.
- Port 'og' is essential for put method.
- All images must be saved as .png and <500 KB
- For each optical component, there is at least one optical port named 'o0'.