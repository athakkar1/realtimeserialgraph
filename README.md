# realtimeserialgraph
A python script for plotting a real-time graph of values coming in from a serial port. Encountered issues with data buffering since values were coming in faster than pyplot could plot, so I used a workaround to ignore data points until pyplot was ready to plot again. Data being sent over the serial port was from an STM32 sampling analog signals from both a potentiometer and waveform generator. This included using their HAL to initalize and configure the built in ADC and UART interfaces that are on my development board.
![2023-12-23 12-39-01](https://github.com/athakkar1/realtimeserialgraph/assets/96598825/abebe75c-c8d0-4478-b0bc-8a7e9cdd6edd)
Potentiometer Readings While Adjusting Resistance
