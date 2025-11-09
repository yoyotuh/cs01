# generate_images_part2.py
# Week 5–8: 14 diagrams
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

# Week 5 (3 diagrams)
create_diagram("week5-function-structure",
    [("Def", "def greet(name):", {"shape": "note"}),
     ("Doc", '    """Docstring"""', {"shape": "note"}),
     ("Body", "    print(...)", {"shape": "note"}),
     ("Ret", "    return", {"shape": "note"})],
    [("Def", "Doc", ""), ("Doc", "Body", ""), ("Body", "Ret", "")]
)
create_diagram("week5-parameters-arguments",
    [("Param", "Parameters\n(def time(h, m))", {"fillcolor": "#c8e6c9"}),
     ("Arg", "Arguments\n(time(9, 30))", {"fillcolor": "#ffcdd2"})],
    [("Param", "Arg", "Values passed at call")], rankdir="LR"
)
create_diagram("week5-local-global-variables",
    [("Global", "x = 10\n# global", {"fillcolor": "#bbdefb"}),
     ("Func", "def f():\n    x = 20\n    # local", {"fillcolor": "#c8e6c9"}),
     ("Access", "Global x=10\nLocal x=20", {})],
    [("Global", "Func", ""), ("Func", "Access", "")]
)

# Week 6 (3 diagrams)
create_diagram("week6-list-tuple-comparison",
    [("List", "List []\nMutable", {"fillcolor": "#b3e5fc"}),
     ("Tuple", "Tuple ()\nImmutable", {"fillcolor": "#d1c4e9"})],
    [], rankdir="LR"
)
create_diagram("week6-sequence-indexing",
    [("Seq", '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
      <TR><TD>0</TD><TD>1</TD><TD>2</TD><TD>3</TD><TD>4</TD><TD>5</TD></TR>
      <TR><TD>P</TD><TD>y</TD><TD>t</TD><TD>h</TD><TD>o</TD><TD>n</TD></TR>
      <TR><TD>-6</TD><TD>-5</TD><TD>-4</TD><TD>-3</TD><TD>-2</TD><TD>-1</TD></TR>
    </TABLE>
    >''', {"shape": "none"})],
    []
)
create_diagram("week6-string-slicing-flow",
    [("s", "s = 'abcdef'", {}),
     ("s1", "s[1:4] → 'bcd'", {"fillcolor": "#e8f5e9"}),
     ("s2", "s[-3:] → 'def'", {"fillcolor": "#e8f5e9"}),
     ("s3", "s[::2] → 'ace'", {"fillcolor": "#e8f5e9"})],
    [("s", "s1", ""), ("s", "s2", ""), ("s", "s3", "")], rankdir="TB"
)

# Week 7 (3 diagrams)
create_diagram("week7-dictionary-key-value",
    [("D", "student = {'name':'Ali', 'age':20}", {"shape": "component"}),
     ("K", "Keys: 'name', 'age'", {"fillcolor": "#d1c4e9"}),
     ("V", "Values: 'Ali', 20", {"fillcolor": "#b3e5fc"})],
    [("D", "K", ""), ("D", "V", "")]
)
create_diagram("week7-set-operations",
    [("A", "A = {1,2,3}", {}),
     ("B", "B = {2,3,4}", {}),
     ("U", "A ∪ B = {1,2,3,4}", {"fillcolor": "#c8e6c9"}),
     ("I", "A ∩ B = {2,3}", {"fillcolor": "#ffecb3"}),
     ("D", "A - B = {1}", {"fillcolor": "#ffcdd2"})],
    [("A", "U", ""), ("B", "U", ""), ("A", "I", ""), ("B", "I", ""),
     ("A", "D", ""), ("B", "D", "")]
)
create_diagram("week7-dictionary-counting",
    [("Start", "words = ['a','b','a']", {}),
     ("Init", "counts = {}", {}),
     ("Loop", "For word?", {"shape": "diamond"}),
     ("In", "word in counts?", {"shape": "diamond"}),
     ("Add", "counts[word] = 1", {}),
     ("Inc", "counts[word] += 1", {}),
     ("End", "counts = {'a':2, 'b':1}", {"shape": "parallelogram"})],
    [("Start", "Init", ""), ("Init", "Loop", ""), ("Loop", "In", "Yes"),
     ("In", "Inc", "Yes"), ("In", "Add", "No"), ("Add", "Loop", ""),
     ("Inc", "Loop", ""), ("Loop", "End", "No")]
)

# Week 8 (4 diagrams)
create_diagram("week8-file-read-write",
    [("W", "open('f','w')", {}),
     ("Write", "write(...)", {}),
     ("C1", "close()", {}),
     ("R", "open('f','r')", {}),
     ("Read", "read()", {}),
     ("C2", "close()", {})],
    [("W", "Write", ""), ("Write", "C1", ""), ("C1", "R", ""),
     ("R", "Read", ""), ("Read", "C2", "")]
)
create_diagram("week8-with-context",
    [("With", "with open('f') as f:", {}),
     ("Body", "    data = f.read()", {}),
     ("Auto", "✅ Auto-closed", {"fillcolor": "#c8e6c9"})],
    [("With", "Body", ""), ("Body", "Auto", "")]
)
create_diagram("week8-exception-flow",
    [("Try", "try:", {"shape": "note"}),
     ("Code", "    risky()", {"shape": "note"}),
     ("Ex", "except Error:", {"shape": "note"}),
     ("Handle", "    fix()", {"shape": "note"}),
     ("Fin", "finally:", {"shape": "note"}),
     ("Clean", "    cleanup()", {"shape": "note"})],
    [("Try", "Code", ""), ("Code", "Ex", "Error?"), ("Ex", "Handle", ""),
     ("Handle", "Fin", ""), ("Code", "Fin", "No error"), ("Fin", "Clean", "")]
)
# Week 8 - CSV Flow
create_diagram("week8-csv-data-flow",
    [("CSV", "Read CSV file", {}),
     ("Parse", "Parse → list of dicts", {}),
     ("Process", "Process data\n(filter, compute)", {}),
     ("Output", "Write/Display results", {})],
    [("CSV", "Parse", ""), ("Parse", "Process", ""), ("Process", "Output", "")]
)

print("✅ Part 2 (Week 5–8): 14 diagrams generated.")