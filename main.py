from pystyle import Anime, Colors, Colorate, Center
from colorama import Fore
import requests
import time
import re
import os

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"} # request headers
ANSI = re.compile(r'\x1b\[[0-9;]*[mK]') # ansi regex

class utility: # utility class
    logo = r"""
 $$$$$$\  $$$$$$$$\ $$\   $$\       $$$$$$$\                                $$\                                
$$  __$$\ $$  _____|$$ |  $$ |      $$  __$$\                               $$ |                               
$$ /  \__|$$ |      \$$\ $$  |      $$ |  $$ | $$$$$$\   $$$$$$$\  $$$$$$\  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
$$ |      $$$$$\     \$$$$  /       $$$$$$$  |$$  __$$\ $$  _____|$$  __$$\ $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
$$ |      $$  __|    $$  $$<        $$  __$$< $$$$$$$$ |\$$$$$$\  $$ /  $$ |$$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$\ $$ |      $$  /\$$\       $$ |  $$ |$$   ____| \____$$\ $$ |  $$ |$$ |  \$$$  /  $$   ____|$$ |      
\$$$$$$  |$$ |      $$ /  $$ |      $$ |  $$ |\$$$$$$$\ $$$$$$$  |\$$$$$$  |$$ |   \$  /   \$$$$$$$\ $$ |      
 \______/ \__|      \__|  \__|      \__|  \__| \_______|\_______/  \______/ \__|    \_/     \_______|\__|      

                                                  by Swezy <3
                                          https://github.com/SwezyDev                                            
    """ # ascii logo

    patterns = [
        ("Discord", r'"(https://discord\.gg/\w+)"'), # discord invite
        ("Banner (Connecting)", r'"banner_connecting#original_url":"(.*?)"'), # connecting banner
        ("Banner (Detail)", r'"banner_detail#original_url":"(.*?)"'), # detail banner
        ("Local", r'"locale":"(.*?)"'), # server locale
        ("FiveM Version", r'"sv_enforceGameBuild":"(.*?)"', "v"), # fivem version
        ("License Key Token", r'"sv_licenseKeyToken":"(.*?)"'), # license token
        ("Project Description", r'"sv_projectDesc":"(.*?)"'), # project desc
        ("Project Name", r'"sv_projectName":"(.*?)"'), # project name
        ("Pure LVL", r'"sv_pureLevel":"(.*?)"'), # pure level
        ("Script Hook Allowed", r'"sv_scriptHookAllowed":"(.*?)"'), # script hook status
        ("Tags", r'"tags":"(.*?)"'), # server tags
        ("Premium", r'"premium":"(.*?)"'), # premium status
        ("Review", r'"can_review":"(.*?)"'), # review status
        ("Owner ID", r'"ownerID":(\d+)'), # owner id
        ("Private", r'"private":"(.*?)"'), # private status
        ("IP", r'"connectEndPoints":\["(.*?)"\]'), # server ip
        ("Up Votes", r'"upvotePower":(\d+)'), # upvotes
        ("Burst Votes", r'"burstPower":(\d+)'), # burst votes
        ("Owner Name", r'"ownerName":"(\w+)"'), # owner name
        ("Owner Profile", r'"ownerProfile":"(.*?)"'), # owner profile
        ("Owner Avatar", r'"ownerAvatar":"(.*?)"'), # owner avatar
        ("Last Seen", r'"lastSeen":"(.*?)"'), # last seen
    ] # regex list

