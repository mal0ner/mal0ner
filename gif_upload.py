import gifos


image = gifos.utils.upload_imgbb("no-loop.gif", 129600)  # 1.5 days expiration
readme_file_content = rf"""
<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="{image.url}">
    <source media="(prefers-color-scheme: light)" srcset="{image.url}">
    <img alt="GIFOS_README_TERMINAL" src="{image.url}">
</picture>

<sub><i>Generated automatically using [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal)</i></sub>

</div>
    """
with open("README.md", "w") as fp:
    fp.write(readme_file_content)
    print("INFO: README.md file generated")
