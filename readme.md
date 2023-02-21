# Transpose LaTeX Tables

This script can be used to transpose LaTeX tables. Simply copy and paste your 
current LaTeX tabular field in `transpose_latex_tables.py`, run the script and 
copy and paste the output back to LaTeX.

However, note that this script is not clever and will not work for all LaTeX 
tables. Things like midrules, multirow, multicolumn, etc. will not work. Only 
straight forward tables with "&" and "\\" will work. Also, this script only takes the main "tabular" part of the table as input. 
 
The script is tested with Python 3.8. 
