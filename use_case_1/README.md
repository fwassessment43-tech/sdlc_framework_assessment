# Prompt:

> ```
> Create a snake game in Python
> ## Requirements:
> ### Game Board:
> - Create a grid-based game board.
> - Define the dimensions of the grid (e.g., 10x10).
> - Display the grid on the screen.
> ### Snake Initialization:
> - Place the snake on the game board.
> - Define the initial length and starting position of the snake.
> - Choose a direction for the snake to start moving immediately, without user input (e.g., right).
> ### Snake Movement:
> - Implement arrow key controls for snake movement.
> - Ensure the snake moves continuously in the chosen direction.
> - Update the snake’s position on the grid.
> ### Food Generation:
> - Generate food at random positions on the game board.
> - Ensure food doesn’t appear on the snake’s body.
> ### Collision Handling:
> - Detect collisions between the snake and the game board boundaries.
> - Detect collisions between the snake’s head and its body.
> - Detect collisions between the snake’s head and the food.
> ### Snake Growth:
> - Increase the length of the snake when it consumes food, adding a new segment to the snake’s body.
> ### Score Display:
> - Implement a scoring system.
> - Display the current score on the screen.
> ### Game Over Condition:
> - Trigger a game over scenario when the snake collides with the boundaries.
> - Trigger a game over scenario when the snake collides with its own body.
> - Display a game over message.
> - Allow the player to restart the game.
> ### Graphics and User Interface:
> - Use graphics or ASCII characters to represent the snake and food.
> - Design a user-friendly interface with clear instructions.
> ### Animations and Effects:
> - Add animations for snake movement and growth.
> - Implement visual effects for collisions and food consumption.
> ```


# RQ1 – UC1 Results

**Performance of different LLMs without frameworks and combined with different frameworks (UC1).**  
Notation:  
- **CG (Y/N)**: Code Generated  
- **CE (Y/N)**: Code Executed  
- **RT**: Runtime (seconds)  
- **RM**: Requirements Met (out of 10)

| Scenario | CG | CE | RT (s) | RM |
|----------|----|----|--------|----|
| qwen_32b_q4 | Y | Y | 233.00 | 8 |
| qwen_32b_q4 + MetaGPT | Y | Y | 1361.28 | 4 |
| qwen_32b_q4 + ChatDev | Y | N | 10277.00 | 0 |
| qwen_32b_q4 + AgileCoder | Y | Y | 2641.00 | 8 |
| qwen_32b_q4 + HyperAgent | Y | Y | 161.97 | 1 |
| gemma_27b_fp16 | Y | Y | 866.00 | 9 |
| gemma_27b_fp16 + MetaGPT | Y | Y | 4739.48 | 0 |
| gemma_27b_fp16 + ChatDev | N | N | 20995.00 | 0 |
| gemma_27b_fp16 + AgileCoder | Y | Y | 4969.00 | 3 |
| gemma_27b_fp16 + HyperAgent | Y | N | 2168.33 | 0 |
| qwen2_7b_fp16 | Y | Y | 131.00 | 8 |
| qwen2_7b_fp16 + MetaGPT | Y | N | 719.93 | 0 |
| qwen2_7b_fp16 + ChatDev | N | N | 1911.00 | 0 |
| qwen2_7b_fp16 + AgileCoder | Y | N | 1636.00 | 0 |
| qwen2_7b_fp16 + HyperAgent | Y | Y | 93.14 | 1 |
| qwen2_7b_q4 | Y | N | 68.00 | 0 |
| qwen2_7b_q4 + MetaGPT | Y | Y | 356.07 | 0 |
| qwen2_7b_q4 + ChatDev | N | N | 851.00 | 0 |
| qwen2_7b_q4 + AgileCoder | Y | Y | 2541.00 | 2 |
| qwen2_7b_q4 + HyperAgent | Y | N | 91.91 | 0 |
| gpt_oss_20b | Y | Y | 32.00 | 0 |
| gpt_oss_20b + MetaGPT | Y | Y | 561.67 | 8 |
| gpt_oss_20b + ChatDev | Y | Y | 306.00 | 10 |
| gpt_oss_20b + AgileCoder | Y | Y | 623.00 | 3 |
| gpt_oss_20b + HyperAgent | N | N | 18.09 | 0 |
| llama3_70b_q3 | Y | Y | 302.00 | 8 |
| llama3_70b_q3 + MetaGPT | Y | Y | 2190.71 | 8 |
| llama3_70b_q3 + ChatDev | Y | Y | 3075.00 | 4 |
| llama3_70b_q3 + AgileCoder | Y | Y | 24000.00 | 0 |
| llama3_70b_q3 + HyperAgent | Y | Y | 2812.85 | 8 |
| llama3_70b_q4 | Y | Y | 506.00 | 5 |
| llama3_70b_q4 + MetaGPT | N | N | 2777.27 | 0 |
| llama3_70b_q4 + ChatDev | Y | Y | 3379.00 | 6 |
| llama3_70b_q4 + AgileCoder | Y | Y | 31906.00 | 6 |
| llama3_70b_q4 + HyperAgent | Y | Y | 779.40 | 0 |
| devstral_24b_fp16 | Y | Y | 440.00 | 7 |
| devstral_24b_fp16 + MetaGPT | Y | Y | 1400.02 | 8 |
| devstral_24b_fp16 + ChatDev | Y | N | 4506.00 | 0 |
| devstral_24b_fp16 + AgileCoder | Y | N | 1325.00 | 0 |
| devstral_24b_fp16 + HyperAgent | Y | N | 2649.08 | 0 |