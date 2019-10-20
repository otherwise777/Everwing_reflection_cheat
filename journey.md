
I enjoyed playing everwing and after i got bored with it i figured i should easily be able to get some powerup by digging into the game mechanics to get an advance. This is a story about how i did the discoveries i did and how i exploited them. I have nothing against the makers of Everwing, i simply enjoy finding the exploits and reverse engineering the game itself. In the end these items should also be helpfull if you ever want to protect your game or any other system against people that might want to exploit it. If you have any improvements or feedback, feel free to share them or make a PR.

Let's first go through some basics about how games work. In a game you do certain actions, based on that you get certain things, like money. For a single player game that doesn't run on the internet you can easily modify it because all the data and code is stored on your machine. So if you have an asset money, you should be able to modify that money asset. Everwing is an online game so data exists on the server, and when you start up your game it sends you this data to initialize your game. But then it's up to you, you can modify this data and send it back, telling the game, i now have this much money, this is a bit tricky in everwing because the server on the other end knows how you can play the game, so if you tell the server that you just received 2m coins, the server might give an error telling you that this is impossible and deny your request. but if you say you just received 100 coins by playing an arcade game the server might agree since it seems feasible.

Now how did i find out these hacks,
The first thing i did was google, i couldn't be the only one doing this right? Especially since Everwing was already out there for a while, and it's made with Javascript which is easy to exploit. I found dozens methods of changing the variables of money stored on your client. When i attempted these i got the message "hack detected" which meant this method was known to the devs and was patched. Aside from that i found some shady websites asking for your details to give money, this didn't look that legit. And that was pretty much all i could find about it, from at least 6 months ago. So one thing i thought, did they  really patch it that well that nobody bothered to create new hacks? Well i was about to figure it out.

First attempt
I wanted to bypass the old hack detection system they made, this pop up saying that they detected a hack was simply some piece of code running on my machine, so i dug through the sources with some simple keywords "hack" and quickly found the codeblock responsible for it. I first tried modifying the DOM where this runtime code was stored, this seemed not so easy since it relies on variables injected into it on startup so the next attempt was to make sure that when your browser loads the file to instead load your own customized file. Chrome has something for it called "overrides" It will copy the source file and allows you to make changes and the next time it loads the web page it will take your piece of code instead of theirs.

So now we have the ability to completely change the client side of the program, in such a way that the serverside still accepts it. Now the hard part begins, trying to understsand how the code works and what happens where. Some functions are easy to understand because there are strings and endpoints in the code that hint to the meaning of the function like "ClaimDailyReward", but most of the code is obfuscated to prevent people like me understanding the code. This part involved lots of time digging into the code, adding breakpoints and prints to see which function is being called (i found a lot of dead code with this method). A full day later i figured out how the code worked, but I didn't really find any exploits. I could modify the code, but not in such a way that old exploits were working again. a possible dead end, so i tried something else.

The network layer, i talked about the 2 sides of the game, client side and server side, well there's a layer in the middle which basically connects the two, it's the way the client and the server talk to each other. Instead of trying to change the client side you can also inspect how the client and server are talking to each other and duplicate or change it. There are many tools to do this but for ease of use i use chromes network inspection. Thise method showed success quite fast, i inspected what happened when asking for a daily reward, and then send the daily rewards for both coins/gems/eggs and i received them all. Unfortunately i couldn't trigger them again for 24 hours since this was protected on the server side, this was a small exploit but it's still one, we're on a good track!

Next up is the arcade game, i found out it communicates twice when doing an arcade game, once to initiate that i started the game, and once to initiate that i finished the game. First attempt was to just send multiple "game finish" requests, this didn't work, but after i send the start request i could send a finish request and get the rewards. Now here comes a nice exploit, in the reward it lets the client decide what the rewards are as follows:

```
"params":{
   "score":<your score>,
   "xpEarned":<xp earned>,
   "coinsEarned":<coins earned>,
   "energyEarned":<energy gained>,
   "eggTypeFound":<egg type>,
   "sidekick1Key":<dragon left>,
   "sidekick2Key":<dragon right,
   "qa":False
}
```

