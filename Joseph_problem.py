import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Zvolte požadovaný počet vojáků!"),
    html.Div(["Počet vojáků: ",
              dcc.Input(id='my-input', value='', type='number'),
               html.Button(id='submit-button-state', n_clicks=0, children='Submit')]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='submit-button-state', component_property='n_clicks'),
    State(component_id='my-input', component_property='value'),
)
def update_output_div(click, n):
    while True:
        group = create_group(n)
        # group.print_list()
        killing_spree(group)
        break
    tr = group.return_value()
    pr = "Poslední přeživší je: " + str(tr)
    return pr


class JosephsProblem:
    def __init__(self, data):
        self.data = data
        self.next = None
       
class CircularList:
    def __init__(self):
        self.head = None

    def push(self, data):
        nmb = JosephsProblem(data)
        temp = self.head

        nmb.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = nmb
        else:
            nmb.next = nmb

        self.head = nmb

    def print_list(self):
        temp = self.head
        txt=""
        if self.head is not None:
            while(True):
                txt += str(temp.data)
                temp = temp.next
                txt += "->"
                if (temp == self.head):
                    break
        print(txt)

    def len_list(self):
        counter=0
        temp = self.head
        if self.head is not None:
            while(True):
                temp = temp.next
                counter +=1
                if (temp == self.head):
                    break
        return counter

    def return_value(self):
        return self.head.data

    def remove(self, index):
        index-=1
        current = self.head
        prev = None

        if current.next == self.head and current == self.head:
            pass
        for i in range(index):         
            prev = current
            current = current.next
        if current == self.head:
            self.head = current.next
            prev.next = self.head
        elif current.next == self.head:
            prev.next = self.head
        else:  
            prev.next = current.next

def create_group(n):
    cllist = CircularList()
    for i in range(1,n+1):
        cllist.push(n+1-i)
    return cllist

def killing_spree(group):
    index = 2
    remove = 0
    while group.len_list() != 1:
        if group.len_list() <= remove:
            index = 2
            remove =0
        group.remove(index)
        remove +=1
        #group.print_list()
        index += 1
    # group.print_list()


if __name__ == '__main__':
    app.run_server(debug=True)
    
        
    


