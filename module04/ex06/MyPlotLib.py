'''Plotting methods among the different libraries:
Pandas, Matplotlib, Seaborn or Scipy.'''

from FileLoader import FileLoader
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:
    def __init__(self) -> None:
        pass

    def histogram(self, data, features):
        if not isinstance(features, list) or not features:
            return None

        # drop lines with NA values
        data_plot = data.dropna(subset=features)

        # plot
        for feature in features:
            plt.hist(data_plot[feature])
            plt.title(feature)
            plt.show()

    def density(self, data, features):
        if not isinstance(features, list) or not features:
            return None

        # drop lines with NA values
        data_plot = data.dropna(subset=features)

        data_plot[features].plot(kind='density')
        plt.show()

    def pair_plot(self, data, features):
        if not isinstance(features, list) or not features:
            return None

        # drop lines with NA values
        data_plot = data.dropna(subset=features)

        # plot
        sns.pairplot(data_plot[features])
        plt.show()

    def box_plot(self, data, features):
        if not isinstance(features, list) or not features:
            return None
        
        # drop lines with NA values
        data_plot = data.dropna(subset=features)

        # plot
        plt.boxplot(data_plot[features], labels=features)
        plt.title(f'Box plot of: {features}')
        plt.show()


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    plotter = MyPlotLib()
    plotter.histogram(data, ['Age'])
    plotter.histogram(data, ['Age', 'Height'])
    plotter.histogram(data, ['Age', 'Height', 'Weight'])

    plotter.density(data, ['Age'])
    plotter.density(data, ['Age', 'Height'])
    plotter.density(data, ['Age', 'Height', 'Weight'])

    plotter.pair_plot(data, ['Age'])
    plotter.pair_plot(data, ['Age', 'Height'])
    plotter.pair_plot(data, ['Age', 'Height', 'Weight'])

    plotter.box_plot(data, ['Age'])
    plotter.box_plot(data, ['Age', 'Height'])
    plotter.box_plot(data, ['Age', 'Height', 'Weight'])
