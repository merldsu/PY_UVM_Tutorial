# Copyright 2023 MERL-DSU

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cocotb
from cocotb.triggers import Timer
import random
import pandas as pd


@cocotb.test()


async def fa_manual_test(dut):

	#define three different input values
	A = 1
	B = 1
	Carry_in = 0
	
	# Assign values to DUT
	dut.in1.value = A 
	dut.in2.value = B
	dut.cin.value = Carry_in
	
	# Timer to wait to perform dut action
	await Timer(2,units='ns')
	
	cout = dut.cout.value
	sums = dut.sums.value
	
	#display the input
	print("Inut 1 =",A)
	print("Inut 2=",B)
	print("Inut 3=",Carry_in)
	# display the output
	print("FA SUM OUTPUT =",sums)
	print("FA COUT OUTPUT =",cout)		
