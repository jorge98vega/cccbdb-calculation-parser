# cccbdb.nist.gov Calculation Parser

Pulls all calculation information from cccbdb.nist.gov for the specified chemical formula

## Setup

* Install Python 3 (Python 3.12.0)

* Clone the repo to your machine

`git clone https://github.com/jorge98vega/cccbdb-calculation-parser.git`

`git clone git@github.com:jorge98vega/cccbdb-calculation-parser.git`

* Install script dependencies

`cd cccbdb-calculation-parser`

`pip install -r requirements.txt`

## Usage

* Run the script by supplying the following command line arguments

`python cccbdb.py CALCULATION FORMULA [DEPTH] [DEEP_FILTERS]`

* Run this other script if you want to parse a local html file `DIRECTORY/FORMULA.CALCULATION.html` downloaded from cccbdb.nist.gov (equivalent to shallow depth)

`python cccbdb2.py CALCULATION FORMULA [DIRECTORY]`

**You get the calculation name from the ccbdb url**  
i.e. the calculation name for this url *https://cccbdb.nist.gov/polcalc1x.asp* is "polcalc"

## Examples

`python cccbdb.py dipole CH4 shallow`

`python cccbdb.py geom CH4 deep`

`python cccbdb.py geom CH4 deep '[{"method": "LSDA"}, {"method": "BLYP"}]'`

`python cccbdb.py geom CH4 deep '[{"method": "LSDA", "basis": "6-31G"}]'`

Deep will go into the cell's url and pull out the components, shallow will not.

* The script will run through extracting the data.  It will create the output files in your current path with the output.

## Screenshots

![Console](screenshots/console.jpg)

![output](screenshots/output.jpg)
