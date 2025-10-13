# Package Management in Linux

## 1. What is a Package?

A **package** in Linux is a collection of files that together make up a program. 
It usually includes:
- **Executable files** (to run the program)
- **Libraries** (shared code used by other programs)
- **Configuration files** (settings)
- **Metadata** (info like version and dependencies)

## 2. Common Package Formats
 Format 
 `.deb`   -  Debian / Ubuntu ( For Debian-based systems )
 `.rpm`   - Fedora / Red Hat ( For Red Hat-based systems )
 `.tar.gz`- All Linux systems ( Source code packages )

## 3. What is a Package Manager?

A **package manager** helps you install, update, and remove software easily. 
It automatically handles dependencies and updates.

The main tool for Ubuntu and Debian systems is **`apt`** (Advanced Package Tool).

## 4. Common `apt` Commands

| Command | Description |
|----------|-------------|
| `sudo apt update` | Updates the package list |
| `sudo apt upgrade` | Upgrades installed packages |
| `sudo apt install [package]` | Installs a new package |
| `sudo apt remove [package]` | Removes a package |
| `sudo apt purge [package]` | Removes a package + configs |
| `sudo apt search [package]` | Searches for a package |
| `apt-cache depends [package]` | Shows dependencies |

