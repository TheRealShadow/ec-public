![EmpireConquestBanner](https://imgshare.io/images/2020/06/19/Empire-Conquestedit.md.png)
# Empire Conquest
Empire Conquest is a text based RTS game for Telegram. The player itself starts with a small village which he can grow and conquer more villages along the way building it's empire with his clan.

## Prequisites

- Python 3.7
- MySql Database
    - For this Bot to work locally you need a MySql Database (it might work with others but for now I don't support them).
- [pipenv](https://github.com/pypa/pipenv) (Python virtual environment and packaging tool)

## Installation

Make sure that you have the prequisites installed and the code checked out.

First create a new Schema in your Database by executing the following SQL (modify the schema name):
```sql
CREATE SCHEMA `yourschemaname` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci ;
```
<br><br>
Then switch to the checked out directory in the Terminal and run:

```bash
pipenv sync
```
This will install all needed python packages in a separate virtual environment.
<br><br><br>
Next is to create the logs folder in the root directory:
```bash
mkdir logs
```

In the resources folder is an example config file. 
<br><br><br>
For the bot to work you need to create a working config:
```bash
cp example_config.cfg config.cfg
--> make your changes in the "config.cfg"
cp config.cfg current_config.cfg
```
<br><br>
After everything is set up we create the necessary tables in the schema.

For this we execute the following in the root directory:
```bash
pipenv run python inserts.py
pipenv run python database_import.py
```

## Usage
To run the bot, simply issue the follwing in the root directory:
```bash
pipenv run python main.py
```

## Contributing
This repository has a project where ideas for functionalities are stored.
After sighting the idea and discussing it with the other participants, move that task into the coresponding swimlane. Please keep those updated, so that everyone else can track work in progress.

Please use Pull Request for making changes in the code, so i can keep track on whatever changes is beeing done.
