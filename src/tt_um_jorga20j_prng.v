/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_jorga20j_prng (
    input  wire [7:0] ui_in,    //! Dedicated inputs
    output wire [7:0] uo_out,   //! Dedicated outputs
    input  wire [7:0] uio_in,   //! IOs: Input path
    output wire [7:0] uio_out,  //! IOs: Output path
    output wire [7:0] uio_oe,   //! IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      //! always 1 when the design is powered, so you can ignore it
    input  wire       clk,      //! clock
    input  wire       rst_n     //! reset_n - low to reset
);

  reg [7:0] state_0;        //! xorshift states
  reg [7:0] state_1;        //! xorshift states
  reg [7:0] state_2;        //! xorshift states
  reg [7:0] state_3;        //! xorshift states


  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = state_3;  //! random output
  assign uio_out = 0;
  assign uio_oe  = 0;

  always @(posedge clk ) begin
      if (!rst_n) begin
          state_0      = ui_in;  
          state_1      = 8'b0;   
          state_2      = 8'b0;   
          state_3      = 8'b0;   
      end else begin
        if(ena) begin
            state_1 = state_0 ^ (state_0 << 3);
            state_2 = state_1 ^ (state_1 >> 5);
            state_3 = state_2 ^ (state_2 << 4);
            state_0 = state_3;
        end else begin
            state_0      = 8'b0;  
            state_1      = 8'b0;   
            state_2      = 8'b0;   
            state_3      = 8'b0; 
        end
      end
  end

endmodule
