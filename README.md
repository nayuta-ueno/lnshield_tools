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
  if [ "$before" != "$count" ]; then
    dt=`date +'%Y/%m/%d'`
    tm=`date +'%T'`
    python3 $HOME/lnshield/lnshield_tools/epaper.py "" "$count" "$dt" "$tm"
    before=$count
  fi
  sleep 60
done
```

5. run script file

```bash
bash watch_block.sh
```

### for background

1. copy "$HOME/umbrel/bin/bitcoin-cli" to "$HOME/umbrel/bin/bitcoin-cli2"
2. edit bitcoin-cli2(add `-T` after `exec`)

```bash
#!/usr/bin/env bash

set -euo pipefail

UMBREL_ROOT="$(readlink -f $(dirname "${BASH_SOURCE[0]}")/..)"

result=$(docker-compose \
  --file "${UMBREL_ROOT}/docker-compose.yml" \
  --env-file "${UMBREL_ROOT}/.env" \
  exec -T bitcoin bitcoin-cli "$@")

# We need to echo with quotes to preserve output formatting
echo "$result"
```

3. use bitcoin-cli2 in watch_block.sh

4. run script file

```bash
bash watch_block.sh &> /dev/null < /dev/null&
```

## Base

* https://www.waveshare.com/wiki/File:2.7inch-e-paper-hat-code.7z
  version: 07:26, 28 November 2018

