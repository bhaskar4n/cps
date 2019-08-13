#dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
import dash
from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta
from datetime import datetime
from dateutil import tz
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import math
from textwrap import dedent as d
import json
#xx = [10,20,30,40,50,60,70]
#yy = [10,20,30,50,60,70,80]
t = datetime.today().strftime('%Y-%b-%d %H:%M:%S')
"""
i = 0
j = 0
ch2x = []
ch2y = []
mx = []
my = []
with open('/home/baskar/Desktop/x.txt') as f:
	for line in f:
		ch2x.append(line[:-1])
		i = i+1
		if i==3500:
			break
with open('/home/baskar/Desktop/y.txt') as f:
	for line in f:
		ch2y.append(line[:-1])
		j = j+1
		if j==3500:
			break

i = 0
j = 0
with open('/home/baskar/Desktop/x1.txt') as f:
	for line in f:
		mx.append(line[:-1])
		i = i+1
		if i==4500:
			break
with open('/home/baskar/Desktop/y1.txt') as f:
	for line in f:
		my.append(line[:-1])
		j = j+1
		if j==4500:
			break
"""
from_zone = tz.tzlocal()
to_zone = tz.tzutc()


utc = datetime.utcnow().strftime('%Y-%b-%d %H:%M:%S')

ut = utc[:-4]+'0:00.0000'
print (ut)
#print t
#k = str(t)[:-11]+'0:00.0000'
#k = t[:-4]+'0:00.0000'
k = ut
"""
obj = Horizons(id='chandrayaan', location='500',epochs={'start':'2019-07-24', 'stop':'2019-08-20',
                       'step':'10m'},id_type='majorbody')

obj1 = Horizons(id='301', location='500',epochs={'start':'2019-07-01', 'stop':'2019-08-20',
                       'step':'10m'},id_type='majorbody')
vec = obj.vectors()
vec1 = obj1.vectors()
"""
ch2x = []
ch2y = []
ch2z = []
chvx = []
chvy = []
chvz = []
s = ['datetime_str','x','y','z','vx','vy','vz']
date = []

mx = []
my = []
mz = []
mvx = []
mvy = []
mvz = []

s1 = ['datetime_str','x','y','z','vx','vy','vz']
date1 = []
with open('ch2.json','r') as json_file:
    c_data = json.load(json_file)

with open('luna.json','r') as json_file:
    moon_data = json.load(json_file)


slide = len(c_data)

for data in c_data:
    date.append(data['date'][5:])
    ch2x.append(data['cx']*149597870.691)    
    ch2y.append(data['cy']*149597870.691)
    ch2z.append(data['cz']*149597870.691)
    chvx.append(data['cvx']*149597870.691/86400)
    chvy.append(data['cvy']*149597870.691/86400)
    chvz.append(data['cvz']*149597870.691/86400)

for data in moon_data:
    date1.append(data['date'][5:])
    mx.append(data['mx']*149597870.691)
    my.append(data['my']*149597870.691)
    mz.append(data['mz']*149597870.691)
    mvx.append(data['mvx']*149597870.691/86400)
    mvy.append(data['mvy']*149597870.691/86400)
    mvz.append(data['mvz']*149597870.691/86400)
    
#utc times
#2019-Jul-24 00:00:00.0000
burn_1 = '2019-Jul-24 09:20:00.0000'
burn_2 = '2019-Jul-25 19:30:00.0000'
burn_3 = '2019-Jul-29 09:40:00.0000'
burn_4 = '2019-Aug-02 09:50:00.0000'
burn_5 = '2019-Aug-06 09:30:00.0000'
burn_6 = '2019-Aug-14 08:30:00.0000'

burn1 = date.index(burn_1)
burn2 = date.index(burn_2)
burn3 = date.index(burn_3)
burn4 = date.index(burn_4)
burn5 = date.index(burn_5)
burn6 = date.index(burn_6)

