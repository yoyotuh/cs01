# generate_images_part4.py
# Week 13–16: 12 diagrams
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

# Week 13 (3 diagrams)
create_diagram("week13-function-call-flow",
    [("Main", "main()", {}),
     ("Call", "greet('Ali')", {}),
     ("Exec", "Execute greet()\n(print 'Hello Ali')", {}),
     ("Return", "Return to main", {})],
    [("Main", "Call", ""), ("Call", "Exec", ""), ("Exec", "Return", "")]
)
create_diagram("week13-recursion-flow",
    [("f5", "fact(5)", {}),
     ("f4", "fact(4)", {}),
     ("f3", "fact(3)", {}),
     ("f2", "fact(2)", {}),
     ("f1", "fact(1) = 1", {"fillcolor": "#c8e6c9"}),
     ("r2", "2 * 1 = 2", {}),
     ("r3", "3 * 2 = 6", {}),
     ("r4", "4 * 6 = 24", {}),
     ("r5", "5 * 24 = 120", {})],
    [("f5", "f4", ""), ("f4", "f3", ""), ("f3", "f2", ""), ("f2", "f1", ""),
     ("f1", "r2", ""), ("r2", "r3", ""), ("r3", "r4", ""), ("r4", "r5", "")],
    rankdir="LR"
)
create_diagram("week13-modular-functions",
    [("Main", "main()", {}),
     ("Input", "get_user_input()", {"fillcolor": "#b3e5fc"}),
     ("Process", "process_data()", {"fillcolor": "#b3e5fc"}),
     ("Output", "display_results()", {"fillcolor": "#b3e5fc"})],
    [("Main", "Input", ""), ("Input", "Process", ""), ("Process", "Output", ""), ("Output", "Main", "Done")]
)

# Week 14 (3 diagrams)
create_diagram("week14-bubble-sort-flow",
    [("Start", "Start", {"shape": "ellipse"}),
     ("Outer", "i = 0 to n-2", {}),
     ("Inner", "j = 0 to n-i-2", {}),
     ("Compare", "arr[j] > arr[j+1]?", {"shape": "diamond"}),
     ("Swap", "Swap elements", {}),
     ("End", "Array sorted", {"shape": "ellipse"})],
    [("Start", "Outer", ""), ("Outer", "Inner", ""), ("Inner", "Compare", ""),
     ("Compare", "Swap", "Yes"), ("Swap", "Inner", ""), ("Compare", "Outer", "No"),
     ("Outer", "End", "Finished")]
)
create_diagram("week14-selection-sort-flow",
    [("Start", "Start", {"shape": "ellipse"}),
     ("Outer", "i = 0 to n-1", {}),
     ("FindMin", "Find index of min\nin arr[i..n-1]", {}),
     ("Swap", "Swap arr[i] with min", {}),
     ("End", "Array sorted", {"shape": "ellipse"})],
    [("Start", "Outer", ""), ("Outer", "FindMin", ""), ("FindMin", "Swap", ""),
     ("Swap", "Outer", "Next i"), ("Outer", "End", "Done")]
)
create_diagram("week14-combined-problem-flow",
    [("Input", "Read input data", {}),
     ("Validate", "Validate input", {}),
     ("Search", "Search for target", {}),
     ("Count", "Count occurrences", {}),
     ("Sort", "Sort results", {}),
     ("Output", "Display final output", {})],
    [("Input", "Validate", ""), ("Validate", "Search", ""), ("Search", "Count", ""),
     ("Count", "Sort", ""), ("Sort", "Output", "")]
)

