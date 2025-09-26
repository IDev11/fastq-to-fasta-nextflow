#!/usr/bin/env python3
"""
FASTQ to FASTA Converter

A simple Python script to convert sequencing reads from FASTQ format to FASTA format.
This is a placeholder implementation that will be enhanced in future versions.

Usage:
    python fastq_to_fasta.py input.fastq output.fasta
"""

import sys
import argparse
from pathlib import Path


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert FASTQ files to FASTA format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "input_fastq",
        type=Path,
        help="Input FASTQ file path"
    )
    parser.add_argument(
        "output_fasta",
        type=Path,
        help="Output FASTA file path"
    )
    return parser.parse_args()


def fastq_to_fasta(input_file, output_file):
    """
    Convert FASTQ file to FASTA format.
    
    Args:
        input_file (Path): Path to input FASTQ file
        output_file (Path): Path to output FASTA file
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            line_count = 0
            for line in infile:
                line = line.strip()
                if line_count % 4 == 0:  # Header line (starts with @)
                    if line.startswith('@'):
                        # Convert @ to > for FASTA header
                        fasta_header = '>' + line[1:]
                        outfile.write(fasta_header + '\n')
                    else:
                        raise ValueError(f"Expected FASTQ header line starting with '@', got: {line}")
                elif line_count % 4 == 1:  # Sequence line
                    outfile.write(line + '\n')
                # Skip quality header (line_count % 4 == 2) and quality scores (line_count % 4 == 3)
                line_count += 1
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied accessing files.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function."""
    args = parse_arguments()
    
    print(f"Converting {args.input_fastq} to {args.output_fasta}")
    
    # Ensure input file exists
    if not args.input_fastq.exists():
        print(f"Error: Input file '{args.input_fastq}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    args.output_fasta.parent.mkdir(parents=True, exist_ok=True)
    
    # Perform conversion
    fastq_to_fasta(args.input_fastq, args.output_fasta)
    
    print(f"Conversion completed successfully!")
    print(f"Output saved to: {args.output_fasta}")


if __name__ == "__main__":
    main()