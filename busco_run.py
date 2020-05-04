import subprocess
from glob import glob
from itertools import product
from os.path import basename, splitext

path_to_samples = "/home/tooi/Study_IB/baikal_project_spring2020/RNA_seqs/data_for_assembly/assembles/*.fa*"
path_to_lineages = "/home/tooi/Study_IB/baikal_project_spring2020/busco-master/linages/*"

samples = glob(path_to_samples)
lineages = glob(path_to_lineages)
print(f"Found samples: {samples}")
print(f"Found lineages: {lineages}")

subprocess.run(
    ("export", "BUSCO_CONFIG_FILE=/home/tooi/Study_IB/baikal_project_spring2020/busco-master/config/config.ini"), shell=True
)

for sample in samples:
    output_name = f"{splitext(basename(sample))[0]}_prok"
    cmd = (
        "busco",
        "-m", "transcriptome",
        "-i", sample,
        "-o", output_name,
        "--auto-lineage-prok"
    )
    print(f"Start {' '.join(cmd)}")
    process = subprocess.run(
        cmd, check=True
    )
    print(f"Finished {process.args}")

for sample in samples:
    output_name = f"{splitext(basename(sample))[0]}_euk"
    cmd = (
        "busco",
        "-m", "transcriptome",
        "-i", sample,
        "-o", output_name,
        "--auto-lineage-euk"
    )
    print(f"Start {' '.join(cmd)}")
    process = subprocess.run(
        cmd, check=True
    )
    print(f"Finished {process.args}")

for sample, lineage in product(samples, lineages):
    output_name = f"{splitext(basename(sample))[0]}_{splitext(basename(lineage))[0]}"
    cmd = (
        "busco",
        "-m", "transcriptome",
        "-i", sample,
        "-o", output_name,
        "-l", lineage
    )
    print(f"Start {' '.join(cmd)}")
    process = subprocess.run(
        cmd, check=True
    )
    print(f"Finished {process.args}")
