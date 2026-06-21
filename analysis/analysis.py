

# region Imports
from matplotlib import pyplot as plt
import csv
# endregion

# region Background
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot()
ax1.set_title("Energy Diagram")
ax1.set_xlabel("Frame")
ax1.set_ylabel("Energy")
#ax1.set_xlim(-60, 60)
#ax1.set_ylim(-60, 60)
ax1.grid(True)
# endregion

# region Plotting

file = open('data/energy.csv', 'r')
reader = csv.reader(file)
next(reader)

row_list = list(reader)
file.close()

frames = []
energies = []
for row in row_list:
    frames.append(float(row[0]))
    energies.append(float(row[1]))

ax1.plot(frames, energies, label="particle energies")
# plotting both particles' energies

plt.show()
# endregion