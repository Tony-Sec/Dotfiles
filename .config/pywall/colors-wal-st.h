const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0c1010", /* black   */
  [1] = "#926F3D", /* red     */
  [2] = "#66897A", /* green   */
  [3] = "#CB883A", /* yellow  */
  [4] = "#A09C74", /* blue    */
  [5] = "#DCAD69", /* magenta */
  [6] = "#FBD07A", /* cyan    */
  [7] = "#b4c1b7", /* white   */

  /* 8 bright colors */
  [8]  = "#7d8780",  /* black   */
  [9]  = "#926F3D",  /* red     */
  [10] = "#66897A", /* green   */
  [11] = "#CB883A", /* yellow  */
  [12] = "#A09C74", /* blue    */
  [13] = "#DCAD69", /* magenta */
  [14] = "#FBD07A", /* cyan    */
  [15] = "#b4c1b7", /* white   */

  /* special colors */
  [256] = "#0c1010", /* background */
  [257] = "#b4c1b7", /* foreground */
  [258] = "#b4c1b7",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
