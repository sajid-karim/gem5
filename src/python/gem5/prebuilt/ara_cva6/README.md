# cva6 GEM5 Board Specs and Usage

## Specs for the cva6 Unmatched

### Cache Hierarchy
- L1D Size : 16kB
- L1D Associativity : 4
- L1I Size : 16kB
- L1I Associativity : 4
- Branch Predictor:
    16 entry BTB, 3.6 kiB branch history table, 8 entry indirect jump target predictor, 6 entry RAS

### Memory
- 1GB DDR3 channeled subsystem
- Starting address : 0x80000000

### CPU
- Inherited from MinorCPU
- Latencies: Int inst. (3 cycles), Mul inst. (3 cycles), Mem inst. (3 cycles), Div inst. (6 cycles)

### Board
- Clock Freq.: 1.2 GHz (base: 1.0 GHz, upper limit: 1.5 GHz)


## Running the cva6 Unmatched Board in GEM5
NOTE: The source code for the board in this directory is outdated.
The up to date source code for the board can be found in
*darchr/gem5/REU2022/riscv-validation* on github. To run this
board in gem5, do the following:

1. Compile the gem5 RISCV binary.
    ```sh
    scons build/RISCV/gem5.opt -j<threads>
    ```

2. Run the board's hello world SE mode simulation script.
    ```sh
    ./build/RISCV/gem5.opt configs/example/gem5_library/cva6-run.py riscv-hello
    ```
    This should run a successful simulation and print "Hello world!".
    You can also run a custom RISCV binary by passing in the path
    to the binary via the command line. Here is an example:
    ```sh
    ./build/RISCV/gem5.opt configs/example/gem5_library/cva6-run.py microbench/CCa.RISCV
    ```
    You can add one optional argument to the binary. Here is an example:
    ```sh
    ./build/RISCV/gem5.opt configs/example/gem5_library/cva6-run.py microbenchmarks/control_complex.RISCV --argv=10
    ```
