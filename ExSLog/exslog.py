

class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'



class Exslog:
    '''
        Provides ability to easily display and/or save debug messages from your program.
	It is up to developer to decide the severity of displayed messages.

	More functionalities incoming ( I have to think about them, what would be useful and how to easily implement it. Any ideas are welcome. ).

        To Do's:
            # 1. check if self.noise is numeric

            # 2. create directories for logs
            # 2.1 check if dir exists, then don't create such

            # 3. if self.output true then create log file at given destination.
    '''

    #LOG_DIR = "pwd / logs"

    def __init__(self, level:str, noise:int, output=False):
        self.level = level
        self.noise = int(noise)
        self.output = output
        self.format = ""


        match self.level:
            case "success":
                self.format = f"{colors.fg.green}{colors.bold}[ + ]{colors.reset}"

            case "failure":
                self.format = f"{colors.fg.red}{colors.bold}[ - ]{colors.reset}"

            case "error":
                self.format = f"{colors.bg.red}{colors.bold}[ ! ]{colors.reset}"

            case "info":
                self.format = f"{colors.fg.blue}{colors.bold}[ * ]{colors.reset}"

            case "warn":
                self.format = f"{colors.fg.yellow}{colors.bold}[ ~ ]{colors.reset}"

            case _:
                print(f"{colors.bg.red}[ ! ]{colors.reset} Exslog: Severity level at assigning object not recognized")
                exit()


    def _log_output(self) -> None:
        pass
        # append to files


    def say(self, m_noise:int, m_text:str, m_new_line=False) -> None:
        # TO DO: check if m_noise is int

        message = f'{self.format} {m_text}'

        if m_noise <= self.noise:
            if m_new_line is True:
                print(f"\n{message}")
            else:
                print(f"{message}")

        # append to file if self.output is True



# if __name__ == "__main__":
#     user_verbose = 2

#     success = Exslog("success", user_verbose)
#     failure = Exslog("failure", user_verbose)
#     error = Exslog("error", user_verbose)
#     info = Exslog("info", user_verbose)
#     warn = Exslog("warn", user_verbose)

#     success.say(1, "pos")
#     failure.say(2, "neg")
#     error.say(3, "err")
#     info.say(2, "inf")
#     warn.say(1, "wrn\n")

#     failure.say(1, "neg")
#     success.say(2, "pos")
#     error.say(3, "err")
#     info.say(3, "inf")
#     warn.say(2, "wrn")
