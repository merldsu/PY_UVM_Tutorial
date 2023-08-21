// Copyright 2023 MERL-DSU

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//    http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


module FA(
             input logic unsigned in1,
             input logic unsigned in2,
             input logic unsigned cin,
             output logic unsigned sums,
             output logic unsigned cout);
             

  
  assign sums = in1 ^ in2 ^ cin;
  
  assign cout = (in1 & in2)|(in2 & cin)|(in1 & cin);
  // this might be change in future
  initial begin
   $dumpfile("dump.vcd");
   $dumpvars(1,FA);
  end
  
endmodule
