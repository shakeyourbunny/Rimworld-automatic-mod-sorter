Changes in the fork (shakeyourbunny)
====================================

 - moved mod database file to extra repository (see https://github.com/shakeyourbunny/Rimworld-automatic-mod-sorter-database)
 - re-added two batch files for easy starting which do not exist anymore (see below).

 - minor cleanup  files (dont commit python cache files...)
 - some whitespace cleanup
 - set version to 0.43.1 (instead of 0.43)

Re-added following batch files (you still need a working python installation in your path, though):
- rwmodsort.bat -> start the mod sorter
- rwmodsort_template_update.bat -> start the database updater and add missing mods (description see bottom
  of the page).

I am aware that the original author is currently writing (March 2019) a major rewrite to address the reason for forking
(database update). Currently I am undecided to upstream my database (alongside the list of contributors) once the rewrite
is working good enough or rewrite the project myself (like linux compatibility etc).

If I will do my own rewrite, some things to update / change:
 - linux compatibilty
 - online update / upload support
 - more meaningful description
 - keep mod weights in line with the original script.
 - sync down additions to the original scripts' database. 

NB: after some essential code cleanup (too many too list), I decided to grow the fork in a full fledged 
    mod sorter with all the (command-line) bells and whistles; expect major changes from now on.

Have fun using it!

If you wish to contact me, please open an issue, send me an email or contact me on Steam.

-- shakeyourbunny.

--- Original notes here ---

HOW-TO-USE
========

(No Linux support. yet...)

unzip a file.

you can see the .bat file named 'Launch mod sorter.bat'

before opening it, you should run rimworld, and go to the mod tab, and activate mod that you want to use.

restart rimworld, and close it(this will add the mod list to the rimworld config file)

and start 'Launch mod sorter.bat'

in the terminal, a window will pop up asking for rimworldwin64.exe

(you can found it in steam/steamapps/common/rimworld folder, or just open game directory in steam)

and that's it!

the mod will be automatically sorted and open rimworld.

if the mod isn't on DB, the terminal will show you a list that which mods are on load list, but not loaded. turn on rimworld and finish your work.


GREEN  = workshop mod

YELLOW = Local mod

~BLUE = local mod saved by mod manager~ deleted feature. it will add if in need.


if you're interested in adding mod to DB. please read below and contact to me!


Screenshots
========

![061](https://user-images.githubusercontent.com/46273764/51812240-099a9100-22f4-11e9-8d42-b66b18232ab3.jpg)
![063](https://user-images.githubusercontent.com/46273764/51812242-099a9100-22f4-11e9-84b0-21ea9e863b6b.jpg)
![064](https://user-images.githubusercontent.com/46273764/51812244-099a9100-22f4-11e9-8fae-d96c50badf1d.jpg)
![065](https://user-images.githubusercontent.com/46273764/51812245-099a9100-22f4-11e9-84fe-1c0bf5eea391.jpg)
![066](https://user-images.githubusercontent.com/46273764/51812247-0a332780-22f4-11e9-9b70-11f7569b3abb.jpg)
![062](https://user-images.githubusercontent.com/46273764/51812251-0c958180-22f4-11e9-9f80-e896e3de62d0.jpg)


HOW-TO use DB updater
=============

I included DB updating tool if the user wants to contribute to DB.

you can found folder named "template updater"

run  "Launch template_updater.bat" (don't run tetmplate_updater.exe)

after you run it, terminal will ask you to type Y or N (if screen freezed, press enter few times.)

type Y to start work, type N to exit program.


a window will pop up asking you to locate "Rimworld64Win.exe"

find rimworld64win.exe and it will download DB from github, and show your all mods from workshop and local.

and remove overlapping mods from list.


then you'll see, you need to input number one of 1 to 20.

if you type P, you can pass that mod if you can't sure. press X to stop the program and save.


*****

important : this number support Prime number. you can use it!

0 to 1. Mod manager, MOD-E, BetterLoading and other mods that should be loaded before Core.
1. Core

2.Hugslib only

2.xx. RuntimeGC

3~6. other mod's Core, framework, library mod
(example: giddy up! core, alien race framework 2.0, advanced animal framework)

7~8 hugslib mod
mod that need hugslib.


9~12 Large-scale mod and sub mod of that mod

example : Rimsennal, EPOE
explain : Hospitality is a large-scale mod, but it hugslib-require mod. so it will go to 7~8.

Race add mod : go to 9~12 if it have any dependency relation. go to 13 if it doesn't have any.

13. Hair/trait/story teller/faction add

14~15. item/terrain/object/simple mod like add animals.
15. simple mod or mods that don't modify mod many.

15~16. mod that affact AI behavior
example: haul to stack, while you're up

17. interface / user convenience

18~ always load last
*****

I'll show you an example.

if you're trying to add mod "Megafuana", what you should do?
first. always read steam mod dscription page unless you know very well about the mod.
(if the mod is very simple, or don't modify game too much, you can just guess it. like 'simple stockpile presets', or 'simple bulk cooking'.)

https://steamcommunity.com/sharedfiles/filedetails/?id=1055485938&searchtext=megafauna

the description says:

>Megafauna will automatically detect and patch both A Dog Said... by >SpoonShortage (so you can cure old wounds of your animals and >install bionic parts on them) and Giddy-up! by Roolo (which means >that you can ride your animals!), so make sure to make it load after >those mods.


nothing refer to mod conflict, and no hugslib require. and always put mod under 'A dog said...' and 'Giddy up! core'
'A dog said...' is the Core mod in other mod. so it will be in 3 to 6.
and also giddy-up! core is the Core mod. so it will be in 3 to 6.
so finally, this mod add lots of animals, but it doesn't modify game too much. so 'Megafuana' will get 14 to 15.

if you have trobule when you add sub mod. you can use PRIME NUMBER to add it.
example:
Rimsenal is a huge mod, so it will be in 9 to 12. (it is core mod so It should be set close to 9.)
"rimsenal : federation", "rimsenal : feral" is a sub-mod of Rimsenal Core.
so it will go to 9.1, 9.2, 9.xx or 10.(It is actually in 10.)

if you adding mod that requires hugslib. read this
let's say A is a hugslib-require mod that doesn't need other mods. B is also a hugslib-require mod but it needs other mods.(sub-mod).
and X is the core mod that B needs it.
currently X is assigned to '10.0'

first, choosing number for A. ignore other considerations and put it to 8. unless it needs to go to specific order.
second, B is also hugslib so it should go to 7 or 8. but it needs X and it is on 10.
so you should assign B to 10.xx or 11to.

after you finished, or saved, you can test your order by using 'mod sorter by local.bat'







