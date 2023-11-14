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

* Run the script by supplying the following command line arguments

`Syntax: python cccbdb.py [calculation] [formula] [deep/shallow]`

* Run this other script if you want to parse a local html file `directory/formula.calculation.html` downloaded from cccbdb.nist.gov

`Syntax: python cccbdb2.py [calculation] [formula] [directory]`

**The calculation name you get from the ccbdb url**  
i.e. the calculation name for this url *https://cccbdb.nist.gov/polcalc1x.asp* is "polcalc"

*Examples:*

`python cccbdb.py geom CH4 deep`

`python cccbdb.py dipole CH4 shallow`

Deep will go into the bond and pull out the components, shallow will not.

* The script will run through extracting the data and outputting status to the console.  It will create a text file in your current path with the output.

# Screenshots

![Console](screenshots/console.jpg)

![output](screenshots/output.jpg)
