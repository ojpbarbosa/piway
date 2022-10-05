import darkdetect

theme = darkdetect.theme()

colors = {
    'primary': '#101010' if theme == 'Dark' else '#ffffff',
    'secondary': '#ffffff' if theme == 'Dark' else '#101010',
}
