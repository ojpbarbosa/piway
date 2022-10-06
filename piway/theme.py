import darkdetect

theme = darkdetect.theme()

colors = {
    'primary': '#101010' if theme == 'Dark' else '#ffffff',
    'secondary': '#ffffff' if theme == 'Dark' else '#101010',
    'shade': '#232323' if theme == 'Dark' else '#d2d2d2',
}
