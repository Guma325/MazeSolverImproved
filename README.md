# MazeSolverImproved
Appling iteration strategies in the Dead end algorithm in maze problems.

To run this project you will need to install the follow libraries:
* Numpy
* Pandas
* Opencv2

After installing the deppendences, all you need is to import the MazeSolver object.
You can also import the Plot and Timer libraries if you want to compare the execution time.

MazeSolver object parameters:
* Maze .png file
* Possible path color
* Maze exits color
* Wall color
* Dead end color
* (Optional) Generates the imgs for the video creation

## Python example:

```python
import MazeSolver
import Plot
import Timer

mazeSolver = MazeSolver.MazeSolver("maze41x41.png", 255, 127, 0, 50, True)
plot = Plot.Plot(mazeSolver)

timer = Timer.Timer()
mazeSolver.solve("rotation")
timer.stop()
plot.add_plot_line()
mazeSolver.save_solution_video("temp_imgs/", "solutions/videos/", 120)
mazeSolver.save_solution("solutions/imgs/")

plot.show()
```

## Image output example:
<img src="https://github.com/JCGCosta/MazeSolverImproved/blob/master/solutions/imgs/maze301x301_36502_solved.png?raw=true" alt="301x301MazeSolution" title="Output solution example.">
