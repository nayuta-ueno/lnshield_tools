ePaper control for Lightning Shield
====

## Usage

### install

```bash
git clone https://github.com/nayuta-ueno/lnshield_tools.git
cd lnshield_tools
python3 install -r requirements.txt
```

### init

```bash
python3 gpio_init.py
```

### display message

```bash
python3 epaper.py "" "hello" "world" "" "I'm Umbrel!"
```

### LED

```bash
python3 gpio.py 1 0
python3 gpio.py - 1
```

## Example

1. login Umbrel using terminal app
2. install and setup

```bash
mkdir lnshield
cd lnshield
git clone https://github.com/nayuta-ueno/lnshield_tools.git
cd lnshield_tools
python3 install -r requirements.txt
python3 gpio_init.py
```

3. goto Umbrel directory

```bash
cd ~/umbrel
```

4. create script file

```bash
vi watch_block.sh
```

```text
#!/bin/bash

before=0
while :
do
  count=`bin/bitcoin-cli getblockcount | sed -e 's/\r//g' -e 's/\n//g'`
  if [ $before != $count ]; then
    python3 $HOME/lnshield/lnshield_tools/epaper.py "" $count
    before=$count
  fi
  sleep 300
done
```

5. run script file

```bash
bash watch_block.sh
```

## Base

* https://www.waveshare.com/wiki/File:2.7inch-e-paper-hat-code.7z
  version: 07:26, 28 November 2018

* https://github.com/elad661/rpi_epd2in7
  commit: 8fd09f4a6a2c8ba26bfd216255c95e6abdad1333

