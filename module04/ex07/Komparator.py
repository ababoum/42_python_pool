'''Introduce plotting methods among the different libraries:
Pandas, Matplotlib, Seaborn or Scipy'''

from FileLoader import FileLoader
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, df) -> None:
        self.df = df.dropna()

    def compare_box_plots(self, categorical_var, numerical_var):
        categories = [item[categorical_var] for _, item in (
            self.df[[categorical_var]].drop_duplicates()).iterrows()]

        # plot
        fig, axes = plt.subplots(ncols=len(categories))
        for i, category in enumerate(categories):
            axes[i].boxplot(self.df[self.df[categorical_var] ==
                            category][[numerical_var]], labels=[category])
        fig.suptitle(f'Compare {numerical_var} box plots by {categorical_var}')
        plt.show()

    def density(self, categorical_var, numerical_var):
        categories = [item[categorical_var] for _, item in (
            self.df[[categorical_var]].drop_duplicates()).iterrows()]

        # plot
        for category in categories:
            self.df[self.df[categorical_var] == category][numerical_var].plot(
                kind='density', label=numerical_var)
        plt.legend(categories)
        plt.title(
            f'Compare {numerical_var} density plots by {categorical_var}')
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        categories = [item[categorical_var] for _, item in (
            self.df[[categorical_var]].drop_duplicates()).iterrows()]

        # plot
        fig, axes = plt.subplots(ncols=len(categories))
        for i, category in enumerate(categories):
            axes[i].hist(self.df[self.df[categorical_var] ==
                            category][[numerical_var]])
            axes[i].set_title(category)
        fig.suptitle(f'Compare {numerical_var} box plots by {categorical_var}')
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    kp = Komparator(data)
    # kp.density('Sex', 'Height')
    # kp.density('Sex', 'Weight')
    kp.compare_box_plots('Medal', 'Age')
    kp.compare_histograms('Medal', 'Age')
    kp.density('Medal', 'Age')
