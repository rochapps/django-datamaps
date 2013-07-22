from django import template
from django.conf import settings

register = template.Library()


# TODO: Allow for custom popup templates to be passed.
@register.inclusion_tag('datamaps/tags/scope_template.html')
def display_scoped_map_with_bombs(scope, element_id, data, bombs, fills):
    """Renders a map with a close-up look to the scope the country belongs to.

    Args:

    scope -> datamaps scope instance.

    element_id -> ID for the DOM element where the map is going to render.
    This element should contain the following css rules: position, (relative),
    width and height. You can set the width and a height to be a percentage but
    map will not render correctly cross-browser.

    data -> Json object that contains data for the popup template.

    bombs -> JSON object that contains info about the bombs that the map will
    render. This object needs at a minimum the lat, lon, and radius as
    attributes.

    fills -> JSON object with info about colors to be use for our data. It should
    at least contain a defaultFill attribute.

    """
    # template variables
    return {'element_id': element_id, 'map_data': data,
            'map_bombs': bombs, 'fills': fills, 'scope': scope}


@register.inclusion_tag('datamaps/tags/libraries.html')
def load_map_libraries(datamaps=True, topojson=True, d3=True):
    return {"STATIC_URL": settings.STATIC_URL, 'd3': d3,
            'topojson': topojson, 'datamaps': datamaps}