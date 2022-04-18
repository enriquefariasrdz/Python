# %%
import matplotlib.pyplot as plot


# %%
cat = ["bored", "happy", "bored"]
dog = ["happy", "bored", "happy"]
activity = ["combining", "drinking", "feeding"]



# %%
fig = ax = plot.subplot()
ax.plot(activity, cat, label="cat")
ax.plot(activity, dog, label="dog")
ax.legend()

plot.show()
# %%
