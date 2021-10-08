| trace  | elem op. | value            | elem der.              | grad x | grad y         |
| ------ |:--------:| ----------------:|------------------------| ------:| --------------:|
| x      |   input  |$\frac{\pi}{2}$   |       1                |   1    |   0             |
| y      |   input  |  $\frac{\pi}{3}$ |       1                |   0    |   1              |
| v_1    |  sin(x)  |     1            |  cos(x)\dot{x}         |   0    |   0              |
| v_2    |  cos(y)  |    \frac{1}{2}   |  -sin(y)\dot{y}        |  0     | -\frac{\sqrt{3}}{2} |
| v_3    |v_1 - v_2 |    \frac{1}{2}   | \dot(v_1) - \dot(v_2)  |  0     |  -\frac{\sqrt{3}}{2}   |
| v_4    |  -v_3^2  |    -\frac{1}{4}  |  -2 v_3 \dot(v_3)      |  0    |      \frac{\sqrt{3}}{2}            |
| v_5    |\exp(v_4) |\exp(-\frac{1}{4})|   \exp(v_4) \dot(v_4）  |  0     |  \exp( -\frac{1}{4} )  \times \frac{\sqrt{3}}{2}   |
