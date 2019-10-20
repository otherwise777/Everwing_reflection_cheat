## Everwing hack

### The project

This is my hobby project to see if i could hack the facebook everwing game. This project has shown many results but is not finished yet, be aware that when you want to use this it's not user friendly yet, but it works.
Right now you can do several things with the code:
* Gain infinite amount of coins
* Retrieve all characters
* Boost all your characters without watching adds
* Retrieve any type of egg

This hack does not make use of code injection like most hacks of everwing do (this is fixed) but instead it does a "reflection attack" which means it simulates real player behaviour. Although i did find some exploits like getting rewards for boss raids that didn't start yet to speed up process and getting specific characters from the pool.

I enjoyed reserver engineering and hacking everwing as a hobby, if you're curious about my journey and what things i faced, you can read my [journey](journey.md)

## Result

This is one of the things i achieved with this hack

## Requirements
* python 2.7 installed (python
* Have a bit of understanding of how python works
* know how to install dependancies in python, aka libraries

## How to
1. Open the game in your browser and hit f12, this will open the developers window
2. go to the table network on the top of the developers window
3. go back to the game and perform an "action" this can be switching characters
4. go back to the network tab in the developers window, and search for a message with "run_action", you can also filter the messages to make it easier
5. select one of messages which has the POST request
6. in the section "request headers" you will see a msg "x-wintermute-session:" copy the part which is behind of it and paste it in the code
7. now you need to fill ion the userid, this is a bit more complicated

*this part needs to be made easier with some ui or function to run to retrieve data, especially retrieving the userid there's no apparant way of retrieving it outside of code*



# functions explained
There are a couple of functions you can run from the commandline which you can use:
* *getSessionID* retrieves session id with cookie
* *buyNewCharacters* buys new characters based on a specific timestamp
* *boostAllCharacters* boosts all your characters
* *claimAndSetAllRewards(lvlstart,lvlend)* Claims rewards for bosses from level *lvlstart* to level *lvlend* keep in mind you cannot claim the reward twice for the same boss level, this resets each week.




## help needed
As you can see, this project is not complete yet, any help is appreciated.
Soe stuff still on the roadmap:
* Make initialization function to retrieve all user variables such that you don't have to fill it in
* make it easier to retrieve sessions
* Have some kind of user interface, for example flask, to make it easier to use it for the user
* compile the code in an executable?

Any suggestions are welcome as well

## notes for future help
So i got most of it automated, but there are a few flaws still, i'm able to get a session with a cookie for example but i failed in retreiving the userid with a call, and to get a session you need to have the userid. The game seems to call the facebook api to get it, but i don't think i can easily script that since the logic is completely different.
