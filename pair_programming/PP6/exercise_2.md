### x^2 +y^2
| trace  | elem op. | value            | elem der.              | grad x | grad y         |
| ------ |:--------:| ----------------:|------------------------| ------:| --------------:|
|  x     |   input  |       1          |      \dot(x)                  |   1    |        0       |
| y      |   input  |  1               |       \dot(y)                |   0    |   1            |
| v_1    |  x^2     |      1           |  2x\dot(x)             |   2    |   0            |
| v_2    |  y^2     |   1              |  2y\dot(y)             |  0     | 2              |
| v_3    |v_1 + v_2 |    2             | \dot(v_1) + \dot(v_2)  |  2     | 2              |


#### exp(x+y)
| trace  | elem op. | value          | elem der.              | grad x | grad y     |
| ------ |:--------:| --------------:|------------------------| ------:| ----------:|
| x      |   input  |        1       |      \dot(x)                 |   1    |   0        |
| y      |   input  |        1       |       \dot(y)               |   0    |   1        |
| v_1    |  x+y     |     2          |  \dot(x) + \dot(y)     |   1    |   1         |
| v_2    |\exp(v_1) |    \exp(2)     |   \exp(v_1) \dot(v_1） | \exp(2)| \exp(2)     |
