import gifos


def main():
    gif = gifos.utils.upload_imgbb("no-loop.gif", 129600)
    readme_file_content = rf"""
<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="{gif.url}">
    <source media="(prefers-color-scheme: light)" srcset="{gif.url}">
    <img alt="GIFOS_README_TERMINAL" src="{gif.url}">
</picture>

<sub><i>Generated automatically using [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal)</i></sub>

</div>
    """
    with open("README.md", "w") as fp:
        fp.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
