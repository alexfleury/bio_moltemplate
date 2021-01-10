Proteins with OPLS/AA
======
This repo regroups amino acids [Moltemplate](http://moltemplate.org/) files (.lt). This is intended to create [LAMMPS](https://lammps.sandia.gov/) data file for proteins molecular dynamics with the OPLS/AA forcefield.


Here is an example for a GLY-GLY-GLY molecule.
```
import "src/glycine.lt"
import "src/glycine_nterm.lt"
import "src/glycine_cterm.lt"
import "src/oplsaa.lt"

POLYGLY inherits OPLSAA {

m1 = new GLYCINE_NTERM
m2 = new GLYCINE
m3 = new GLYCINE_CTERM

write("Data Bonds") {
    # bond-id bond-type
    $bond:pep1   @bond:003_024   $atom:m1/C  $atom:m2/N
    $bond:pep2   @bond:003_024   $atom:m2/C  $atom:m3/N
    }
}

system = new POLYGLY

write_once("Data Boundary") {
    0.0 99.9 xlo xhi
    0.0 99.9 ylo yhi
    0.0 99.9 zlo zhi
    }
```

To make the data file, here is the command.
```
$ moltemplate.sh foo.lt -pdb foo.pdb
```

## TODO
* Cysteine (SS);
* Cysteine (S-);
* Histidine (+);
* Aspartate (COOH);
* Glutamate (COOH);
* Lysine (NH2);
* Arginine (NH);
* Most of N-terminal and C-terminal;
* Other biomolecules.