print('burn1: ', date[burn1],burn1)
print('burn2: ', date[burn2],burn2)
print('burn3: ', date[burn3],burn3)
print('burn4: ', date[burn4],burn4)
print('burn5: ', date[burn5],burn5)
print('burn6: ', date[burn6],burn6)
# for astroquery only
"""    
for i in range(len(vec)):
    date.append(vec[s][i][0][5:])
    xaxis = vec[s][i][1]*149597870.691
    yaxis = vec[s][i][2]*149597870.691
    zaxis = vec[s][i][3]*149597870.691
    vx = vec[s][i][4]*149597870.691/86400
    vy = vec[s][i][5]*149597870.691/86400
    vz = vec[s][i][6]*149597870.691/86400
    ch2x.append(xaxis)    
    ch2y.append(yaxis)
    ch2z.append(zaxis)
    chvx.append(vx)
    chvy.append(vy)
    chvz.append(vz)
	#ch2x.write(xaxis)
	#ch2y.write(yaxis)
#	print date[i],x[i],y[i]
"""
"""
for i in range(len(vec1)):
    date1.append(vec1[s1][i][0][5:])
    moon_xaxis = vec1[s1][i][1]*149597870.691
    moon_yaxis = vec1[s1][i][2]*149597870.691
    moon_zaxis = vec1[s1][i][3]*149597870.691
    vx = vec1[s1][i][4]*149597870.691/86400
    vy = vec1[s1][i][5]*149597870.691/86400
    vz = vec1[s1][i][6]*149597870.691/86400
    mx.append(moon_xaxis)
    my.append(moon_yaxis)
    mz.append(moon_zaxis)
    mvx.append(vx)
    mvy.append(vy)
    mvz.append(vz)
	#moonx1.write(moon_xaxis)
	#moony1.write(moon_yaxis)
#	print date1[i],x1[i],y1[i]
"""
#print (len(vec))
ind = date.index(k)
print ('Now',k)
print ('ind',ind)
#print ('x ',x[ind])
#print ('y ',y[ind])
chxx = []
chyy = []
chzz = []
#chxx.append(ch2x[ind])
#chyy.append(ch2y[ind])
#chzz.append(ch2z[ind])
#print date[ind],x[ind],y[ind]

ind1 = date1.index(k)
print('ind1',ind1)

diff = ind1 - ind

print (diff)

mxx = []
myy = []
mzz = []
#mxx.append(mx[ind1])
#myy.append(my[ind1])
#mzz.append(mz[ind1])
launch = 1
end = 2500
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'marginLeft': 510, 'marginRight': 10, 'marginTop': -70, 'marginBottom': 0,
        'backgroundColor':'#FAD7A0',
        'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'
    }
}

