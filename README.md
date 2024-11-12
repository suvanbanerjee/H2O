# H2O

## [ This Project is now archived. ]

This is a project i build for myself but i decided to share it with the world. It is a simple program that can be used to calculate the amount of water you should drink daily. and send you notifications to remind you to drink water. It is built with python and pyler library. 

## Installation
To install the program, you need to have python installed on your computer. If you don't have python installed, you can download it from [here](https://www.python.org/downloads/). 

- Clone the repository
- Open the terminal and navigate to the project directory
- run config.py file to set your details
- add main.pyw to your startup folder to run the program on startup

Note: Make sure to edit the path of json file in the main.pyw file to match the path of the son file on your computer. if you dont know just put the json file in the same directory as the main.pyw file. that is in the startup folder.

## How it works

The program uses the following formula to calculate the amount of water you should drink daily. 
```
base_intake = 0.033 * weight(KG)
```
Alternate Method (Miffin-St Jeor Equation)
```
caloric_expenditure = 10 * weight + 6.25 * height - 5 * age * activity_factor
```
dividing the caloric_expenditure by 1000 gives the amount of water you should drink daily.

Then it compares the base intake by both methods and selects the highest value.

It divides one day (16 hours ie. 24-8[sleep]) into n equal parts so you can drink water at regular intervals and completes the amount of water you should drink daily.and sends you notifications to remind you to drink water.

## FAQ

### How do i change the amount of water i should drink daily?
You dont need to as the program calculates the amount of water you should drink daily based on your weight and height. Anyway if you want to change it, in main.pyw file, change the value of `base_intake` to the amount of water you want to drink daily.

### Woudn't it be better be a mobile app?
Yes, it would be better as a mobile app but i am not a mobile developer. If you are a mobile developer, do send a PR to this repository.

## Note project is archived besause of unavalability of proper research on the topic moreover its overengineered and kind of not needed but if you want to use it plug in the function to calculate the amount of water you should drink daily in the main.pyw file and run the program.


## License

This project is not licensed. You can use it for whatever you want. 