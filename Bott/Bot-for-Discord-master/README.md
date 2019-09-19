# Discord   
This is a simple implementation of a discord bot using the discord.py rewrite library.      
To run the bot you would need the following:

How to get Bot Token: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord       
Reddit API info: https://stackoverflow.com/a/42304034  

Bot commands prefix ".":
CopyPasta = Bot responds to keywords by posting a message    
    -addpasta:  Add a response to users keyword    
    -eatpasta:  Removes one of the copypastas   
    -pastabits: Changes when the trigger messages gets deleted     
              
Dictionary = Parsing through urban dictionary to obtain info 
    -define:    UrbanDict definiton of a users word  
    -wotd:      Word of the day on UrbanDictionary  
    
DiscordRateGirl = Generates 2 PRNG values that stay consistent depending on day   
    -rategirl:  Rates @User by 2 values, Hot and Crazy    
         
Miscellaneous = Fun commands   
    -avm:       Print avatar of pinged User   
    -badbot:    Same as goodbot     
    -cm:        Turns cm (height) to ft + inch (metric to imperial) by approximation 
    -dice:      Rolls 2 dice ( returns 2 values between 1-6)   
    -erase:     Erase N messages (admin only)   
    -ft:        Turns height ft.inch (Eg: 5.11) to cm (imperial to metric)      
    -gimg:      Searcher for a random image from google         
    -goodbot:   Filler command. Bot sends a message on call.      
    -hide:      Removes the messages of a user from a channel      
    -kg:        Turn kg into lb (metric to imperial)        
    -lb:        Turn lb into kg (imperial to metric)   
         
Reactions = Users can have the bot add a reaction to keywords that users choose  
    -addreact:  Add a reaction to a keyword/keywords   
    -rmreact:   Removes a reaction to a keyword/keywords   
        
Reddit = Parsing reddit for you (Has NSFW filter on.)   
    -rbon:      Best Of N from a subreddit   
    -rrand:     Random search result from a subreddit   
    -rrsearch:  Random post from search results      
    -rsearch:   Top post from reddit search      
    -rtop:      Top post from hot section of subreddit   

Youtube = Parsing Youtube         
    -randyt:    Random result of a topic from youtube      
    -yt:        First result from youtube of a topic      
     
Bugs found:     
-Encoding problems in logging the messages.          
-Certain subreddits cause unexpected behaviour in the random function.        
 
