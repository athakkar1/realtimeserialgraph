# realtimeserialgraph
A python script for plotting a real-time graph of values coming in from a serial port. Encountered issues with data buffering since values were coming in faster than pyplot could plot, so I used a workaround to ignore data points until pyplot was ready to plot again. Data being sent over the serial port was from an STM32 sampling analog signals from both a potentiometer and waveform generator. This included using their HAL to initalize and configure the built in ADC and UART interfaces that are on my development board.
https://github.com/athakkar1/realtimeserialgraph/assets/96598825/69a0d327-74fb-4028-a613-013a0d5babca
Potentiometer Readings While Adjusting Resistance
