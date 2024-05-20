# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

import prng_model

#Parameters
seed_0 = 42
seed_1 = 250
Latency_cycles = 2

#Functions
def compare(A, B):
    for x in range(0, len(A)):
        assert A[x] == B[x]


#Test
@cocotb.test()
async def test_enable_prng(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    #PRNG model
    prng = prng_model.Xorshift8bit(seed_0)

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 0
    dut.ui_in.value = seed_0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Enable
    dut._log.info("Test project behavior")
    dut.rst_n.value = 1
    dut.ena.value = 1
    await ClockCycles(dut.clk, Latency_cycles)

    # Read Output
    expected_output = []
    output = []
    for i in range(0, 10):  
        expected_output.append(prng.next())
        output.append(int(dut.uo_out.value))
        await ClockCycles(dut.clk, 1)

    # Compare results
    compare(output, expected_output)


@cocotb.test()
async def test_disable_prng(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    #PRNG model
    prng = prng_model.Xorshift8bit(seed_0)

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 0
    dut.ui_in.value = seed_0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Enable
    dut._log.info("Test project behavior")
    dut.rst_n.value = 1
    dut.ena.value = 0
    await ClockCycles(dut.clk, Latency_cycles)

    # Read Output
    expected_output = []
    output = []
    for i in range(0, 10):  
        expected_output.append(0)
        output.append(int(dut.uo_out.value))
        await ClockCycles(dut.clk, 1)

    # Compare results
    compare(output, expected_output)


@cocotb.test()
async def test_reseed_prng(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    #PRNG model
    prng = prng_model.Xorshift8bit(seed_0)

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 0
    dut.ui_in.value = seed_0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Enable
    dut._log.info("Test project behavior")
    dut.rst_n.value = 1
    dut.ena.value = 1
    await ClockCycles(dut.clk, Latency_cycles)

    # Read Output
    expected_output = []
    output = []
    for i in range(0, 10):  
        expected_output.append(prng.next())
        output.append(int(dut.uo_out.value))
        await ClockCycles(dut.clk, 1)

    # Compare results
    compare(output, expected_output)


    #PRNG model
    prng = prng_model.Xorshift8bit(seed_1)

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 0
    dut.ui_in.value = seed_1
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Enable
    dut._log.info("Test project behavior")
    dut.rst_n.value = 1
    dut.ena.value = 1
    await ClockCycles(dut.clk, Latency_cycles)

    # Read Output
    expected_output = []
    output = []
    for i in range(0, 10):  
        expected_output.append(prng.next())
        output.append(int(dut.uo_out.value))
        await ClockCycles(dut.clk, 1)
    
    # Compare results
    compare(output, expected_output)
