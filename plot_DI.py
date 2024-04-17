from colour import Color
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def colorFader(
    c1, c2, mix=0
):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


def plot_sheet(data: pd.DataFrame, title: str):
    freq = data.iloc[1:, 0]
    theta = np.deg2rad([0, 60, 120, 180, 240, 300, 360])
    DI_all = data.iloc[1:, 14:21]

    print(DI_all)
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction("clockwise")

    for index, row in DI_all.iterrows():
        DI_row = [*row.to_list(), row.to_list()[0]]
        plt.plot(
            theta,
            DI_row,
            color=colorFader("red", "blue", index / len(DI_all.index)),
            linewidth=0.8,
        )
    plt.title(title)
    ax.set_ylim(-20, 20)
    ax.set_yticks(np.array([-10, 0, 10]))
    ax.set_xticks(theta[:-1])
    plt.savefig(f"figures/dirindx_{title}.png")


plot_sheet(
    data=pd.read_excel("data/FinalProject_Data.xlsx", sheet_name="Ground-level DI"),
    title="Ground-Level DI",
)
plot_sheet(
    data=pd.read_excel("data/FinalProject_Data.xlsx", sheet_name="Elevated DI"),
    title="Elevated DI",
)
