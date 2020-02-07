This othello game uses alpha beta pruning. The function is noted at line 405 in the code.
def alphaBeta(self, node, depth, alpha, beta, maximizing)

The function is called with these arguments:
alphaBeta(self.array, depth, -float("inf"), float("inf"), 1)

“Self.array” is current board state, “depth” is the depth limit set globally athe the start of the program, “-float("inf")” and “float("inf")” are the values for alpha and beta, and the 1 is to initialize the Maximizing if-condition check.

It first makes lists with all valid moves and valid board states using the variables “boards” and “possible_moves”. It also creates a variable “value” with the value -float("inf") for maximizing, and float("inf") for minimizing. It then calls itself with a possible board state, lowers the depth by one, and sets the maximizing flag to 0 so it will go to min. It continues to do this between minimizing and maximizing.

After each time a value is returned from the function it is compared to the variable “value” to see if it is larger when maximizing and smaller when minimizing. If it meets one of these conditions, that board state and move choice are save as the best board and best choice. If it is maximizing it will set alpha to the Max(alpha, value) and if it is minimizing it will set to min(beta, value). It will continue to do this until beta is less than or equal to alpha, depth reaches 0, or it runs out of possible moves from the choices list created at the beginning. It then returns the value, the best board, and the bestchoice.

Here is what a  board state would look like:

[[None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, 'w', 'w', 'w', None, None],
 [None, None, None, 'b', 'b', 'b', None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None]]

Here is what the possible move list could look like:
[3, 5]


For the heuristic, normal tiles are worth 1 point, edge tiles worth 3 points, and corner tiles worth 5 points. The function accepts an array representing a possible board state and checks for each of these based on the x and y coordinates and finds the score by adding the points from the AI pieces and subtracting points for the opposing player pieces.