#style={'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10, 
 #              'backgroundColor':'#F7FBFE',
  #             'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'})





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([

html.Div(id='intermediate-value', style={'display': 'none'}),
html.Div(id='intermediate-value1', style={'display': 'none'}),
	
    dcc.Graph(id='graph',style={'height':'90vh'},figure={
            'data': [
                go.Scatter(
                    #x=[0],
                    #y=[0],
                    #text='name',
                    #mode='lines',
                    #opacity=0.7,
                    #line=dict(width=2, color="blue"),
                )],'layout': go.Layout(
                xaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                yaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest' )
				 }
	),
dcc.Dropdown(
        id='my-dropdown',style={'height': '30px', 'width': '500px'},
        options=[
            {'label': 'START ', 'value': launch},
            {'label': 'RIGHT_NOW', 'value': ind},
            {'label': 'BURN_1', 'value': burn1},
            {'label': 'BURN_2', 'value': burn2},
            {'label': 'BURN_3', 'value': burn3},
            {'label': 'BURN_4', 'value': burn4},
            {'label': 'BURN_5', 'value': burn5},
            {'label': 'END', 'value': end}
        ],
        value= ind,clearable=False
    ),
	
dcc.Markdown(d("""
                **use dropdown for interaction**
            """)),
            html.Pre(id='click-data', style=styles['pre']),
dcc.Graph(id='graph1',figure={
            'data': [
                go.Scatter(
                    x=[0],
                    y=[0],
                    #text='name',
                    #mode='lines',
                    #opacity=0.7,
                    #line=dict(width=2, color="blue"),
                )],'layout': go.Layout(
                xaxis={'title': 'GDP Per Capita','showgrid':False,'zeroline': False},
                yaxis={'title': 'Life Expectancy','showgrid':False,'zeroline': False},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest' )
				 }
	),dcc.Markdown(d("""
                **CHANDRAYAAN-2**

                Use slider for interaction.
            """)),
            html.Pre(id='click-data1', style=styles['pre']), dcc.Slider(
        id='my-slider',
        
        min=0,
        max=slide,
        step=1,
        value=1,
        marks={
        burn1: {'label': 'burn1 at 56th pt', 'style': {'color': '#f50','margin-top':-40,'margin-left':30}},
        burn2: {'label': 'burn2 at 261th pt', 'style': {'color': '#f50'}},
        burn3: {'label': 'burn3 at 778th pt', 'style': {'color': '#f50'}},
        burn4: {'label': 'burn4 at 1355th pt', 'style': {'color': '#f50'}},
        burn5: {'label': 'burn at 1929th pt', 'style': {'color': '#f50'}},
        burn6: {'label': 'burn6 at 3075th pt', 'style': {'color': '#f50'}}
    }
    ),html.Div(id='slider-output-container',style={'margin-top': 20})  

])

#x = [1,2,3,4,5]
#y = [1,2,3,4,5]
@app.callback(Output('intermediate-value','children'),[Input('my-dropdown','value')])
def ch2(value):
    ind = date.index(k)
    print('ind:::',ind)
    return ind


@app.callback(Output('intermediate-value1','children'),[Input('my-dropdown','value')])
def moon(value):
    ind1 = date1.index(k)
    print('ind1:::',ind1)
    return ind1


    


@app.callback(
    Output('click-data', 'children'),
    [Input('my-dropdown', 'value')])
def display_click_data(value):
    dat = date[int(value)]
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
   
    # utc = datetime.utcnow()
    utc = datetime.strptime(dat[:-5], '%Y-%b-%d %H:%M:%S')
    # Tell the datetime object that it's in UTC time zone since 
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)
    # Convert time zone
    central = utc.astimezone(to_zone)
    ind = date.index(k)
    ind1 = date1.index(k)
    print('ind:',ind,'ind1:',ind1)
    cx = ch2x[value]
    cy = ch2y[value]
    cz = ch2z[value]
    cvx = chvx[value]
    cvy = chvy[value]
    cvz = chvz[value]
    print('cx:',cx,'cy:',cy,'cz:',cz,'vx',cvx,'vy',cvy,'vz',cvz)
    cr = math.sqrt(float(cx)*float(cx) + float(cy)*float(cy)+ float(cz)*float(cz))
    vl = math.sqrt(float(cvx)*float(cvx) + float(cvy)*float(cvy)+ float(cvz)*float(cvz))
    print ('cr:',cr,'vl',vl)
    lx = mx[int(value)+diff]
    ly = my[int(value)+diff]
    lz = mz[int(value)+diff]

    mvxx = mvx[int(value)+diff]
    mvyy = mvy[int(value)+diff]
    mvzz = mvz[int(value)+diff]
    
    ax = cx - lx
    ay = cy - ly
    az = cz - lz

    vxx = cvx - mvxx
    vyy = cvy - mvyy
    vzz = cvz - mvzz
    
    
    print('ax:',ax,'ay:',ay,'az:',az,'vx',mvxx,'vy',mvyy,'vz',mvzz)
    mr = math.sqrt(float(ax)*float(ax) + float(ay)*float(ay) + float(az)*float(az))
    mvl = math.sqrt(float(vxx)*float(vxx) + float(vyy)*float(vyy) + float(vzz)*float(vzz))
    print ('mr:',mr,'mvl',mvl)
    return str(central)+'\n'+'chandrayaan \n'+'Relative distance btw earth & ch2: '+str(cr)+' km\n'+ 'Relative distance btw moon & ch2: '+str(mr)+' km\n'+'velocity wrt Earth:'+str(vl)+'km/s\nvelocity wrt to moon:'+str(mvl)+'km/s\n'


#@app.callback(Output('graph', 'figure'), [Input('btn-1', 'n_clicks_timestamp')])
@app.callback(Output('graph', 'figure'),[Input('my-dropdown', 'value')])
def displayClick(value):


    burn_1 = '2019-Jul-24 09:20:00.0000'
    burn_2 = '2019-Jul-25 19:30:00.0000'    
    burn_3 = '2019-Jul-29 09:40:00.0000'
    burn_4 = '2019-Aug-02 09:50:00.0000'
    burn_5 = '2019-Aug-06 09:30:00.0000'
    burn_6 = '2019-Aug-14 08:30:00.0000'
    burn_66 ='2019-Aug-14 09:30:00.0000'

   
    burn1 = date.index(burn_1)  
    burn2 = date.index(burn_2)
    burn3 = date.index(burn_3)
    burn4 = date.index(burn_4)
    burn5 = date.index(burn_5)
    burn6 = date.index(burn_6)
    burn66 = date.index(burn_66)

    print('gburn1: ', date[burn1])
    print('gburn2: ', date[burn2])
    print('gburn3: ', date[burn3])
    print('gburn4: ', date[burn4])
    print('gburn5: ', date[burn5])


    tlix = []
    tliy = []

    for i in range(burn6,burn66):
        tlix.append(ch2x[i])
        tliy.append(ch2y[i])

    return {'data':[
                go.Scatter(
                    x=ch2x,
                    y=ch2y,
                    text='chandrayaan2 orbit',
                    name = 'Chandrayaan2 orbit',
                    #mode='lines',
                    #opacity=0.7,
                    #line=dict(width=2, color="blue"),
                    hoverinfo='text'
                ),
				go.Scatter(x=mx,y=my,mode='lines',text='moon orbit',name='Moon orbit',line=dict(width=2,color='orange'),hoverinfo='text'),
                
				go.Scatter(x=[ch2x[int(value)]],y=[ch2y[int(value)]],mode='markers',text = 'CH2',name='CH2',marker=dict(size=15,color='red'),hoverinfo='text'),
				go.Scatter(x=[mx[int(value)+diff]],y=[my[int(value)+diff]],mode='markers',text='Moon',name='Moon',marker=dict(size=15,color='purple'),hoverinfo='text'),
				go.Scatter(x=[0],y=[0],mode='markers',text='Earth',name='Earth',marker=dict(size=15,color='green')),
                go.Scatter(x=[ch2x[int(burn1)]],y=[ch2y[int(burn1)]],mode='markers',text = 'burn1 - 24.07.2019 (target orbit: 241.5 x 45162 km)',name='burn1',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn2)]],y=[ch2y[int(burn2)]],mode='markers',text = 'burn2 - 26.07.2019 (target orbit: 262.9 x 54848 km)',name='burn2',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn3)]],y=[ch2y[int(burn3)]],mode='markers',text = 'burn3 - 29.07.2019 (target orbit: 281.6 x 71341 km)',name='burn3',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn4)]],y=[ch2y[int(burn4)]],mode='markers',text = 'burn4 - 02.08.2019 (target orbit: 262.1 x 89743 km)',name='burn4',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn5)]],y=[ch2y[int(burn5)]],mode='markers',text = 'burn5 - 06.08.2019 (target orbit: 233.2 x 143953 km)',name='burn5',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=tlix,y=tliy,mode='lines',text = 'burn6 - 14.08.2019 (Trans lunar insertion(3:00pm - 4:00pm IST): 278.4 x 412505 km)',name='Trans lunar insertion',line=dict(width=2, color="red"),hoverinfo='text')
				],'layout': go.Layout(
                xaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                yaxis={'showgrid':False,'zeroline': False,'showticklabels':False},

				title = "CHANDRAYAAN-2",
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest' )
				}
@app.callback(
    Output('click-data1', 'children'),
    [Input('my-slider', 'value')])
def display_click_data(value):
    dat = date[int(value)]
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('IST')
    dd = '2019-Aug-09 17:40:00.0000'
    # utc = datetime.utcnow()
    utc = datetime.strptime(dat[:-5], '%Y-%b-%d %H:%M:%S')

    # Tell the datetime object that it's in UTC time zone since 
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)

    # Convert time zone
    central = utc.astimezone(to_zone)
    ind = date.index(k)
    ind1 = date1.index(k)
    print('ind:',ind,'ind1:',ind1)
    cx = ch2x[value]
    cy = ch2y[value]
    cz = ch2z[value]
    cvx = chvx[value]
    cvy = chvy[value]
    cvz = chvz[value]
    print('cx:',cx,'cy:',cy,'cz:',cz,'vx',cvx,'vy',cvy,'vz',cvz)
    cr = math.sqrt(float(cx)*float(cx) + float(cy)*float(cy)+ float(cz)*float(cz))
    vl = math.sqrt(float(cvx)*float(cvx) + float(cvy)*float(cvy)+ float(cvz)*float(cvz))
    print ('cr:',cr,'vl',vl)
    lx = mx[int(value)+diff]
    ly = my[int(value)+diff]
    lz = mz[int(value)+diff]

    mvxx = mvx[int(value)+diff]
    mvyy = mvy[int(value)+diff]
    mvzz = mvz[int(value)+diff]
    
    ax = cx - lx
    ay = cy - ly
    az = cz - lz

    vxx = cvx - mvxx
    vyy = cvy - mvyy
    vzz = cvz - mvzz
    
    
    print('ax:',ax,'ay:',ay,'az:',az,'vx',mvxx,'vy',mvyy,'vz',mvzz)
    mr = math.sqrt(float(ax)*float(ax) + float(ay)*float(ay) + float(az)*float(az))
    mvl = math.sqrt(float(vxx)*float(vxx) + float(vyy)*float(vyy) + float(vzz)*float(vzz))
    print ('mr:',mr,'mvl',mvl)
    return str(dat)+'\n'+'chandrayaan \n'+'Relative distance btw earth & ch2: '+str(cr)+' km\n'+ 'Relative distance btw moon & ch2: '+str(mr)+' km\n'+'velocity wrt Earth:'+str(vl)+'km/s\nvelocity wrt to moon:'+str(mvl)+'km/s\n'


