# Poseidon Rate Analysis
These scripts parses the [Poseidon simulator's](https://github.com/StevenSeiden/Poseidon/) data files to perform offline external detection of switch attacks.

### Node Rate Comparison
Compares the sending rate of a real node with simulated node introduced by the analyist.
Example usage: `python3 compare.py example.txt 0b002001 0b000201`

### Switch Responsiveness Test
Tests the impacts of introducing a simulated node on a real node's sending rate. The results can be used to determine if the resulting impact is as expected.
Example usage: `python3 testAddingNode.py example.txt 0b002001 0b000201`
