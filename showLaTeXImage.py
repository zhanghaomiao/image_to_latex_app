pageSource = r"""
            <!DOCTYPE html>
        <html>
        <head>
        <style>
        .center {
          padding: 10px 0;
          text-align: center;
        }
        </style>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>MathJax example</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async
                src="https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js">
        </script>
        </head>
        <body>
        <div class = "center">
        <p>
        </p>
        </div>
        </body>
        </html>
        """


def convertHtml(string="<Showing the LaTeX converted image>"):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(pageSource, features='lxml')
    soup.p.string = string
    return str(soup)
