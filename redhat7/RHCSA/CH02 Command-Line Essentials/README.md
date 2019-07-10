# Command-Line Essentials

## Shells & Virtual Terminals

### Shells

In Linux, the shell is a command-line interpreter that allows you to interact
 with the operating system. Shells can process commands in various sequences,
 depending on how you manage the input and output of each command. The way
 commands are interpreted is in part determined by variables and parameters
 associated with each shell.

Users can choose between multiple command-line shells:

+ bash - The Bourne-Again shell, this is the default shell based on the
 command-line interpreter originally developed by Stephen Bourne.
+ ksh - The Korn shell, developed by David Korn at Bell Labs in the 1980s,
 to incorporate the best features of the Bourne and C shell.
+ tcsh - An enhanced version of the Unix C shell.
+ zsh - A sophisticated shell, similar to the Korn shell.

These shells are located in the /bin directory. The most direct method to change
 a user's shell is to edit the /etc/passwd file. The other way is to use the 
 __chsh -s /bin/*shell* *username*__ command.

When running a command, the shell cites the full path to that command. For
 example, the __ls__ command is located in the /bin directory. When we run
 __ls__ the shell is actually running __/bin/ls__. This is where the PATH
 environment variable comes in.

The PATH variable is a colon seperated list of directories defined for the current user.
 These directories are searched, in order, for the command being used. You can
 view the PATH variable by running __echo $PATH__. The PATH variable is globally
 defined by the /etc/profile file or scripts in the /etc/profile.d directory.
 The PATH for individual users can be customized by modifying the .bash\_profile
 or .profile hidden files in the user's home directory.

The command line prompt differs between regular users and the root user. A 
 regular user's prompt by default is the username, hostname, and current directory
 followed by a __$__. The root prompt is similar but has a __#__ instead.

```bash
[user@localhost ~]$
```

```bash
[root@localhost ~]#
```

### Virtual Terminals

Virtual terminals is a conceptual combination of the keyboard and display for a 
 computer user interface. It is a feature in which the system console of the 
 computer can be used to switch between multiple virtual consoles to access
 independent login sessions.

Virtual terminals are defined by the /etc/systemd/logind.conf file. By default,
 a maximum of 6 virtual terminals can be activated and are associated with the
 device files /dev/tty1 through /dev/tty6. It's possible to configure more
 virtual terminals but is limited by those allowed for the root administrative
 user in the /etc/securetty file.

To change between virtual terminals, you press the __ALT+F*n*__ to move to the
 *n*th virtual terminal. For example, to swith to the 3rd virtual terminal, I
 would press **ALT+F3**. If I am using a GUI, I would need to use
 __ALT+CTRL+F*n*__ to move to the *n*th virtual terminal.

## Navigation

### pwd

### ls

### cd


## File Searches

### find

### locate


## Manage Files & Directories

### touch

### cp

### mv

### rm

### mkdir

### rmdir

### vi


## Text Streams

### cat

### less & more

### head & tail

### sort

### grep

### sed

### awk


## Command Redirection

### <

### >

### |

### 2>

### &>
