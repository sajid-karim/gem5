# Copyright (c) 2022 The Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
from gem5.resources.resource import Resource, CustomResource
from gem5.simulate.simulator import Simulator
from python.gem5.prebuilt.ara_cva6.ara_cva6_board import cva6Board
from m5.util import addToPath


# collect optional CLI arg for RISCV binary to run
parser = argparse.ArgumentParser(description="Binary to run on system")
parser.add_argument(
    "workload", type=str, help="The disk image or RV binary to execute"
)
parser.add_argument(
    "--argv", type=str, help="CLI argument to the binary", default=""
)
parser.add_argument(
    "--fullsystem", type=bool, help="Set the board to FS mode", default=False
)
args = parser.parse_args()

board = cva6Board(clk_freq="1.2GHz", is_fs=args.fullsystem)

# Set FS or SE mode workload depending on user input
if args.fullsystem:
    command = (
        "echo 'This is running on U74 CPU core.';" + "sleep 1;" + "m5 exit;"
    )
    if args.workload in ["riscv-disk-img", "riscv-ubuntu-20.04-img"]:
        board.set_kernel_disk_workload(
            kernel=Resource("riscv-bootloader-vmlinux-5.10"),
            disk_image=Resource(args.workload),
            readfile_contents=command,
        )
    else:
        board.set_kernel_disk_workload(
            kernel=CustomResource("riscv-bootloader-vmlinux-5.10"),
            disk_image=CustomResource(args.workload),
            readfile_contents=command,
        )
else:
    board.set_se_binary_workload(
        CustomResource(args.workload),
        arguments=args.argv.split(" "),
    )

simulator = Simulator(board=board)
simulator.run()
