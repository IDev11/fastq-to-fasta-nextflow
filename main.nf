#!/usr/bin/env nextflow

/*
 * FASTQ to FASTA Conversion Pipeline
 * A simple Nextflow pipeline that converts sequencing reads from FASTQ format to FASTA format
 */

// Default parameters
params.input = params.input ?: 'data/*.fastq'
params.outdir = params.outdir ?: 'results'

log.info """
         ===================================
         FASTQ to FASTA Conversion Pipeline
         ===================================
         input    : ${params.input}
         outdir   : ${params.outdir}
         """
         .stripIndent()

// Input channel for FASTQ files
Channel
    .fromPath(params.input)
    .ifEmpty { error "Cannot find any FASTQ files matching: ${params.input}" }
    .set { fastq_ch }

/*
 * Process: Convert FASTQ to FASTA
 */
process FASTQ_TO_FASTA {
    tag "$fastq.simpleName"
    publishDir params.outdir, mode: 'copy'

    input:
    path fastq
    
    output:
    path "*.fasta"
    
    script:
    """
    python $projectDir/bin/fastq_to_fasta.py $fastq ${fastq.simpleName}.fasta
    """
}

/*
 * Process : Count sequences in FASTA file
 */
process Count_Fasta_Sequences {
    tag "$fasta.simpleName"
    publishDir params.outdir, mode: 'copy'
    
    input:
    path fasta

    output:
    path "*.txt"

    script:
    """
    python $projectDir/bin/count_fasta_sequences.py $fasta ${fasta.simpleName}_count.txt
    """
}

/*
 * Workflow
 */
workflow {
    converted = FASTQ_TO_FASTA(fastq_ch)
    Count_Fasta_Sequences(converted)
}