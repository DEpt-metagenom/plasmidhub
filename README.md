 <img src="https://img.shields.io/github/license/BALINTESBL/plasmidhub" alt="License"> <img src="https://img.shields.io/pypi/v/plasmidhub" alt="PyPI">  <img src="https://github.com/timmerb/Plasmidhub/actions/workflows/tests.yml/badge.svg" alt="Build"> 
 
# Plasmidhub
Plasmidhub is a free and open-source command-line tool for comprehensive plasmid network analysis based on nucleotide sequence similarity. It enables researchers to cluster plasmids and identify genetically related groups using a dynamic, database-independent approach. The approach of plasmidhub: 
* Is applicable to any plasmid
* Provides an unambiguous classification
* Considers the whole sequence of the plasmids

Network visualizations and stats are provided for further analysis.

## Download and Installation
PlasmidHub can be installed easily via PyPI, Bioconda, or directly from GitHub.

### Install via Pip:
```
pip install plasmidhub
```
**Note:** It's highly recommended to use a virtual environment or conda environment.
Recommended environment setup:
```
conda create -n plasmidhub python=3.8
conda activate plasmidhub
```
### Install via Bioconda

If you use Conda for environment management:
```
conda install -c bioconda plasmidhub
```
Make sure you have the bioconda channel configured. If not, configure them with:
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```
### Install from GitHub
To get the latest version:
```
git clone https://github.com/BALINTESBL/plasmidhub.git
cd plasmidhub
pip install .
```
### Dependencies
This tool requires the following external software to be installed:

- [FastANI](https://github.com/ParBLiSS/FastANI)
- [ABRicate](https://github.com/tseemann/abricate)

## Inputs

Plasmidhub requires plasmid FASTA files (.fna or .fa or .fasta). Your FASTA files need to be placed in one directory. Ideally, there are no other files in the directory.

## Usage
Perform plasmid network analysis with default settings by defining only the directory path of your plasmid FASTA files! Or, you can also adjust parameters.
Example usage:
```
% plasmidhub path/to/my/plasmid/FASTA/files --fragLen 1000 --kmer 14 --coverage_threshold 0.5 --ani_threshold 95 --min_cluster_size 4 --plot_k 2.0 3.0 -t 32

```
This command will:

* Compute pairwise ANI using FastANI
* Build a plasmid similarity network
* Save network metrics and statistics (results/statistics)
* Cluster plasmids
* Annotate resistance and virulence genes with ABRicate (results/abricate_results)
* Generate network visualizations (results/plots)

### Key Options

| Category       | Flag                   | Description                             | Default                   |
| -------------- | ---------------------- | --------------------------------------- | ------------------------- |
| **Input**      | `                      | Path to folder with plasmid FASTA files | –                         |
| **FastANI**    | `--fragLen`            | Fragment length                         | `1000`                    |
|                | `--kmer`               | K-mer size                              | `14`                      |
|                | `--coverage_threshold` | Minimum proportion of the plasmid leghts| `0.5`                     |
|                |                        | covered by the matching fragments       |                           |
|                | `--ani_threshold`      | minimum ANI score (after applying       | `95.0`                    |
|                |                        |  coverage threshold)                    |                           | 
| **Clustering** | `--cluster_off`        | Disable clustering                      | –                         |
|                | `--min_cluster_size`   | Minimum cluster size (plasmids)         | `3`                       |
| **ABRicate**   | `--skip_abricate`      | Skip annotation step                    | –                         |
|                | `--abricate_dbs`       | Databases to use e.g.:                  | `plasmidfinder card vfdb` |
|                |                        |  --abricate_dbs ncbi ecoli_vf           |                           |
| **Plotting**   | `--plot_k`             | Range of k values                       | 3 3                       |
|                | `--plot_skip`          | Skips plotting                          |                           |
| **Threads**    | `-t` or `--threads`    | Number of threads                       | `4`                       |

### Plot-only mode 
In plot-only mode, network visualizations can be generated from existing networks directyl, by using --plot_only flag and defining the directory path. In this mode, several parameters can be adjusted.
Example usage:
```
% plasmidhub --plot_only path/to/my/results  --plot_k 3 5 --plot_node_color blue --plot_node_size 500 --plot_node_shape s --plot_figsize 20 20 -t 32

```
| **Plotting**   | `--plot_node_size`     | Size of nodes                           | `900`                     |
|                | `--plot_node_shape`    | Shape of nodes (`o`, `s`, `^`, etc.)    | `o` (circle)              |
|                | `--plot_edge_width`    | Min/max edge width                      | `0.2 2.0`                 |
|                | `--plot_figsize`       | Figure size in inches                   | `25 25`                   |
|                | `--plot_iterations`    | Spring layout iterations                | `100`                     |

Node shapes: 
| **Node shapes**|                        |
|      'o'       | circle                 |
|      'v'       |	triangle_down          |
|      '^'       |	triangle_up            |
|      '<'       |	triangle_left          |
|      '>'       |	triangle_right         |
|      's'       |	square                 |
|      'p'       |	pentagon               |
|      '*'       |	star                   |
|      'h'       |	hexagon1               |
|      'H'       |	hexagon2               |
|      '+'       |	plus                   |
|      'x'    	  | x                      |
|      'D'       |	diamond                |
|      'd'	      | thin diamond           |


<img width="1668" height="1668" alt="image" src="https://github.com/user-attachments/assets/afed18b8-6dbe-44b8-b539-23aa47b4bfb0" />



You can install them with conda:

```bash
conda install -c bioconda fastani abricate
abricate --setupdb

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


