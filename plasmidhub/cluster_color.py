import os
import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)

def assign_cluster_colors(results_dir, mapping_file):
    cluster_list_path = os.path.join(results_dir, "cluster_list.txt")
    color_file = os.path.join(results_dir, "cluster_colours.txt")
    
    clusters = []
    with open(cluster_list_path) as f:
        next(f)  # Skip header
        for line in f:
            if line.strip():
                cluster_file, _ = line.strip().split('\t')
                cluster = cluster_file.replace('.txt', '')
                clusters.append(cluster)

    # Use a perceptually distinct color palette (e.g., tab20)
    cmap = plt.get_cmap('tab20')
    base_colors = cmap.colors

    # Cycle colors if needed
    n_clusters = len(clusters)
    full_color_list = (base_colors * ((n_clusters // len(base_colors)) + 1))[:n_clusters]

    color_map = {
        cluster: '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
        for cluster, (r, g, b) in zip(clusters, full_color_list)
    }

    with open(color_file, 'w') as out:
        for cluster, color in color_map.items():
            out.write(f"{cluster}\t{color}\n")

    logger.info(f"Cluster colors saved to: {color_file}")
