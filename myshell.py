import os
import subprocess


def myshell_cd(directory):
   # This function changes the default directory to the chosen one.
   try:
      # changes directory
      os.chdir(directory)
   except Exception:
      # if directory spot was empty this handles it
      if directory == "":
         print(os.getcwd())
      # if the directory doesnt exist this handles it
      else:
         print("Error: directory does not exist: {}".format(directory))


def myshell_pause():
   # this function pauses the shell
   usrinp = input(os.getcwd() + "/myshell$ ")
   # tests to see if the input was just an <Enter> key
   while len(usrinp) > 0:
      # if it wasnt it runs endlessly until the input is the <Enter> key
      print ("Myshell is paused. Please hit <Enter> to continue.")
      usrinp = input(os.getcwd() + "/myshell$ ")


def myshell_echo(comment):
   # this function returns the argument entered but with excess blank spaces removed
   comment = comment.split()
   # split the argument so can iterate through
   for i in comment:
      # whenever a blank space is encountered it replaces it with an empty character, getting rid of it
      i.replace(" ","")
   # after all blank spaces removed each string is joined together again with a single blank space in between
   return(" ".join(comment) + "\n")


def myshell_help():
   # this function reads through the readme file and displays it on the screen periodically
   f = open("readme", 'r')
   # opens the file and takes all the lines
   helper = [line.rstrip("\n") for line in f]
   x = 0
   y = 20
   # display the first 20 lines
   while x < y:
      print(helper[x])
      x += 1
   y += 20
   while y < len(helper):
      # prompts the user to hit enter in order to continue through the readme file
      usrinp = input("Please hit <Enter> to continue.")
      if len(usrinp) == 0:
         # displays 20 lines each time as long as there is at least 20 lines to display
         while x < y:
            print(helper[x])
            x += 1
         y += 20
   # when there is less than 20 lines left to display move here
   while x < len(helper):
      print(helper[x])
      x += 1


def myshell_environ():
   # this function displays all of the environment strings
   for i in os.environ:
      # makes the SHELL directory display the full pathname including myshell
      if i == "SHELL":
         print("SHELL: " + os.getcwd() + "/myshell")
      # display the rest of the environment strings
      else:
         print(i + ": " + os.environ[i])


def myshell_clr():
   # this function clrs the screen by pushing the bottom line to the top of the screen
   os.system('clear')


def myshell_dir():
   # this function displays the contents of the directory
   # iterate using os.walk
   for files in os.walk("."):
      for filename in files:
         print(filename)

def myshell_strpinp1(arg, filename):
   # this function handles output redirection
   # particularly creating/overwriting the file
   f= open(filename,"w+")
   i = 0
   # able to handle mulptiple commands being redirected
   while i < len(arg):
      # if using the dir command run the dir function
      if arg[i] == "dir":
         f.write(subprocess.getoutput("dir") + "\n")
         i += 1
      # if using the environ command run the environ command
      elif arg[i] == "environ":
         f.write(subprocess.getoutput("environ") + "\n")
         i += 1
      # if using the echo command
      elif arg[i] == "echo":
         j = i
         a = []
         # seperate the trailing arguments from the other commands so not confused
         while arg[j] != "dir" and arg[j] != "environ" and arg[j] != "echo" and arg[j] != "help":
            a.append(arg[j])
            j += 1
         n = "".join(a)
         m = myshell_echo(n)
         # run echo function
         f.write(subprocess.getoutput("echo " + m) + "\n")
         i = j
      # if using the help command utilize this instead of running the help function as we do not need to wait for the <Enter> key to be pressed
      elif arg[i] == "help":
         f = open("readme", 'r')
         helper = [line.rstrip("\n") for line in f]
         x = 0
         y = 20
         while x < y:
            f.write(helper[x] + "\n")
            x += 1
         y += 20
         while y < len(helper):
            while x < y:
               f.write(helper[x] + "\n")
               x += 1
            y += 20
         while x < len(helper):
            f.write(helper[x] + "\n")
            x += 1
   f.close()


def myshell_strpinp2(arg, filename):
   # same as strpinp1 function but now instead of overwriting a currently existing file we instead add to it, however still able to create new file using this function
   f= open(filename,"a+")
   i = 0
   while i < len(arg):
      if arg[i] == "dir":
         f.write(subprocess.getoutput("dir") + "\n")
         i += 1
      elif arg[i] == "environ":
         f.write(subprocess.getoutput("environ") + "\n")
         i += 1
      elif arg[i] == "echo":
         j = i
         a = []
         while arg[j] != "dir" and arg[j] != "environ" and arg[j] != "echo" and arg[j] != "help":
            a.append(arg[j])
            j += 1
         n = "".join(a)
         m = myshell_echo(n)
         # run echo function
         f.write(subprocess.getoutput("echo " + m) + "\n")
         i = j
      elif arg[i] == "help":
         f = open("readme", 'r')
         helper = [line.rstrip("\n") for line in f]
         x = 0
         y = 20
         while x < y:
            f.write(helper[x] + "\n")
            x += 1
         y += 20
         while y < len(helper):
            while x < y:
               f.write(helper[x] + "\n")
               x += 1
            y += 20
         while x < len(helper):
            f.write(helper[x] + "\n")
            x += 1
         i += 1
   f.close()


def main():
   while True:
      # make the command prompt the pathname of the current directory
      usrinp = input(os.getcwd() + "/myshell$ ")
      strpinp = usrinp.split(" ")
      # if quit is entered then exit the program
      if usrinp == "quit":
         break

      # check if using output redirection
      if ">" in strpinp or ">>" in strpinp:
         # if you want to overwrite a file 
         if strpinp[-2] == ">":
            myshell_strpinp1(strpinp[0:len(strpinp)-2], strpinp[-1])

         # if you want to add to a file
         elif strpinp[-2] == ">>":
            myshell_strpinp2(strpinp[0:len(strpinp)-2], strpinp[-1])
      else:
         # the following if statements all check which command you entered and direct you to the appropriate function
         if usrinp == "dir":
            myshell_dir()

         elif usrinp == "clr":
            myshell_clr()

         elif usrinp == "environ":
            myshell_environ()

         # seperate cd from the directory as this would cause an error
         elif usrinp[:2] == "cd":
            myshell_cd(usrinp[3:])

         # same as cd, seperate echo from the arguments
         elif usrinp[:4] == "echo":
            t = myshell_echo(usrinp[5:])
            print(t)

         elif usrinp == "help":
            myshell_help()

         elif usrinp == "pause":
            myshell_pause()

         else:
            # if the entered command was not any of the above commands then check to see if it was a file and if so read the file for commands.
            try:
               f = open(usrinp, 'r')
               commands = [line.rstrip("\n") for line in f]
               for i in commands:
                  os.system(i)
               # after file has been read exit the shell
               break
            # after going through everything and the command still hasn't been sorted then it must not be a valid command so display an error message to inform the user
            except Exception:
               print("Error: command not valid: {}".format(usrinp))


if '__main__' == __name__:
   main()
