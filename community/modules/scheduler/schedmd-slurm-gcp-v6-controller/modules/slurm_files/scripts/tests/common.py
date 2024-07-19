# Copyright 2024 "Google LLC"
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional
import sys
from dataclasses import dataclass, field

SCRIPTS_DIR = "community/modules/scheduler/schedmd-slurm-gcp-v6-controller/modules/slurm_files/scripts"
if SCRIPTS_DIR not in sys.path:
    sys.path.append(SCRIPTS_DIR)  # TODO: make this more robust


# TODO: use "real" classes once they are defined (instead of NSDict)
@dataclass
class TstNodeset:
    nodeset_name: str
    node_count_static: int = 0
    node_count_dynamic_max: int = 0


@dataclass
class TstCfg:
    slurm_cluster_name: str = "m22"
    nodeset: dict[str, TstNodeset] = field(default_factory=dict)
    nodeset_tpu: dict[str, TstNodeset] = field(default_factory=dict)
    output_dir: Optional[str] = None


@dataclass
class TstTPU:  # to prevent client initialization durint "TPU.__init__"
    vmcount: int


def make_to_hostnames_mock(tbl: Optional[dict[str, list[str]]]):
    tbl = tbl or {}

    def se(k: str) -> list[str]:
        if k not in tbl:
            raise AssertionError(f"to_hostnames mock: unexpected nodelist: '{k}'")
        return tbl[k]

    return se