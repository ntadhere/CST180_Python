# Island Population Dynamics Simulation

![Flowchart](/img/topic1_flowchart.png)


## Overview
Simulate how rabbit and wolf populations evolve over 20 years on an island.  
- Rabbits start first and grow annually.  
- Wolves arrive in year 5, grow annually, and prey on rabbits.

## Key Parameters
1. **Initial Populations**  
   - Rabbits: 50  
   - Wolves: 0 (years 1–4), then 10 in year 5  

2. **Annual Rates**  
   - Rabbit growth: +10%  
   - Rabbit loss to predation: −1% (once wolves present)  
   - Wolf growth: +8% (once introduced)  
   - Wolf death rate: −6% (once introduced)  

3. **Simulation Length**  
   - 20 years  

## Example Output

| Year | Rabbits | Wolves |
|------|--------:|-------:|
| 1    |      55 |      0 |
| 2    |      60 |      0 |
| 3    |      66 |      0 |
| 4    |      73 |      0 |
| 5    |      79 |     10 |
| 6    |      86 |     10 |
| 7    |      94 |     10 |
| 8    |     102 |     10 |
| 9    |     112 |     10 |
| 10   |     122 |     10 |
| 11   |     132 |     10 |
| 12   |     144 |     11 |
| 13   |     157 |     11 |
| 14   |     171 |     11 |
| 15   |     187 |     11 |
| 16   |     203 |     11 |
| 17   |     221 |     11 |
| 18   |     241 |     12 |
| 19   |     263 |     12 |
| 20   |     286 |     12 |
