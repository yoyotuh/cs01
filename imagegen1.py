# generate_images_part1.py
# Week 1–4: 16 diagrams
import os
from graphviz import Digraph

os.makedirs("images", exist_ok=True)
DPI = 150

def create_diagram(name, nodes, edges, **kwargs):
    dot = Digraph(name=name, format='png', engine='dot')
    dot.attr('graph', dpi=str(DPI), fontsize='12', rankdir=kwargs.get('rankdir', 'TB'),
             margin='0.1', nodesep='0.3', ranksep='0.4')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='11')
    dot.attr('edge', arrowhead='normal', fontname='Arial', fontsize='10')
    for nid, label, attrs in nodes:
        dot.node(nid, label, **attrs)
    for src, dst, lbl in edges:
        dot.edge(src, dst, lbl)
    dot.render(os.path.join("images", name), cleanup=True)
    print(f"✅ {name}.png")

# Week 1 (4)
create_diagram("week1-computational-thinking-components",
    [("D", "Decomposition", {"fillcolor": "#a8e6cf"}),
     ("P", "Pattern Recognition", {"fillcolor": "#dcedc1"}),
     ("A", "Abstraction", {"fillcolor": "#ffd3b6"}),
     ("Al", "Algorithm Design", {"fillcolor": "#ffaaa5"})],
    [("D", "P", ""), ("P", "A", ""), ("A", "Al", "")], rankdir="LR"
)
create_diagram("week1-algorithm-vs-program-flow",
    [("Prob", "Real World Problem", {}),
     ("Algo", "Algorithm Design", {}),
     ("Code", "Program Code", {}),
     ("Sol", "Solution", {})],
    [("Prob", "Algo", ""), ("Algo", "Code", ""), ("Code", "Sol", ""), ("Sol", "Prob", "Feedback")]
)
create_diagram("week1-basic-flowchart-boiling-egg",
    [("S", "Start", {"shape": "ellipse"}),
     ("F", "Fill pot with water", {}),
     ("E", "Add eggs", {}),
     ("B", "Boil water", {}),
     ("W", "Wait 7 minutes", {}),
     ("H", "Stop heat", {}),
     ("Ser", "Serve", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("S", "F", ""), ("F", "E", ""), ("E", "B", ""), ("B", "W", ""),
     ("W", "H", ""), ("H", "Ser", ""), ("Ser", "End", "")]
)
create_diagram("week1-first-python-program-memory",
    [("Code", "Python Code\n(print('Hi'))", {}),
     ("Mem", "Memory (State)", {"shape": "component"}),
     ("Exec", "Execution", {}),
     ("Out", "Output", {"shape": "parallelogram"})],
    [("Code", "Mem", ""), ("Mem", "Exec", ""), ("Exec", "Out", "")]
)

# Week 2 (4)
create_diagram("week2-memory-storage-diagram",
    [("age", "age = 21\nAddr: 0x100", {"shape": "record"}),
     ("name", "name = 'Sarah'\nAddr: 0x104", {"shape": "record"})],
    [], rankdir="LR"
)
create_diagram("week2-variable-container-analogy",
    [("box1", "Container: 'age'\nContents: 21", {"shape": "box3d", "fillcolor": "#c9c9ff"}),
     ("box2", "Container: 'name'\nContents: 'Sarah'", {"shape": "box3d", "fillcolor": "#ffc9c9"})],
    [], rankdir="LR"
)
create_diagram("week2-input-output-flowchart",
    [("In", "Input", {"shape": "parallelogram"}),
     ("Proc", "Process", {}),
     ("Out", "Output", {"shape": "parallelogram"})],
    [("In", "Proc", ""), ("Proc", "Out", "")]
)
create_diagram("week2-data-type-map",
    [("int", "int\n42", {"fillcolor": "#b3e5fc"}),
     ("float", "float\n3.14", {"fillcolor": "#b3e5fc"}),
     ("str", "str\n'hello'", {"fillcolor": "#d1c4e9"}),
     ("bool", "bool\nTrue", {"fillcolor": "#ffccbc"})],
    [], rankdir="LR"
)

# Week 3 (4)
create_diagram("week3-expression-order-diagram",
    [("P", "Parentheses ()", {"fillcolor": "#e1bee7"}),
     ("E", "Exponents **", {"fillcolor": "#e1bee7"}),
     ("MD", "Mul / Div\n*, /, //, %", {"fillcolor": "#bbdefb"}),
     ("AS", "Add / Sub\n+, -", {"fillcolor": "#bbdefb"})],
    [("P", "E", ""), ("E", "MD", ""), ("MD", "AS", "")]
)
create_diagram("week3-boolean-decision-tree",
    [("Start", "Start", {"shape": "ellipse"}),
     ("Q1", "age < 13?", {"shape": "diamond"}),
     ("Child", "Child", {}),
     ("Q2", "age < 20?", {"shape": "diamond"}),
     ("Teen", "Teenager", {}),
     ("Adult", "Adult", {})],
    [("Start", "Q1", ""), ("Q1", "Child", "Yes"), ("Q1", "Q2", "No"),
     ("Q2", "Teen", "Yes"), ("Q2", "Adult", "No")]
)
create_diagram("week3-if-else-flowchart",
    [("Start", "Start", {"shape": "ellipse"}),
     ("In", "Input number", {"shape": "parallelogram"}),
     ("Check", "Even?", {"shape": "diamond"}),
     ("Even", "Print 'Even'", {}),
     ("Odd", "Print 'Odd'", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("Start", "In", ""), ("In", "Check", ""), ("Check", "Even", "Yes"),
     ("Check", "Odd", "No"), ("Even", "End", ""), ("Odd", "End", "")]
)
create_diagram("week3-input-validation-flow",
    [("Start", "Start", {"shape": "ellipse"}),
     ("In", "Get input", {"shape": "parallelogram"}),
     ("Valid", "Valid?", {"shape": "diamond"}),
     ("Proc", "Process", {}),
     ("Err", "Show error", {"fillcolor": "#ffcdd2"}),
     ("End", "End", {"shape": "ellipse"})],
    [("Start", "In", ""), ("In", "Valid", ""), ("Valid", "Proc", "Yes"),
     ("Valid", "Err", "No"), ("Err", "In", ""), ("Proc", "End", "")]
)

# Week 4 (4)
create_diagram("week4-for-loop-flow",
    [("Init", "Initialize", {}),
     ("Cond", "More items?", {"shape": "diamond"}),
     ("Body", "Loop body", {}),
     ("Next", "Next item", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("Init", "Cond", ""), ("Cond", "Body", "Yes"), ("Body", "Next", ""),
     ("Next", "Cond", ""), ("Cond", "End", "No")]
)
create_diagram("week4-while-loop-flow",
    [("Cond", "Condition?", {"shape": "diamond"}),
     ("Body", "Body", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("Cond", "Body", "Yes"), ("Body", "Cond", ""), ("Cond", "End", "No")]
)
create_diagram("week4-accumulator-diagram",
    [("sum", "sum = 0", {}),
     ("i", "i = 1", {}),
     ("Loop", "i ≤ 5?", {"shape": "diamond"}),
     ("Add", "sum += i", {}),
     ("Inc", "i += 1", {}),
     ("Res", "sum = 15", {"shape": "parallelogram"})],
    [("sum", "i", ""), ("i", "Loop", ""), ("Loop", "Add", "Yes"),
     ("Add", "Inc", ""), ("Inc", "Loop", ""), ("Loop", "Res", "No")]
)
create_diagram("week4-infinite-loop-warning",
    [("Start", "Start", {"shape": "ellipse"}),
     ("Loop", "while True:", {"shape": "diamond", "fillcolor": "#ffcdd2"}),
     ("Body", "Do work", {}),
     ("Warn", "⚠️ No exit!", {"fillcolor": "#ff8a80"})],
    [("Start", "Loop", ""), ("Loop", "Body", "Yes"), ("Body", "Loop", ""),
     ("Loop", "Warn", "")]
)

print("✅ Part 1 (Week 1–4): 16 diagrams generated.")