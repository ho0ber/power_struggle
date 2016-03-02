# Power Struggle
A Rust (Experimental) Oxide 2 mod to provide victory conditions to vanilla-like gameplay

## The Problem
Rust's wipe cycle is a very good thing. Nobody wants to join a server where players have been hoarding loot for months, and who have nothing better to do with their 500 rockets than to blow your shit-shack off the face of the island.

However, this cycle causes a noticeable ebb and flow of interest and investment depending on how soon the map will be wiped. At the beginning of the cycle, right after a fresh wipe, the world is ripe for the plucking, and there are no super-bases to avoid. At the end of the cycle, players let their bases decay and care not if their compound is raided.

This leads to an anticlimactic close to the month, rather than a triumphant race to the finish. The blasé of a server's community in the final days before a wipe can even drive players away from the game for good.

## Our Solution
Our goal is to have interest and investment strong at the beginning of the wipe cycle, and even stronger as the end approaches. To facilitate this, we're adding victory conditions to each wipe cycle.

How do you "win" Rust? Hoard the most loot, of course! Power Struggle will flag a single unused item (Batteries? Blood bags?) as the victory currency on the server, and the player (or team) with the most of that currency at the end of the cycle will "win" that round, and forever be listed in the hall of fame.

In addition to a hall of fame showing prior cycle winners, there will be a live scoreboard showing the leading players/teams in the current cycle. This will paint targets on heads, destroy neighborly friendships, and dramatically increase the stakes at the end of the cycle.

## Design Specifics
* Ownership of victory currency in chests/boxes will be determined by the person who placed the container.
* The clans plugin will be used to allow groups to pool their currency on the scoreboard.
* Drop rates of the victory currency will be modified to show up in barrels, crates, and (especially) airdrops.
* The scoreboard will be available in-game and on a website (easy to know if you were raided without logging in).
* Victory currency stack size will be configurable, in order to increase or decrease the burden of storing these items.
* Victory currency may be configured to be awarded upon killing a member of a rival clan.