# Week 15 (3 diagrams)
create_diagram("week15-binary-search-flow",
    [("Start", "Sorted list", {}),
     ("Init", "low = 0, high = n-1", {}),
     ("Loop", "low ≤ high?", {"shape": "diamond"}),
     ("Mid", "mid = (low+high)//2", {}),
     ("Equal", "arr[mid] == target?", {"shape": "diamond"}),
     ("Less", "target < arr[mid]?", {"shape": "diamond"}),
     ("High", "high = mid - 1", {}),
     ("Low", "low = mid + 1", {}),
     ("Found", "Return mid", {}),
     ("NotFound", "Return -1", {})],
    [("Start", "Init", ""), ("Init", "Loop", ""), ("Loop", "Mid", "Yes"),
     ("Mid", "Equal", ""), ("Equal", "Found", "Yes"), ("Equal", "Less", "No"),
     ("Less", "High", "Yes"), ("Less", "Low", "No"),
     ("High", "Loop", ""), ("Low", "Loop", ""), ("Loop", "NotFound", "No")]
)
create_diagram("week15-recursive-sum-flow",
    [("Call", "sum_list([1,2,3])", {}),
     ("Base", "Empty?", {"shape": "diamond"}),
     ("Recur", "1 + sum_list([2,3])", {}),
     ("Base2", "Empty?", {"shape": "diamond"}),
     ("Recur2", "2 + sum_list([3])", {}),
     ("Base3", "Empty?", {"shape": "diamond"}),
     ("Recur3", "3 + sum_list([])", {}),
     ("Base4", "Empty → return 0", {"fillcolor": "#c8e6c9"}),
     ("Result", "6", {"shape": "parallelogram"})],
    [("Call", "Base", ""), ("Base", "Recur", "No"), ("Recur", "Base2", ""),
     ("Base2", "Recur2", "No"), ("Recur2", "Base3", ""), ("Base3", "Recur3", "No"),
     ("Recur3", "Base4", ""), ("Base4", "Result", "Unwind stack")]
)
create_diagram("week15-merge-sort-flow",
    [("Array", "Unsorted Array", {}),
     ("Split", "Split into halves", {}),
     ("Left", "Sort Left Half", {}),
     ("Right", "Sort Right Half", {}),
     ("Merge", "Merge Sorted Halves", {}),
     ("Sorted", "Fully Sorted Array", {})],
    [("Array", "Split", ""), ("Split", "Left", ""), ("Split", "Right", ""),
     ("Left", "Merge", ""), ("Right", "Merge", ""), ("Merge", "Sorted", "")]
)

# Week 16 (3 diagrams)
create_diagram("week16-capstone-data-flow",
    [("UI", "User Interface\n(CLI/Web)", {}),
     ("Engine", "Core Engine\n(Search, Sort, Stats)", {}),
     ("Data", "Data Storage\n(CSV/JSON files)", {}),
     ("Viz", "Visualizations\n(Charts/Reports)", {})],
    [("UI", "Engine", ""), ("Engine", "Data", "Read/Write"), ("Data", "Engine", ""),
     ("Engine", "Viz", ""), ("Viz", "UI", "Display")]
)
create_diagram("week16-capstone-function-interaction",
    [("Main", "main()", {}),
     ("Load", "load_dataset()", {"fillcolor": "#b3e5fc"}),
     ("Search", "perform_search()", {"fillcolor": "#b3e5fc"}),
     ("Count", "count_matches()", {"fillcolor": "#b3e5fc"}),
     ("Report", "generate_summary()", {"fillcolor": "#b3e5fc"})],
    [("Main", "Load", ""), ("Load", "Search", ""), ("Search", "Count", ""),
     ("Count", "Report", ""), ("Report", "Main", "Return results")]
)
create_diagram("week16-capstone-algorithm-flow",
    [("Input", "User query\n(e.g., 'count A grades')", {}),
     ("Prep", "Preprocess dataset", {}),
     ("Algo", "Run algorithms:\n- Search\n- Count\n- Sort", {}),
     ("Post", "Post-process results", {}),
     ("Output", "Return final answer", {})],
    [("Input", "Prep", ""), ("Prep", "Algo", ""), ("Algo", "Post", ""), ("Post", "Output", "")]
)

print("✅ Part 4 (Week 13–16): 12 diagrams generated.")