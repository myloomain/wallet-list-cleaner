### wallet-list-cleaner
simple and efficient python script for processing wallet lists before opensea minting

### what this script does:
1. **deduplication**: finds duplicate addresses, merges them into a single line, and sums up the total number of nfts for the mint
2. **gtd priority**: if an address exists in the guaranteed mint (gtd) list, it is automatically removed from the fcfs list to prevent confusion and errors during contract or opensea uploads
3. **csv formatting**: generates ready-to-use files in `address,amount` format
4. **lowercase conversion**: automatically converts all addresses to lowercase to avoid duplicates caused by different letter cases

### how to use:
1. place your `gtd.txt` and `fcfs.txt` files in the same folder as the script
2. run the script: `python web3-wallet-tools.py`
3. find your results in `gtd_final.csv` and `fcfs_final.csv` files
