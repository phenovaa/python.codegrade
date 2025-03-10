widgets_input = input("Number of widgets: ")
widgets_int = int(widgets_input)
gizmos_input = input("Number of gizmos: ")
gizmos_int = int(gizmos_input)

widgets_weight = widgets_int * 75
gizmo_weight = gizmos_int * 112

total_weight = widgets_weight + gizmo_weight

print(f"The Total Weight of the Order: {total_weight}")