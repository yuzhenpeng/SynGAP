## genome annotations polishment
Based on the gene synteny, the potential omissions and errors in the original genome annotations of related species can be found and polished by bidirectional alignment-based homologous gene prediction.
### _dual_
SynGAP _dual_ was a module designed for the mutual gene structure annotation correction of two species, which takes the genome sequences and genome annotations of the correction objects as input.
For example:
```
syngap dual \
--sp1fa=Athaliana_167_TAIR9.fa \
--sp1gff=Athaliana_167_TAIR10.gene.gff3 \
--sp2fa=Arabidopsis_halleri.Ahal2.2.dna.toplevel.fa \
--sp2gff=Arabidopsis_halleri.Ahal2.2.52.gff3 \
--sp1=Ath \
--sp2=Aha
```
In the _results_ directory, there are several key output files:

| *.SynGAP.gff3 | the full polished genome annotation file (originnal + polished) |
| --- | --- |
| *.SynGAP.clean.gff3 | the polished genome annotation file (only polished) |
| *.SynGAP.clean.miss_annotated.gff3 | only the polished annotations that are miss-annotated in the originnal genome annotation |
| *.SynGAP.clean.mis_annotated.gff3 | only the polished annotations that are mis-annotated in the originnal genome annotation |
| *.anchors.gap | the _gaps_ where mis-annotation or miss-annotation of gene models (MAGs) may exist |

### _master_
You can also chosse to polish the gene structural annotations of one species with the Core set picked up by us. Core set includes several plant and animal species with high quality genome annotation:

| **plant** | **animal** |
| --- | --- |
| _Aristolochia fimbriata_ | _Bos taurus_ |
| _Arabidopsis thaliana_ | _Caenorhabditis elegans_ |
| _Brachypodiumdistachyon_ | _Canis lupus familiaris_ |
| _Cucumis sativus_ | _Drosophila melanogaster_ |
| _Citrus sinensis_ | _Danio rerio_ |
| _Fragaria vesca_ | _Felis catus_ |
| _Glycine max_ | _Gallus gallus_ |
| _Musa acuminata_ | _Homo sapiens_ |
| _Oryza sativa_ | _Mus musculus_ |
| _Solanum lycopersicum_ | _Ovis aries_ |
| _Vitis vinifera_ | _Pan troglodytes_ |
| _Zea mays_ | _Sus scrofa_ |
|  | _Xenopus tropicalis_ |

To use SynGAP master, you should first download the database from the link below, which include plant.tar.gz and animal.tar.gz. You can choose the one you need.
[https://tbtools.cowtransfer.com/s/85ed3920aa7f47](https://tbtools.cowtransfer.com/s/85ed3920aa7f47)
Then import the downloaded database:
```
syngap initdb \
--sp=plant \
--file=plant.tar.gz
```
After import the database, run SynGAP _master_:
```
syngap master \
--sp=plant \
--sp1fa=Brassica_rapa_ro18.SCU_BraROA_2.3.dna.toplevel.fa \
--sp1gff=Brassica_rapa_ro18.SCU_BraROA_2.3.53.chr.gff3 \
--sp1=Bra
```
### _triple_
As for the polishment of three species in combination, you can choose SynGAP _triple._
```
syngap triple \
--sp1fa=Athaliana_167_TAIR9.fa \
--sp1gff=Athaliana_167_TAIR10.gene.gff3 \
--sp2fa=Arabidopsis_halleri.Ahal2.2.dna.toplevel.fa \
--sp2gff=Arabidopsis_halleri.Ahal2.2.52.gff3 \
--sp3fa=Brassica_rapa_ro18.SCU_BraROA_2.3.dna.toplevel.fa \
--sp3gff=Brassica_rapa_ro18.SCU_BraROA_2.3.53.chr.gff3 \
--sp1=Ath \
--sp2=Aha \
--sp3=Bra
```
### _custom_
If you only focus on the annotation polishment in specific synteny block, or prefer to use synteny results from other software rather than jcvi, you can offer the _*.anchors_ file that contains the block  and use SynGAP _custom_.
```
syngap custom \
--sp1fa=Athaliana_167_TAIR9.fa \
--sp1gff=Athaliana_167_TAIR10.gene.gff3 \
--sp2fa=Arabidopsis_halleri.Ahal2.2.dna.toplevel.fa \
--sp2gff=Arabidopsis_halleri.Ahal2.2.52.gff3 \
--custom_anchors=Ath.Aha.originalid.anchors \
--sp1=Ath \
--sp2=Aha
```
## **gene differential expression analysis of related species**
SynGAP incorporates another function module, _genepair_, to generate high-confidence cross-species homologous gene pairs by combining the improved synteny (from SynGAP _dual_ or _triple_) and best two-way BLAST. And SynGAP _evi_ can adopte another parameter, expression variation index (_EVI_), which is calculated based on the gene expression level, the difference in expression level, and the difference of the expression trend in a time-series transcriptome data.
### _genepair_
SynGAP _genepair_ takes the genome sequences and genome annotations of the paired objects as input.
```
syngap genepair \
--sp1fa=Can.fa \
--sp1gff=Can.SynGAP.gff3 \
--sp2fa=Sly.fa \
--sp2gff=Sly.SynGAP.gff3 \
--sp1=Can \
--sp2=Sly
```
SynGAP _genepair_ will generate several key output files (see below), and _*.*.final.genepair_ will used in SynGAP _evi_.

| *.final.genepair | the full gene pairs file (syntenic + best two-way BLAST) |
| --- | --- |
| *.Synteny.genepair | the syntenic gene pairs |
| *.2wayblast.genepair | the best two-way BLAST gene pairs |

### _evi_
Base on the gene pairs between two species and the time-series transcriptome data, _evi_ calculates the _EVI_ for each gene pair.
```
syngap evi \
--genepair=Can.Sly.final.genepair \
--sp1exp=Can.S1_S7.transcript.TPM.xls \
--sp2exp=Sly.S1_S7.transcript.TPM.xls
```
There are several key output files:

| *.final.genepair.EVI.xls | the final EVI result file, in which the gene pairs are ranked by _EVI_ |
| --- | --- |
| *.final.genepair.EVI.threshold.txt | the threshold of _EVI_. The gene pairs with _EVI_ exceeding the threshold were considered to show marked differential expression signals |
| *.final.genepair.EVI.pdf | the ranked dotplot of _EVI_ for all gene pairs |
| *.final.genepair.EVI.indexweight.pdf | the stacked barplot of the three indexes contributing to _EVI_, which can help to adjust the weight of three indexes |
| *.final.genepair.EVI.indexweightratio.pdf | the percentage stacked barplot of the three indexes contributing to _EVI_, which can help to adjust the weight of three indexes |

### _eviplot_
If you are interested in specific gene pairs, you can highlight them using _eviplot_.
```
syngap eviplot \
--EVI=Can.Sly.final.genepair.EVI.xls \
--highlightid=highlight.id \
--outgraph=Can.Sly.highlight.EVI.pdf
```
The format of _highlight.id_ is like follow:

| GeneID1 | GeneID2 | Label |
| --- | --- | --- |
| Capana06g001783 | transcript:Solyc06g059840.3.1 | CaBCKDH |
| Capana02g002339  | transcript:Solyc02g081745.1.1  | CaAT3 |
| Capana04g000751  | transcript:Solyc04g077240.3.1 | CaBCAT |

