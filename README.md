# fastq-to-fasta-nextflow

A simple Nextflow pipeline that converts sequencing reads from FASTQ format to FASTA format using a custom Python script. Built for learning and practicing workflow automation in bioinformatics.

## Project Structure

```
fastq-to-fasta-nextflow/
├── main.nf                    # Main Nextflow pipeline script
├── bin/
│   └── fastq_to_fasta.py     # Python script for FASTQ to FASTA conversion
├── data/                      # Directory for input FASTQ files
│   └── .gitkeep
├── results/                   # Directory for output FASTA files
│   └── .gitkeep
├── README.md                  # This file
└── .gitignore                # Git ignore file for Python and Nextflow
```

## Requirements

- [Nextflow](https://www.nextflow.io/) (version 21.04 or later)
- Python 3.6 or later
- Input FASTQ files

## Usage

### Basic Usage

1. Place your FASTQ files in the `data/` directory
2. Run the pipeline:

```bash
nextflow run main.nf
```

### Custom Parameters

You can specify custom input and output paths:

```bash
nextflow run main.nf --input "path/to/your/*.fastq" --outdir "path/to/output"
```

### Parameters

- `--input`: Pattern for input FASTQ files (default: `$projectDir/data/*.fastq`)
- `--outdir`: Output directory for FASTA files (default: `$projectDir/results`)

## Example

```bash
# Run with default parameters (uses files in data/ directory)
nextflow run main.nf

# Run with custom input path
nextflow run main.nf --input "/path/to/fastq/files/*.fastq"

# Run with custom input and output paths
nextflow run main.nf --input "/path/to/fastq/*.fastq" --outdir "/path/to/output"
```

## Output

The pipeline will generate FASTA files with the same base name as the input FASTQ files in the specified output directory.

## Python Script

The `bin/fastq_to_fasta.py` script can also be used independently:

```bash
python bin/fastq_to_fasta.py input.fastq output.fasta
```

## Development

This is a learning project for bioinformatics workflow automation. The Python script provides a basic implementation of FASTQ to FASTA conversion that can be enhanced with additional features as needed.

## License

This project is open source and available under the MIT License.
