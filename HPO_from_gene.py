import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

DISEASE_TERMS=["ACUTE", "LEUKEMIA", "MYELOID"]

genelist = """ANKRD26
RUNX1
CEBPA
ETV6
GATA2
TP53
RUNX1
CEBPA
ETV6
CEBPA
TP53
GATA2
TP53
GATA2
SRP72
RUNX1
DDX41
RTEL1
ACD
SRP72
TP53
SRP72
GATA2
SRP72
SRP72
ALARS
TERT
SRP72
"""
gene_list = set(genelist.strip().split("\n"))

#gets all genes from the export (set as node list include duplicates)
# with open("All_Network_Genes.txt", "rt") as f:
#     gene_list=sorted(set([x.strip("\n") for x in f.readlines()]))


for gene in gene_list:
    #just skip fusions with "/" in for now, should later add them as two entries to the list though
    if "/" in gene:
        continue
    #gets entrez_id (needed for HPO API) from mygene
    gene_request=requests.get(f"https://mygene.info/v3/query?q={gene}&fields=fields%3Dentrezgene%2Csymbol&species=human&entrezonly=true")
    query=json.loads(gene_request.text)
    # print(gene)
    hits = query["hits"]
    gene_id=None
    #skip entries that don't have a hits list for now....
    if hits==[]:
        continue
    for hit in hits:
        #some genes can have many hits, check that the symbol exactly matches the expected hit
        if hit["symbol"]==gene:
            gene_id=hit["_id"]
    if gene_id==None:
        continue
    request = requests.get(f"http://hpo.jax.org/api/hpo/gene/{gene_id}", verify=False)
    #skip things that don't give a valid HTTP response when searching
    if request.status_code!=200:
        continue
    result = json.loads(request.text)
    #print both diseaseAssoc and termAssoc as some genes (that definitely are involved) only have the info
    #in termAssoc not diseaseAssoc
    try:
        for disease in result["diseaseAssoc"]:
            if any(to_check.upper() in disease["diseaseName"].upper() for to_check in DISEASE_TERMS):
                print(f'{gene} - Disease: {disease["diseaseName"]}')
    except:
        print("NO DISEASE ASSOC - {gene}")
    try:
        for term in result["termAssoc"]:
            if any(to_check.upper() in term["name"].upper() for to_check in DISEASE_TERMS):
                print(f'{gene} - Associated Term: {term["name"]}')
    except:
        print("NO TERM ASSOC - {gene}")