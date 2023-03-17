# HyperCompressBench

Version: 0.0.1-alpha

HyperCompressBench is a suite of synthetic compression and decompression
benchmarks representative of Google's usage of general-purpose lossless
compression and decompression algorithms.

Further details will be made available in an upcoming paper at the 50th
International Symposium on Computer Architecture (ISCA 2023).

This is not an officially supported Google product.

## Setup instructions

1. In the `source_data/` directory, reproduce the directory/file structure shown
   in `index_to_fname` in `index_builder.py` by downloading and extracting the
   [Calgary](https://corpus.canterbury.ac.nz/descriptions/#calgary),
   [Canterbury](https://corpus.canterbury.ac.nz/descriptions/#cantrbry),
   [Silesia](https://sun.aei.polsl.pl//~sdeor/index.php?page=silesia), and
   [Snappy](https://github.com/google/snappy/tree/main/testdata) Compression
   Benchmarks to `source_data/`. For example, you should have the file
   `source_data/Calgary/bib` before proceeding.

2. Run the following to produce the HyperCompressBench benchmarks:

    python3 reconstruct.py

3. The HyperCompressBench suites (and files) will now be found in
   `extracted_benchmarks/`. You should end up with the following:

    extracted_benchmarks/
        Snappy-COMPRESS/
            [many files]
        Snappy-DECOMPRESS/
            [many files]
        ZSTD-COMPRESS/
            [many files]
        ZSTD-DECOMPRESS/
            [many files]

