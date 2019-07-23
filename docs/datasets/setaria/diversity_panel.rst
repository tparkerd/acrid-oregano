#######################
Setaria Diversity Panel
#######################

Genotype, Individual, and Position (.012, .indv, .pos) files were generated
from the original files:

``2.from12.setaria.maf0.1.maxMissing0.1.allLines.012``
``2.from12.setaria.maf0.1.maxMissing0.1.allLines.012.indv``
``2.from12.setaria.maf0.1.maxMissing0.1.allLines.012.pos``

The population structure file (6.Eigenstrat.population.structure.50PCs.csv)
has been modified from the original copy because the column names were
shifted left by one. Therefore, I added the 'Pedigree' column title and
shifted the V# headings to the right, adding V50 to the final column.

The mappings for weird namings for line/pedigrees is in the file
Setaria_597_diversity_samples.csv
Still need to include the conversion in the script. Or! Modify the existing
files to use them expected pedigree labels instead of the strange 
XXXX_XXXX_XXXX_XXXX construction.

*****
Files
*****

.. literalinclude:: ../../_static/files/setaria.json
    :caption: :download:`Download setaria.json <../../_static/files/setaria.json>`
    :name: setaria.json
    :language: json
    :linenos:

.012 (Genotype file)
Format: