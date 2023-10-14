from dash import Dash, html
import dash_vtk
from dash_vtk.utils import to_mesh_state
from vtkmodules.vtkImagingCore import vtkRTAnalyticSource

data_source = vtkRTAnalyticSource()
data_source.Update()
dataset = data_source.GetOutput()

mesh_state = to_mesh_state(dataset)
content = dash_vtk.View([
    dash_vtk.GeometryRepresentation([
        dash_vtk.Mesh(state=mesh_state)
    ]),
])

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "100vh"},
    children=[content],
)

if __name__ == "__main__":
    app.run(debug=True)
