# telegram_robbinsvault_bot
 
*Current work in progress.*

Designed for control over a basic server at home, or any other system.

## Implemented Features ##
- Added login and logout function for basic security
- Added basic grab of system IP address for local access
    - Great for use with Raspberry Pis if you don't have the system set as a static IP and is on a constant changing DHCP server.

## Planned Features ##
- Adding a watchdog system to let me know when files have moved in certain directories.
- Add different users, if classified as a moderator account.
- Add Docker Monitoring System 
- Add notifactions for:
  - CPU Overheating
  - Hard Drive issues
  - Unhealthy Docker Containers
- Update database for users and logging to a remote database as a pose to a local .json file (Currently using TinyDB for testing purposes).

## Ignored Files for Privacy ##
Folder - configuration

    - config.ini
```
    [Telegram]
    token=blahblahblah

    [TinyDB]
    setup = False / True
```

    - db.json 
        - file should be created automatically if setup is set to false

