#!/usr/bin/env python3
"""
Count FASTA Sequences

A simple script to count the number of sequences in a FASTA file.
Usage:
    python count_fasta_sequences.py input.fasta output.txt
"""

import sys
import argparse
from pathlib import Path


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Count the number of sequences in a FASTA file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "input_fasta",
        type=Path,
        help="Input FASTA file path"
    )
    parser.add_argument(
        "output_txt",
        type=Path,
        help="Output file path for the sequence count"
    )
    return parser.parse_args()


def fasta_seq_count(input_file: Path, output_file: Path):
    """Count sequences in FASTA and write the result."""
    try:
        seq_count = 0
        with open(input_file, 'r') as infile:
            for line in infile:
                if line.startswith('>'):
                    seq_count += 1

        with open(output_file, 'w') as outfile:
            outfile.write(f"{input_file.name}: {seq_count} sequence(s)\n")

        print(f"Counted {seq_count} sequences in {input_file}")

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

    # Ensure input file exists
    if not args.input_fasta.exists():
        print(f"Error: Input file '{args.input_fasta}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Create output directory if it doesn't exist
    args.output_txt.parent.mkdir(parents=True, exist_ok=True)

    # Perform counting
    fasta_seq_count(args.input_fasta, args.output_txt)


if __name__ == "__main__":
    main()
