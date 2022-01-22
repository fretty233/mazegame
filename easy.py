from pyamaze import maze,COLOR,agent,textLabel
m=maze(10,10)
m.CreateMaze(loopPercent=100)
print(m.maze_map)

a=agent(m,10,10)
print(a.position)

a=agent(m,footprints=True,filled=True)

# m.enableArrowKey(a)

textLabel(m,'Total Cells',m.rows*m.cols)
m.tracePath({a:m.path},delay=200,kill=True)

m.run()