This is where the fun begins. I first tried giving myself 5000 coins and xp, but this didn't work, i found out it actually tracks the time between the "game start" and "game finish" requests were send to decide how many coins/xp/score you can claim. If you do a game of 2 seconds the maximum score you can get is 120 and the maximum coins is 120 (except when using lily then you can get 240 coins max, independent of her level). Next up i wrote a little python script to automate this and send the start and finish request every 2 seconds to get lots of coins, this basically still uses the mechanics of the game so i wouldn't call this an exploit. Gaining coins was ok but it's not what makes you say: DAYUM! So the search continued for more exploits

The game bug
So prior to this point i used my main account for the exploits, i cannot do this anymore since i corrupted my game save client side and there's no  way to reset your game. I figured i can change the eggtype found, then after an arcade game i would have this egg, this worked! So i got myself a gold egg. Now i wanted a legendary egg, because why not right? Well! THERE IS NO LEGENDARY EGG, so i actually managed to get a legendary egg, but it didn't exist! so my game crashed. The serverside  tells the client side that i have a legendary egg in one of my slots, but since the client side does not recognize this egg type it crashes. There was also no way to hatch this egg so i decided to abandon my account and start a new one for my exploits.

I digged some more in the code to find the egg types that the game recognizes, i found out the ancient egg was the highest available egg that you could get from an arcade so got myself some of those, but the time it  takes to hatch is 24 hours, and there was no way around that so this was only a minor exploit.

The boss raids
I figured i found most of the game mechanics of the arcade game and focused on the boss raids for now. The boss raids were a bit more complex to exploit since it involves more requests with more variables. First off the boss raids also have a start and finish raid, additionally they als have a "clan login" and "boss update" call which checks you into the boss raid and gets info on the boss, this getting an update from the boss is essential since for these requests you have to give an incremental number to your requests. This meant i couldn't randomly go throwing requests around but i actually had to keep track of them in some manner. So i found out i could easily "simulate" doing 2m damage to the boss so i did. The bosses died quite easily and i found an interesting call to the server setting the reward for a boss:

"params":{
   "nodeID":<Boss level>,
   "treasureLevel":<treasure level>,
   "damageNormalized":<no idea what this is>,
   "hadBestRun":True,
   "wasFirstToMaxReward":True
},

So we can see a few interesting things here, to start with "hadBestRun" and "wasFirstToMaxReward" setting these to True increases your chest rewards by 1 each. Treasure level is an integer from 1 to 20, where 20 is the highest level chest [https://everwing.fandom.com/wiki/Boss_Raids](wiki) So i of course immediately set my treasure level to 20 to get most out of the rewards, COOL! easy legendary and mythic dragons :D, this is another exploit. The next day was spend on automating this process to automatically defeat bosses and set and claim rewards for each run, this took some more time than expected because i found out that the "clan login" command and "update boss" command return the same types of data but the contents might differ, like the boss hp you get on "clan login" might be outdated.

At this time i already tried claiming chests from bosses i didn't defeat yet, but unfortunately that didn't work. i did successfully set the rewards for bosses i didn't start or defeat yet, this came in handy in the automating process. So at this time i got a lot of loot from all the boss chests and decided to get some more characters and just play around with some different requests. Among others i tried setting and claiming the rewards for a boss that didn't exist, boss lvl 23, and to my surprise, it worked! Now i found myself opening 500 level 20 chests from boss raids, maxing the amount of coins and getting the maximum character count for both Lucia and Lyra (both drops from the chests) and having more legendary dragons than i could count. This was the biggest exploit i found.

Moving on, i now had the maximum amount of money and a shitload of dragons, what now? I figured i could buy a ton of characters now so i did. Here i found another exploit by accident. i kept sending the server the same request and i kept getting the same characters, i found this weird because the other functions didn't work the same. After some trying out changing some variables in the function i found out that the timestamp i send acted as some kind of variable for the character(s) that were selected as a reward:

```
"params":{
  "gachaID":"starTokenCommonGacha",
  "priceID":"regular"
},
"simulateTime":timestamp
```

I tried out this same mechanism on the chest selection of the boss raids, but that didn't seem to work.

The end
I didn't achieve everything that i wanted but got pretty much out of the exploits that i found. I have a method to get an infinite amount of cash and with that unlock all characters. Unfortunately i didn't find a method to get an infinite amount of gems, they seemed to have closed off that part quite well. I hope you enjoyed reading this as much as i enjoyed solving this "puzzle"


