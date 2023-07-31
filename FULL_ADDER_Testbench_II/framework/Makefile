TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

SIM ?= verilator

EXTRA_ARGS += --trace --trace-structs
WARNING_ARGS += -Wno-TIMESCALEMOD -Wno-WIDTH -Wno-UNOPT

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

ifeq ($(TOPLEVEL_LANG),verilog)
    VERILOG_SOURCES = $(PWD)/../hdl/full_adder.sv
else ifeq ($(TOPLEVEL_LANG),vhdl)
    VHDL_SOURCES = $(PWD)/../hdl/full_adder.vhdl
else
    $(error A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG))
endif

TOPLEVEL := FA # Verilog or SystemVerilog TOP file module name
MODULE   := full_adder_testbench # Python file name

include $(shell cocotb-config --makefiles)/Makefile.sim
