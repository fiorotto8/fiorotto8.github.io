# Local typography

Go Regular, Bold and Italic, by Bigelow & Holmes. Source: the installed
`fonts-go` package; upstream font files are available from
<https://go.googlesource.com/image/+/master/font/gofont/ttfs/>.
The BSD 3-clause licence is retained in `assets/fonts/go/LICENSE.txt`.

The fonts were converted to WOFF2 using fontTools, retaining Latin, extended
Latin, Greek, punctuation, superscripts, arrows and mathematical operators.
The build serves these checked-in assets directly; fontTools is not a build
dependency. No remote font request is made. Uncovered scripts use the fallback.

Input hashes and delivered sizes:

```json
[
  {
    "source": "Go-Regular.ttf",
    "source_sha256": "dd02d2f04dbc9f6329f3777b999fd3985f70b8f69b7c8aa522db3ec1fef9ceb2",
    "output": "go-regular.woff2",
    "bytes": 29276
  },
  {
    "source": "Go-Bold.ttf",
    "source_sha256": "47d5aab3f49d958dd3ab857691b84dfc0b49e143e0e6f37b62f3d3f312c14bf0",
    "output": "go-bold.woff2",
    "bytes": 29660
  },
  {
    "source": "Go-Italic.ttf",
    "source_sha256": "51e880f8a40b39baf291a4ef4c27c9e2eb8c36cb640063f867d213db444195b3",
    "output": "go-italic.woff2",
    "bytes": 30472
  }
]
```

## Social-card rendering

`images/local/identity/social-card.svg` is the local editable source. Its PNG is a checked-in
1200×630 export, so Jekyll does not need an image-rendering dependency.
To reproduce the export on a machine with Go installed and CairoSVG available:

```sh
python3 -m cairosvg images/local/identity/social-card.svg -o images/public/identity/social-card.png
```

Inspect the export after editing; the renderer must have the Go family available
or it will substitute another font.
