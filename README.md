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
cd
```

3. copy "$HOME/umbrel/bin/bitcoin-cli" to "$HOME/umbrel/bin/bitcoin-cli2" and 

```bash
cat $HOME/umbrel/bin/bitcoin-cli | sed -e 's/exec/exec -T/' > $HOME/umbrel/bin/bitcoin-cli2 ; chmod u+x $HOME/umbrel/bin/bitcoin-cli2
```

4. create $HOME/watch_block.sh and edit

```bash
#!/bin/bash

before=0
while :
do
  count=`$HOME/umbrel/bin/bitcoin-cli2 getblockcount | sed -e 's/\r//g' -e 's/\n//g'`
  if [ "$before" != "$count" ]; then
    dt=`date +'%Y/%m/%d'`
    tm=`date +'%T'`
    tmp_cpu=`vcgencmd measure_temp`
    python3 $HOME/lnshield/lnshield_tools/epaper.py "" "$count" "$dt" "$tm" "$tmp_cpu"
    before=$count
  fi
  sleep 180
done
```

5. chmod

```bash
chmod u+x watch_block.sh
```

6. run script file

```bash
nohup ./watch_block.sh &> /dev/null < /dev/null&
```

## References

* [2.7inch ePaper HAT wiki](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT)
* https://www.waveshare.com/wiki/File:2.7inch-e-paper-hat-code.7z
  version: 07:26, 28 November 2018

