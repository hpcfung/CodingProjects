## Dependencies
- prettytable (just for characterization, used once)

Also data (COMSOL?)

## Usage
See `.py` for sample script, for typical usage

initialize object; print and return voltages?

more advanced features: change default args

or change code/logic (eg micromotion optimization)



## FAQ

### Units
see section, of report

(nondim, then dim in the end?)

## Changes
Compared to `voltage_optimization_and_characterization.ipynb`
- all characterization removed?

## TODO

default params
- quadratic
- weights
- nondim = False

leave characterization as legacy code?

micromotion: DC null and AC null, another optimization, another weight

implement rotation: easy, just rotate (x+y)**2, get coeff; eg for cross terms eg xy