class functions: # functions class
    def lookup(): # lookup function
        os.system("cls") # clear screen
        print("\n" + " " * 43 + f"{Fore.RESET}[{Fore.GREEN}#{Fore.RESET}] Enter the server invite code [{Fore.GREEN}#{Fore.RESET}]\n") # input message
        invcode = input(f" https://cfx.re/join/{Fore.GREEN}") # invite input

        print(f"\n{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] Connecting ...") # connecting message
        time.sleep(2) # wait 2 secs | just visual, you can remove it
        os.system("cls") # clear screen

        try: # try request
            r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{invcode}", headers=UA) # send request
        except: # request failed
            r = None # set none

        if not r or r.status_code != 200: # invalid request
            print(f"\n{Fore.RESET} [{Fore.RED}-{Fore.RESET}] Connection Error\n") # error message
            os.system("pause >nul") # wait for key
            functions.lookup() # retry lookup

        data = r.json() # parse json
        raw = r.text # raw response
        d = data.get("Data", {}) # get data

        direct = {
            "Join Invite": f"cfx.re/join/{data.get('EndPoint')}" if data.get("EndPoint") else None, # join invite
            "Server Name": d.get("hostname"), # hostname
            "Players": d.get("clients"), # player count
            "Max. Players": d.get("sv_maxclients"), # max players
            "Gametype": d.get("gametype"), # gamemode
            "Map": d.get("mapname"), # map name
            "Steam Verify": d.get("requestSteamTicket"), # steam verify
            "Server Type": d.get("server"), # server type
        } # direct values

        for type, val in direct.items(): # print direct values
            print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] {type}{Fore.CYAN} > {Fore.RESET}{val}") if val else print(f"{Fore.RESET} [{Fore.RED}-{Fore.RESET}] {type}{Fore.CYAN} > {Fore.RESET}Not Found") # print value
            #time.sleep(0.3) # small delay incase you want it to make it look nicer

        regex_res = {} # regex results

        for entry in utility.patterns: # loop patterns
            label, pattern, *rest = entry # unpack values
            prefix = rest[0] if rest else "" # optional prefix
            m = re.search(pattern, raw) # regex search
            val = f"{prefix}{m.group(1)}" if m else None # matched value
            regex_res[label] = val # save result
            print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] {label}{Fore.CYAN} > {Fore.RESET}{val}") if val else print(f"{Fore.RESET} [{Fore.RED}-{Fore.RESET}] {label}{Fore.CYAN} > {Fore.RESET}Not Found") # print result
            #time.sleep(0.3) # small delay incase you want it to make it look nicer

        print() # empty line
        print(Fore.RED + "-" * 120) # separator line
        print() # empty line

        players = d.get("players", []) # player list
        if players: # players found
            for p in players: # loop players
                print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] Player ID{Fore.CYAN} > {Fore.RESET}{p.get('id')}") # player id
                print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] Player Name{Fore.CYAN} > {Fore.RESET}{p.get('name')}") # player name
                print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] Player Ping{Fore.CYAN} > {Fore.RESET}{p.get('ping')} ms") # player ping
                print(f"{Fore.RESET} [{Fore.GREEN}+{Fore.WHITE}] Player Identifiers{Fore.CYAN} > {Fore.RESET}{', '.join(p.get('identifiers', []))}") # player identifiers
                print(Fore.RED + "-" * 120) # separator line
                #time.sleep(0.1) # small delay incase you want it to make it look nicer
        else: # no players
            print(f"{Fore.RESET} [{Fore.RED}-{Fore.RESET}] Players{Fore.CYAN} > {Fore.RESET}Not Found") # no players found

        owner = regex_res.get("Owner Name") or "Unknown" # owner fallback
        with open(f"Server_{owner} [Swezy].txt", "w", encoding="utf-8") as f: # open output file
            for type, val in direct.items(): # loop direct values
                if val: # check if value exists
                    f.write(f"{type} > {ANSI.sub('', str(val))}\n") # write value
            for label, value in regex_res.items(): # loop regex values
                if value: # check if value exists
                    f.write(f"{label} > {ANSI.sub('', str(value))}\n") # write value
            f.write("-" * 120 + "\n")# separator line
            for p in players: # loop players
                f.write(f"Player ID > {p.get('id')}\n") # write player id
                f.write(f"Player Name > {ANSI.sub('', str(p.get('name')))}\n") # write player name
                f.write(f"Player Ping > {p.get('ping')} ms\n") # write player ping
                f.write(f"Player Identifiers > {', '.join(p.get('identifiers', []))}\n") # write identifiers
                f.write("-" * 120 + "\n") # separator line
            f.write("Coded by Swezy <3") # signature

        os.system("pause >nul") # wait for key
        functions.lookup() # restart lookup

def main(): # main function
    os.system("cls") # clear screen on start
    os.system("title CFX Resolver ^| github^.com^/SwezyDev") # set console title
    os.system("start https://servers.fivem.net/servers") # open FiveM servers
    Anime.Fade(Center.Center(utility.logo), Colors.yellow_to_red, Colorate.Vertical, interval=0.030, enter=True) # animate logo
    os.system("cls") # clear screen after animation
    functions.lookup() # call lookup

if __name__ == "__main__": # main check
    main() # start program