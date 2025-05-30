import os

tools = {
    "1": ("Broadcast Tool", "tools/broadcast.py"),
    "2": ("Auto Responder", "tools/autoresponder.py"),
    "3": ("Auto Forwarder", "tools/forwarder.py"),
    "4": ("Group Scraper & Inviter", "tools/scraper_inviter.py"),
    "5": ("Media Downloader", "tools/mediadownloader.py"),
    "6": ("OTP Saver", "tools/otpsaver.py"),
    "7": ("Chat Logger", "tools/logger.py"),
    "8": ("Game Bot", "tools/gamebot.py"),
    "9": ("Stats Dashboard", "tools/stats_dashboard.py"),
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear()
    print("""\033[1;36m
 ████████╗███████╗██╗     ███████╗ ██████╗  ██████╗ ██╗     ███████╗
 ╚══██╔══╝██╔════╝██║     ██╔════╝██╔═══██╗██╔════╝ ██║     ██╔════╝
    ██║   █████╗  ██║     █████╗  ██║   ██║██║  ███╗██║     █████╗  
    ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██║   ██║██║     ██╔══╝  
    ██║   ███████╗███████╗███████╗╚██████╔╝╚██████╔╝███████╗███████╗
    ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    \033[0m""")
    print("🔧 Telegram Tools Launcher")
    for key, (name, _) in tools.items():
        print(f"{key}. {name}")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter Tool Number: ").strip()
        if choice == "0":
            break
        elif choice in tools:
            _, script_path = tools[choice]
            os.system(f"python {script_path}")
        else:
            input("❌ Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    main()