@app.callback(Output('slider-output-container', 'children'),[Input('my-slider', 'value')])
def displayClick111(value):
    return 'You have selected "{}"'.format(value)

@app.callback(Output('graph1', 'figure'),[Input('my-slider', 'value')],[State('graph1', 'relayoutData')])
def displayClick(value,relayout_data):
    burn_1 = '2019-Jul-24 09:20:00.0000'
    burn_2 = '2019-Jul-25 19:30:00.0000'    
    burn_3 = '2019-Jul-29 09:40:00.0000'
    burn_4 = '2019-Aug-02 09:50:00.0000'
    burn_5 = '2019-Aug-06 09:30:00.0000'
    burn_6 = '2019-Aug-14 08:30:00.0000'
    burn_66 ='2019-Aug-14 09:30:00.0000'

   
    burn1 = date.index(burn_1)  
    burn2 = date.index(burn_2)
    burn3 = date.index(burn_3)
    burn4 = date.index(burn_4)
    burn5 = date.index(burn_5)
    burn6 = date.index(burn_6)
    burn66 = date.index(burn_66)

    print('sburn1: ', date[burn1],burn1)
    print('sburn2: ', date[burn2],burn2)
    print('sburn3: ', date[burn3],burn3)
    print('sburn4: ', date[burn4],burn4)
    print('sburn5: ', date[burn5],burn5)
    
    tlix = []
    tliy = []

    for i in range(burn6,burn66):
        tlix.append(ch2x[i])
        tliy.append(ch2y[i])

    return {'data':[
                go.Scatter(
                    x=ch2x,
                    y=ch2y,
                    text='Chandrayaan2',name='Chandrayaan2',hoverinfo='text'
                    #mode='lines',
                    #opacity=0.7,
                    #line=dict(width=2, color="blue"),
                ),
				go.Scatter(x=mx,y=my,mode='lines',text='Moon oribt',name='Moon orbit',line=dict(width=2,color='orange'),hoverinfo='text'),
				go.Scatter(x=[ch2x[int(value)]],y=[ch2y[int(value)]],text='CH2',name='CH2',mode='markers',marker=dict(size=15,color='red'),hoverinfo='text'),
				go.Scatter(x=[mx[int(value)+diff]],y=[my[int(value)+diff]],text='Moon',name='Moon',mode='markers',marker=dict(size=15,color='purple'),hoverinfo='text'),
				go.Scatter(x=[0],y=[0],text='Earth',name='Earth',mode='markers',marker=dict(size=15,color='green'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn1)]],y=[ch2y[int(burn1)]],mode='markers',text = 'burn1 - 24.07.2019 (target orbit: 241.5 x 45162 km)',name='burn1',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn2)]],y=[ch2y[int(burn2)]],mode='markers',text = 'burn2 - 26.07.2019 (target orbit: 262.9 x 54848 km)',name='burn2',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn3)]],y=[ch2y[int(burn3)]],mode='markers',text = 'burn3 - 29.07.2019 (target orbit: 281.6 x 71341 km)',name='burn3',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn4)]],y=[ch2y[int(burn4)]],mode='markers',text = 'burn4 - 02.08.2019 (target orbit: 262.1 x 89743 km)',name='burn4',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=[ch2x[int(burn5)]],y=[ch2y[int(burn5)]],mode='markers',text = 'burn5 - 06.08.2019 (target orbit: 233.2 x 143953 km)',name='burn5',marker=dict(size=5,color='red'),hoverinfo='text'),
                go.Scatter(x=tlix,y=tliy,mode='lines',text = 'burn6 - 14.08.2019 (Trans lunar insertion(3:00pm - 4:00pm IST): 278.4 x 412505 km)',name='Trans lunar insertion',line=dict(width=2, color="red"),hoverinfo='text')
				],'layout': go.Layout(
                xaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                yaxis={'showgrid':False,'zeroline': False,'showticklabels':False},

				title = "CHANDRAYAAN-2",
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest' )
				}



	 
			
if __name__ == '__main__':
    app.run_server(debug=True)
