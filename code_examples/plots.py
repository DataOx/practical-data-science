def histPlot(ds, xlimMin, xlimMax, xlab, ylab, title):
    """hist plot for a column

    Args:
        ds (series): input column to plot
        xlab (string): x label text
        ylab (string): y label text
        title (string): title string
    """
    ftsize = 18
    plt.figure(figsize=(15, 10))
    sns.distplot(ds, bins=100)
    plt.xticks(rotation=45, fontsize=ftsize)
    plt.xlabel(xlab, fontsize=ftsize)
    plt.xlim(xlimMin, xlimMax)
    plt.ylabel(ylab, fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.title(title, fontsize=ftsize)


def barPlot(ds, title, topN):
    """bar plot for a column

    Args:
        ds (series): input column to plot
        xlab (string): x label text
        ylab (string): y label text
        title (string): title string
    """
    # print(ds[:topN].index)
    # print(ds[:topN].values)
    ftsize = 18
    plt.figure(figsize=(16, 9))
    #sns.barplot(x=ds[:topN].index, y=ds[:topN].values)
    plt.bar(x=ds[:topN].index, height=ds[:topN].values)
    plt.xticks(rotation=45, fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.title(title, color='blue', fontsize=ftsize)
