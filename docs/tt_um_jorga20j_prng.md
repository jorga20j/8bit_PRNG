
# Entity: tt_um_jorga20j_prng 
- **File**: tt_um_jorga20j_prng.v

## Diagram
![Diagram](tt_um_jorga20j_prng.svg "Diagram")
## Ports

| Port name | Direction | Type       | Description                                               |
| --------- | --------- | ---------- | --------------------------------------------------------- |
| ui_in     | input     | wire [7:0] | Dedicated inputs                                          |
| uo_out    | output    | wire [7:0] | Dedicated outputs                                         |
| uio_in    | input     | wire [7:0] | IOs: Input path                                           |
| uio_out   | output    | wire [7:0] | IOs: Output path                                          |
| uio_oe    | output    | wire [7:0] | IOs: Enable path (active high: 0=input, 1=output)         |
| ena       | input     | wire       | always 1 when the design is powered, so you can ignore it |
| clk       | input     | wire       | clock                                                     |
| rst_n     | input     | wire       | reset_n - low to reset                                    |

## Signals

| Name       | Type      | Description     |
| ---------- | --------- | --------------- |
| state_0    | reg [7:0] | xorshift states |
| state_1    | reg [7:0] | xorshift states |
| state_2    | reg [7:0] | xorshift states |
| state_3    | reg [7:0] | xorshift states |
| random_out | reg [7:0] | output value    |

## Processes
- unnamed: ( @(posedge clk ) )
  - **Type:** always
