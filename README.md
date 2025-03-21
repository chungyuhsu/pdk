## Installation

## Tutorial

### Component List
| Name | Description |
|-|-|
| component | Basic class |
| mmi1x2 | 1×2 MMI |
| mmi2x2 | 2×2 MMI |

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