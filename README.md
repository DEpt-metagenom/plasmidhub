 <img src="https://img.shields.io/github/license/BALINTESBL/plasmidhub" alt="License"> <img src="https://img.shields.io/pypi/v/plasmidhub" alt="PyPI">  <img src="https://github.com/timmerb/Plasmidhub/actions/workflows/tests.yml/badge.svg" alt="Build"> 
 
# Plasmidhub
Plasmidhub is a free and open-source command-line tool for comprehensive plasmid network analysis based on nucleotide sequence similarity. It enables researchers to cluster plasmids and identify genetically related groups using a dynamic, database-independent approach.

## Download and Installation

Recommended environment setub

conda create -n plasmidhub_env python=3.10
conda activate plasmidhub_env

### Clone and install

git clone https://github.com/BALINTESBL/plasmidhub.git
cd Plasmidhub
pip install .

### Dependencies

This tool requires the following external software to be installed and available in PATH:

- [FastANI](https://github.com/ParBLiSS/FastANI)
- [ABRicate](https://github.com/tseemann/abricate)

## Inputs

## Usage

```bash
plasmidhub path/to/my/plasmid/FASTA/files --fragLen 1000 --kmer 14 --coverage_threshold 0.5 --ani_threshold 95 --min_cluster_size 4 --plot_k 2.0 3.0 -t 32

plasmidhub --plot_only path/to/my/results  --plot_k 3 3 --plot_node_color white --plot_node_size 500 --plot_node_shape s -t 32

```


<img width="1668" height="1668" alt="image" src="https://github.com/user-attachments/assets/afed18b8-6dbe-44b8-b539-23aa47b4bfb0" />



You can install them with conda:

```bash
conda install -c bioconda fastani abricate
abricate --setupdb

# Plasmidhub

**Plasmidhub** is a free and open-source command-line tool for comprehensive plasmid network analysis based on nucleotide sequence similarity. It enables researchers to cluster plasmids and identify genetically related groups using a dynamic, database-independent approach.

---

## Overview

Plasmidhub performs an **all-vs-all comparison** of input plasmid sequences using [FastANI] (https://github.com/ParBLiSS/FastANI), and builds a similarity network where:
- **Nodes** represent plasmids
- **Edges** represent genetic relatedness based on shared ANI

The tool clusters plasmids based on complete subgraph (clique) detection, identifying highly similar plasmid groups. This approach is **alignment-free**, **reference-free**, **databese-independent**, and uses relative system instead of database dependency.

Network visualizations and network statistics are provided for further analysis.

Resistance and virulence genes can optionally be annotated using [ABRicate](https://github.com/tseemann/abricate).

---

## Features

- Full-sequence plasmid comparisons using FastANI
- Customizable fragment length and k-mer size
- Dynamic ANI and coverage thresholding
- Graph-based clustering via community detection
- Optional annotation with ABRicate (plasmidfinder, card, vfdb, etc.)
- Network visualization and exportable outputs
- Statistics for downstream analyses (Connectance, modularity, nestedness, community partition, degree centrality, node degrees, betweenness, closeness ect.)

---

## Input Requirements

- A directory containing plasmid **nucleotide FASTA files**  
  Accepted extensions: `.fna`, `.fa`, `.fasta`
- Preferably, no other files in the input directory
- Each file should represent a **single plasmid**

---

## Example Usage

```bash
plasmidhub path/to/plasmid_dir \
  --fragLen 1000 \
  --kmer 14 \
  --coverage_threshold 0.5 \
  --ani_threshold 95 \
  --min_cluster_size 4 \
  --plot_k 2.0 3.0 \
  -t 32

---

Developed by **Dr. Bálint Timmer**,  
*Institute of Metagenomics, University of Debrecen, Debrecen, Hungary*  
Contact: [timmer.balint@med.unideb.hu](mailto:timmer.balint@med.unideb.hu)


