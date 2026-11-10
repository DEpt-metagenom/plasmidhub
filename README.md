[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) <img src="https://img.shields.io/pypi/v/plasmidhub" alt="PyPI">  [![Test Status](https://github.com/BALINTESBL/plasmidhub/actions/workflows/python-tests.yml/badge.svg)](https://github.com/BALINTESBL/plasmidhub/actions/workflows/python-tests.yml)
 
# Plasmidhub
Plasmidhub is a free and open-source command-line tool for comprehensive plasmid network analysis based on nucleotide sequence similarity. It enables researchers to cluster plasmids and identify genetically related groups using a dynamic, database-independent approach. Plasmidhub's approach: 
* Is applicable to any plasmid
* Provides an unambiguous classification
* Considers the whole sequence of the plasmids

Network visualizations, stats and data are provided for further analysis.

## Download and Installation
PlasmidHub can be installed either from PyPI, from Bioconda, or directly from the GitHub source tree. The recommended setup is a dedicated virtual environment or Conda environment, and the external command-line tools FastANI and ABRicate should be installed with Conda before installing the Python package.

### PyPI install
Use this when you want the Python package from PyPI.

```bash
python -m venv .venv
source .venv/bin/activate
conda install -c conda-forge -c bioconda fastani abricate
python -m pip install --upgrade pip
python -m pip install plasmidhub
```

If you prefer Conda instead of a Python venv, use:

```bash
conda create -n plasmidhub python=3.8
conda activate plasmidhub
conda install -c conda-forge -c bioconda fastani abricate
python -m pip install plasmidhub
```

`mamba` can be used as a faster alternative to `conda` for the same setup.

```bash
mamba create -n plasmidhub python=3.8
mamba activate plasmidhub
mamba install -c conda-forge -c bioconda fastani abricate
python -m pip install plasmidhub
```

### Conda install
Use this when you want the package managed entirely in a Conda environment.

```bash
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
conda create -n plasmidhub python=3.8
conda activate plasmidhub
conda install -c bioconda plasmidhub
```

`mamba` can be used as a faster alternative to `conda` for the same workflow.

### GitHub install
Use this when you want to install the latest source code from the repository in a virtual environment.

```bash
git clone https://github.com/DEpt-metagenom/plasmidhub.git
cd plasmidhub
python -m venv .venv
source .venv/bin/activate
conda install -c conda-forge -c bioconda fastani abricate
python -m pip install --upgrade pip
python -m pip install -e .
```

If you prefer Conda instead of a venv:

```bash
git clone https://github.com/DEpt-metagenom/plasmidhub.git
cd plasmidhub
conda create -n plasmidhub-dev python=3.8
conda activate plasmidhub-dev
conda install -c conda-forge -c bioconda fastani abricate
python -m pip install -e .
```

### Docker install
Use this when you want to run Plasmidhub in a containerized environment.

```bash
git clone https://github.com/DEpt-metagenom/plasmidhub.git
cd plasmidhub
docker build -t plasmidhub .
docker run --rm -it plasmidhub --help
```

The container image installs the Conda environment from [environment.yml](environment.yml), including FastANI and ABRicate, then installs the Plasmidhub package itself.

### Running the unit tests
From the project root, run:

```bash
pytest -q
```

If you are using the project Conda environment:

```bash
eval $(conda shell.bash hook)
conda activate plasmidhub
pytest -q
```

### Dependencies
This tool requires the following external software to be installed:
- [FastANI](https://github.com/ParBLiSS/FastANI)
- [ABRicate](https://github.com/tseemann/abricate)
- biopython
- pandas
- networkx
- matplotlib
- python-louvain
- numpy
- scipy

## Inputs
Plasmidhub requires plasmid FASTA files (.fna or .fa or .fasta). Your FASTA files need to be placed in one directory. Ideally, there are no other files in the directory.

## Usage
Perform plasmid network analysis with default settings by defining only the directory path of your plasmid FASTA files! Alternatively, parameters can be adjusted.
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
|                | `--coverage_threshold` | Minimum proportion of the plasmid lenghts| `0.5`                     |
|                |                        |  covered by the matching fragments      |                           |
|                | `--ani_threshold`      | Minimum ANI score (after applying       | `95.0`                    |
|                |                        |  coverage threshold)                    |                           | 
| **Clustering** | `--cluster_off`        | Disable clustering                      | –                         |
|                | `--min_cluster_size`   | Minimum cluster size (plasmids)         | `3`                       |
| **ABRicate**   | `--skip_abricate`      | Skip annotation step                    | –                         |
|                | `--abricate_dbs`       | Databases to use e.g.:                  | `plasmidfinder card vfdb` |
|                |                        |  --abricate_dbs ncbi ecoli_vf           |                           |
| **Plotting**   | `--plot_k`             | Range of k values                       |`3` `3`                    |
|                | `--plot_skip`          | Skips plotting                          |                           |
| **Threads**    | `-t` or `--threads`    | Number of threads                       | `4`                       |
### Plot-only mode 
In plot-only mode, network visualizations can be generated from existing networks directly, by using --plot_only flag and defining the directory path. In this mode, multiple parameters can be adjusted.
Example usage:
```
% plasmidhub --plot_only path/to/my/results  --plot_k 3 5 --plot_node_color blue --plot_node_size 500 --plot_node_shape s --plot_figsize 20 20 -t 32
```
| **Plotting**   | Flag                   | Description                             | Default                   |
| -------------- | ---------------------- | --------------------------------------- | ------------------------- | 
|                | `--plot_node_size`     | Size of nodes                           | `900`                     |
|                | `--plot_node_shape`    | Shape of nodes (`o`, `s`, `^`, etc.)    | `o` (circle)              |
|                | `--plot_node_color`    | Color of nodes (`blue`, `#e8e831`, etc.)| `grey`                    |
|                | `--plot_edge_width`    | Min/max edge width                      | `0.2 2.0`                 |
|                | `--plot_figsize`       | Figure size in inches                   | `25 25`                   |
|                | `--plot_iterations`    | Spring layout iterations                | `100`                     |

Node shapes: 
| Marker | Description                |
| ------ | -------------------------- |
| `'o'`  | Circle                     |
| `'s'`  | Square                     |
| `'^'`  | Upward-pointing triangle   |   
| `'v'`  | Downward-pointing triangle |       
| `'>'`  | Right-pointing triangle    |       
| `'<'`  | Left-pointing triangle     |          
| `'D'`  | Diamond                    |        
| `'d'`  | Thin diamond               |    
| `'p'`  | Pentagon                   |    
| `'h'`  | Hexagon 1                  |               
| `'H'`  | Hexagon 2                  |
|  `'*'` | Star                       |
| `'+'`  | Plus                       |
| `'x'`  | Cross                      |
| `'X'`  | Filled X                   |

Plots generated with Plasmidhub:
<img width="1668" height="1668" alt="image" src="https://github.com/user-attachments/assets/afed18b8-6dbe-44b8-b539-23aa47b4bfb0" />
Nodes represents plasmids, edges represent genetic relatedness (weighted ANI scores). Plasmids are colored by their cluster. Plasmids outside clusters have grey color by default. 

## Overview

Plasmidhub performs an all-vs-all comparison of input plasmid sequences using FastANI. FastANI results ("raw results") are filtered  by the coverage (proportion of the full plasmid sequences covered by the matching fragments). The remaining pairs are filtered by the minimum ANI score. ANI scores are further weighted by the proportion of matching fragments and data are sorted into a similarity matrix. The network is build from the similarity matrix, where:
- **Nodes** represent plasmids
- **Edges** represent genetic relatedness (weighted ANI)

Within the network, communities are detected via Louvain method (subclusters). Plasmid clusters are complete subgraphs (cliques) detected within the whole network. Clusters comprising highly similar or identical plasmids. If relevant and scientifically appropriate, plasmids of the same cluster may be considered as equivalent. This approach is alignment-free, reference-free, database-independent, and uses relative similarity-based system to overcome the limitations of database dependency (untypeable plasmids, multireplicon/multi-MOB plasmids, mosaic, hybrid plasmids ect.)
Network and node statistics are saved to a distinct directory for downstream analyses (connectance, modularity, nestedness, community partition, degree centrality, node degrees, betweenness, closeness ect.)

Resistance and virulence genes can be annotated via [ABRicate](https://github.com/tseemann/abricate). The abricate files are saved to a distinct subdirectory. By default, plasmidfinder, vfdb and card databases are used, but optionally other databases can be specified from the databases available with ABRicate. 

To generate more custom visualizations, feel free to use and modify the *plot.py*.

## Troubleshooting
Users are welcome to report any issue or feedback related to Plasmidhub by posting a [Github issue](https://github.com/BALINTESBL/plasmidhub/issues).

---

 <img width="33" height="33" alt="image" src="https://github.com/user-attachments/assets/bd9f17e9-e9ce-4edb-8319-ef0091c45f00" /> <img width="99" height="32.054" alt="image" src="https://github.com/user-attachments/assets/5f3d5b6b-cef6-478a-af66-614b2e2860b2" />
 
Contact: [timmer.balint@med.unideb.hu](mailto:timmer.balint@med.unideb.hu) , [timmer.balint@pte.hu](mailto:timmer.balint@pte.hu)
