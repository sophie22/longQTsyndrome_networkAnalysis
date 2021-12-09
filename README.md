# Network Analysis for Long QT syndrome

Scripts and files for the network analysis of the PanelApp genes for long QT syndrome.
Was tested and run with Python 3.7.5 on Windows 10.

## Aim of this exercise
The task was to identify candidates genes to expand the current PanelApp panel for a selected disease.

## Analysis steps
We chose long QT syndrome and downloaded the list of genes from PanelApp panel 76 version [2.20](https://nhsgms-panelapp.genomicsengland.co.uk/panels/76/v2.20) (*LongQTsyndrome_PA.tsv*) and provided the list of 22 genes (10 green, 10 red and 2 amber) to Cytoscape 3.9.0 to generate an enriched network. We then used ModuLand 2.0 to identify clusters among the network and up to 10 genes from the resulting 27 cluster are saved in the file *ModuLand_clusters_NCBI.csv*. This file is the input for the *query_NCBI.ipynb* Jupyter Notebook which annotates the genes with gene symbol and organism information by querying NCBI's API (via the Entrez module of the BioPython package).
Running of this notebook generates the _NCBI_human_genes.csv_ and _NCBI_other_genes.csv_, as well as the _NCBI_genes.csv_, which is one of the inputs to the *matrix.ipynb* notebook. The other input is the *longQT_phenotypes.csv* which is the union of unique HPO terms for all long QT syndrome types from the Human Phenotype Ontology's [webiste](https://hpo.jax.org/app/browse/disease/OMIM:192500).

## Scripts written by
Sophie Ratkai and Joe Larkman
