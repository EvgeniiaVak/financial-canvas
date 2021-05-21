from bokeh.models import ColumnDataSource


def create_sources(df, selected_from=None, name='main'):
    sources = {}

    def get_bokeh_source(df):
        dict_source = {'index': df.index}
        for column in df.columns:
            dict_source[column] = df[column]
        return ColumnDataSource(dict_source)

    source_df = df[df.index >= selected_from] if selected_from else df
    source = get_bokeh_source(source_df)
    origin = get_bokeh_source(df)

    sources.update({
        name: (source, origin),
    })

    return sources


def read_file(file_name):
    contents = ""
    with open(f'financial_canvas/js_collbacks/{file_name}') as f:
        contents = f.read()
        return contents
