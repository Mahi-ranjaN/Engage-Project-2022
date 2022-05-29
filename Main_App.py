#*************IMPORTING MODULES**************
import dash
from dash import dcc , html ,Input , Output , State
import dash_labs as dl
import dash_bootstrap_components as dbc
import dash_auth



#*************INITIALIZING THE APPLICATION*************
app = dash.Dash(
      __name__ ,
      plugins = [dl.plugins.pages] , 
      external_stylesheets= [dbc.themes.BOOTSTRAP]
)

# *************LOGIN AUTHENTICATION*************
auth = dash_auth.BasicAuth(
      app,
      {'EngageProject' : 'MahiRanjan'}
      # username , user password
)
#*************NAVIGATION BAR*************
navbar = dbc.NavbarSimple(
      dbc.Nav(
            [
                  dbc.NavLink(page["name"],href = page["path"])
                  for page in dash.page_registry.values()
                  if page.get("top_nav")
            ]
      ),
      brand = "Automobile Industry",
      color="primary",
      dark = True,
      className="mb-1"
)

#***********APP LAYOUT AND PLUGINS**************
app.layout = dbc.Container(
      [navbar , dl.plugins.page_container],
      fluid = True,
)


#*************************************************************
if __name__ == "__main__":
      app.run_server(debug = True)