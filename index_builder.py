# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

chunk_size = 1024
source_data = "source_data/"
remap_dir = "remapped_benchmarks/"

benchmark_suites = [
  "Snappy-COMPRESS",
  "Snappy-DECOMPRESS",
  "ZSTD-COMPRESS",
  "ZSTD-DECOMPRESS",
]

index_to_fname = [
  "Calgary/bib",
  "Calgary/book1",
  "Calgary/book2",
  "Calgary/geo",
  "Calgary/news",
  "Calgary/obj1",
  "Calgary/obj2",
  "Calgary/paper1",
  "Calgary/paper2",
  "Calgary/pic",
  "Calgary/progc",
  "Calgary/progl",
  "Calgary/progp",
  "Calgary/trans",
  "Canterbury/alice29.txt",
  "Canterbury/asyoulik.txt",
  "Canterbury/cp.html",
  "Canterbury/fields.c",
  "Canterbury/grammar.lsp",
  "Canterbury/kennedy.xls",
  "Canterbury/lcet10.txt",
  "Canterbury/plrabn12.txt",
  "Canterbury/ptt5",
  "Canterbury/sum",
  "Canterbury/xargs.1",
  "Silesia/dickens",
  "Silesia/mozilla",
  "Silesia/mr",
  "Silesia/nci",
  "Silesia/ooffice",
  "Silesia/osdb",
  "Silesia/reymont",
  "Silesia/samba",
  "Silesia/sao",
  "Silesia/webster",
  "Silesia/xml",
  "Silesia/x-ray",
  "Snappy/fireworks.jpeg",
  "Snappy/geo.protodata",
  "Snappy/html",
  "Snappy/html_x_4",
  "Snappy/kppkn.gtb",
  "Snappy/paper-100k.pdf",
  "Snappy/urls.10K",
]


fname_to_index = dict()
for index, filename in enumerate(index_to_fname):
  fname_to_index[filename] = index


