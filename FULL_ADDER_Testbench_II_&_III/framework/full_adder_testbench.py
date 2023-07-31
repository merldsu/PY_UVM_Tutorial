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
	


@cocotb.test()

async def fa_random_test(dut):
	
	# Create 3 arrays for input
	input_A = []
	input_B = []
	input_CIN = []
	
	# Create 2 arrays for output
	
	output_SUM = []
	output_COUT = []
	
	for i in range(20):
		
		#define three inputs which are random
		
		A = random.randint(0,1) # range
		#input_A.append(A)
		
		B = random.randint(0,1)
		#input_B.append(B)
		
		Carry_in = random.randint(0,1)
		#input_CIN.append(Carry_in)
		
		#Assign values into dut
		
		dut.in1.value = A
		input_A.append(dut.in1.value)
		dut.in2.value = B
		input_B.append(dut.in2.value)
		dut.cin.value = Carry_in
		input_CIN.append(dut.cin.value)
		
		# Timer to wait to perform DUT Logic
		
		await Timer(2,units='ns')
		
		
		cout = dut.cout.value
		output_COUT.append(cout)
		
		sums = dut.sums.value
		output_SUM.append(sums)
		
		# display the input and output of DUT
		
	#print("Input A =",input_A)
	#print("Input B =",input_B)
	#print("Input Cin =",input_CIN)
	
	#print("sum ",output_SUM)
	#print("cout ",output_COUT)
	#print(len(input_A))
	#print(len(input_B))
	#print(len(input_CIN))
	#print(len(output_SUM))
	#print(len(output_COUT))
	
	
	df=pd.DataFrame({"Input_A":input_A,"Input_B":input_B,"Input_CIN":input_CIN,"SUM":output_SUM,"COUT":output_COUT})
	df.to_csv("FA.csv",index=False)

			
		
