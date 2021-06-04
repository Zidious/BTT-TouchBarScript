# BTT-TouchBarScript
CryptoCurrency touchbar button to get price, marketcap and volume of an asset. 

![](ASSETS/NewExample.gif)

# Steps: Adding a script - 

###### Step 1

Install BTT: https://bettertouchtool.net/releases/. You get a 45 day trial, I would recommend buying the license as I did, 100% worth buying the license and to support the dev!

Download python 3.7: https://www.python.org/.

You will need to also install the CoinGeckoAPI dependency via pip, the command is:  ```pip3 install pycoingecko```.

###### Step 2

Open up BTT and top left make sure "Touch Bar" is selected. There is where you'll be able to add individual buttons and/or button groups.

###### Step 3

Select "+" under Groups & Top Level Triggers.

###### Step 4

Under "Touch Bar Trigger Configuration" select the "Touch Bar Widgets" drop down and select "Shell Script / Task Widget".

###### Step 5

Under "Widget Identifier" remove any text within this box. 

Under "Execute script every" select to the duration you wish i.e. 10 seconds

At the bottom, under "script" enter the the name of the button i.e. AVA like so: ```echo AVA``` - This is the test that will appear on the button itself.

###### Step 6

Now, we need to assign an Action to this script, this will be the Python script. 

Select the "+" and enter in "execute Shell Script / Task".

###### Step 7

Now, we need to enter in the path of the script using Python3. 

Download a script, for this example we will use ```Travala.py```.

The script is the python3 path followed by the path of your saved script. Like so: 

```/usr/local/bin/python3/ Users/gabe/Scripts/BTT-TouchBarScript/Travala.py``` - NOTE: there is a space between the end of `python3/ Users`.

###### Step 8

After inputting the script select "Run Script Now" and you should be prompted with the following output (example below): 

`$3.0 - MC: $156,455,696 - VOL: $7,070,268`

And thats it... You're done! 

# Adding Icons To Button (As shown in the GIF) - 

First of all you'll need to source your desired icon, many projects have a graphic bundle, you can use this as your icon for each button.

###### Step 1

Select your desired script, underneath "Run Shell Script and Show Return Value".

###### Step 2

Click onto "Advanced Configuration" and then onto "Appearance & Settings" 

###### Step 3

On the right hand side of the window you will see "Icon" and next to this a blank box with a dot in the middle. Simply click in the middle to be prompted to the next window 

###### Step 4

Once the pop up window has appeared, select "From Disk' and locate your icon from your directory and click "Open"

###### Step 5

Now, you will see you have an icon on your button. 

If you want to make it more aesthetically pleasing, you can make the background of the button the same colour as your icon. To do this select "Background Color" and at the bottom left of the pop-up window you will see a colour picker, click onto this and hover over your icon and click to save the colour. 

That is it! Your button (background) will be the same colour as your icon.

