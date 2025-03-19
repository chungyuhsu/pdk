## Installation

## Tutorial

### Current Components
| Name | Description |
|-|-|
| component | Basic class |
| mmi1x2 | 1×2 MMI |
| mmi2x2 | 2×2 MMI |
| fgc | Focusing grating coupler |
| ec | Edge coupler |
| stitch | Field crossing |
| wgcrossing | Waveguide crossing |
| mzi1x2 | Balanced 1×2 MZI |
| mzi2x2 | Balanced 2×2 MZI |
| via | Contact between two metal layers |
| alignEBL | Alignment mark for EBL |
| alignPLG | Alignment mark for PLG |
| dice | Dicing mark |
| box | For depth measurement |
| wiring | For metal wiring |
| routing | For waveguide routing |
| spiral | Archimedean spiral |
| ring | Ring resonator |
| bend | Waveguide bending |
| cascaded_mmi1x2 | 1×2 MMI test structure |
| cascaded_mmi2x2 | 2×2 MMI test structure |
| heater | Heater for probe testing |
| metalens | Metalens designed by Ping-Yen |


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

## Maintenance
- For convenience, we only use one cell named 'cell'.
- Each component has its folder. Please refer to the Folder Structure.

### Folder Structure
```bash
/pdk
 ├── main.py
 ├── tool.py # Some useful math tools
 ├── README.md # This file
 ├── image/ # Store the images used in README.md
 ├── component/
     ├── component.py # Code for generating component
     ├── component.gds
     ├── README.md # Describe component
     ├── image/ # Store the images used in README.md
 ├── mmi1x2/
 ├── mmi2x2/
 ├── fgc/
```