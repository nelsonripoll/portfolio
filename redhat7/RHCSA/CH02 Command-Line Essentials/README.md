# Command-Line Essentials

## Shells, Commands & Virtual Terminals

### Shells

### Commands

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

To change between virtual terminals, you press the **ALT+F_n_** to move to the
 _n_th virtual terminal. For example, to swith to the 3rd virtual terminal, I
 would press **ALT+F3**. If I am using a GUI, I would need to use
 **ALT+CTRL+F_n_** to move to the _n_th virtual terminal.

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
