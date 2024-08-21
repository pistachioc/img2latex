import matplotlib
import matplotlib.pyplot as plt

# Runtime Configuration Parameters
matplotlib.rcParams["mathtext.fontset"] = "cm"  # Font changed to Computer Modern


def latex2image(
        latex_expression, image_name, image_size_in=(5, 1), fontsize=20, dpi=300
):
    """
    A simple function to generate an image from a LaTeX language string.

    Parameters
    ----------
    latex_expression : str
        Equation in LaTeX markup language.
    image_name : str or path-like
        Full path or filename including filetype.
        Accepeted filetypes include: png, pdf, ps, eps and svg.
    image_size_in : tuple of float, optional
        Image size. Tuple which elements, in inches, are: (width_in, height_in).
    fontsize : float or str, optional
        Font size, that can be expressed as float or
        {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}.
    dpi : int, optional
        The resolution of the output image in dots per inch.

    Returns
    -------
    fig : object
        Matplotlib figure object from the class: matplotlib.figure.Figure.

    """

    fig = plt.figure(figsize=image_size_in, dpi=dpi)
    text = fig.text(
        x=0.5,
        y=0.5,
        s=latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=fontsize,
    )

    # Save the figure
    plt.savefig(image_name)

    return fig

if __name__ == "__main__":
    latex_expression = r"""$\vec{\nabla}\times\vec{H}=\vec{J}+\dfrac{\partial\vec{D}}{\partial t},$"""
    image_name = "Duc test.png"
    fig = latex2image(latex_expression, image_name, image_size_in=(5, 1), fontsize=20, dpi=300)

    img = plt.imread(image_name)
    plt.imshow(img)
