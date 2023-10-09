print("""This repository uses RiboTree-mRNA to optimize our mRNA sequences. However, the files related to RiboTree
have been omitted from the repository since the tool is distributed with a license. The following sequences
have been optimized.
      
1. Anti PD1
2. Anti PD1 nanobody
3. Q-IL6-9 antibody
4. Q-IL6-9 nanobody
5. O-IL8-15 antibody
6. O-IL8-15 nanobody
7. CD36
      
SOME OTHER THINGS TO INSTALL:
$ sudo apt-get install gfortran
$ sudo apt-get install liblapack-dev liblapacke-dev
$ pip install setuptools networkx matplotlib scipy numpy pandas
      
ARNIE FILE:
#Path to EternaFold
eternafold: /path/to/mRNA-Optimization/eternafold/src

# Vienna RNAfold 2 Linux build from source:
vienna: /path/to/mRNA-Optimization/ViennaRNA-2.6.3/src/bin
vienna_2: /path/to/mRNA-Optimization/ViennaRNA-2.6.3/src/bin

# CONTRAfold build
contrafold_2: /path/to/mRNA-Optimization/contrafold-se/src

# LinearFold build
linearfold: /path/to/mRNA-Optimization/LinearFold/bin

#LinearPartition build
linearpartition: /path/to/mRNA-Optimization/LinearPartition/bin

#directory to write temp files
TMP: /tmp
       """)