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

import os

from index_builder import *

indexable_file_contents = []

for filename in index_to_fname:
  with open(os.path.join(source_data, filename), 'rb') as filecontents:
    indexable_file_contents.append(filecontents.read())

output_dir = "extracted_benchmarks/"

try:
  os.mkdir(output_dir)
except FileExistsError:
  pass

for suite in benchmark_suites:
  base_path = os.path.join(remap_dir, suite, '')
  output_path = os.path.join(output_dir, suite, '')
  try:
    os.mkdir(output_path)
  except FileExistsError:
    pass

  all_benchmarks = os.listdir(base_path)

  for benchmark in all_benchmarks:

    output_data = b""
    with open(os.path.join(base_path, benchmark), 'r') as bench_data:
      print(benchmark)
      index_offset_arr = eval(bench_data.read())
      for index, offset in index_offset_arr:
        output_data += indexable_file_contents[index][offset:offset+1024]

    with open(os.path.join(output_path, benchmark), 'wb') as bench_extracted:
      bench_extracted.write(output_data)


