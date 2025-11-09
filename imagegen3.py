# generate_images_part3.py
# Week 9–12: 12 diagrams
import os
from graphviz import Digraph

# Buat folder output
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

# Helper untuk Big-O (Week 11)
def plot_big_o(filename, title):
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(1, 15, 200)
    plt.figure(figsize=(6, 4), dpi=DPI)
    plt.plot(x, np.log2(x), label='O(log n)', linewidth=2)
    plt.plot(x, x, label='O(n)', linewidth=2)
    plt.plot(x, x * np.log2(x), label='O(n log n)', linewidth=2)
    plt.plot(x, x**2, label='O(n²)', linewidth=2)
    plt.ylim(0, 50)
    plt.title(title, fontsize=13)
    plt.xlabel('n', fontsize=11)
    plt.ylabel('Relative Time', fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join("images", filename), dpi=DPI)
    plt.close()

# Week 9 (3 diagrams)
create_diagram("week9-algorithm-flowchart",
    [("Prob", "Real-World Problem", {"shape": "ellipse"}),
     ("Understand", "1. Understand Problem", {}),
     ("Plan", "2. Plan Solution\n(Pseudocode/Flowchart)", {}),
     ("Design", "3. Design Algorithm", {}),
     ("Test", "4. Test with Examples", {}),
     ("Refine", "5. Refine?", {"shape": "diamond"}),
     ("Code", "6. Implement in Code", {}),
     ("Done", "Working Program", {"shape": "ellipse"})],
    [("Prob", "Understand", ""), ("Understand", "Plan", ""), ("Plan", "Design", ""),
     ("Design", "Test", ""), ("Test", "Refine", ""), ("Refine", "Design", "Yes"),
     ("Refine", "Code", "No"), ("Code", "Done", "")]
)
create_diagram("week9-problem-solving-steps",
    [("I", "1. Identify Input & Output", {}),
     ("D", "2. Decompose Problem", {}),
     ("P", "3. Find Patterns", {}),
     ("A", "4. Create Algorithm", {}),
     ("V", "5. Validate with Tests", {})],
    [("I", "D", ""), ("D", "P", ""), ("P", "A", ""), ("A", "V", "")]
)
create_diagram("week9-counting-algorithm",
    [("Start", "Count occurrences\nin a list", {"shape": "ellipse"}),
     ("Init", "count = 0", {}),
     ("Loop", "Next item?", {"shape": "diamond"}),
     ("Match", "item == target?", {"shape": "diamond"}),
     ("Inc", "count += 1", {}),
     ("End", "Return count", {"shape": "parallelogram"})],
    [("Start", "Init", ""), ("Init", "Loop", ""), ("Loop", "Match", "Yes"),
     ("Match", "Inc", "Yes"), ("Inc", "Loop", ""), ("Match", "Loop", "No"),
     ("Loop", "End", "No")]
)

# Week 10 (3 diagrams)
create_diagram("week10-linear-search-flow",
    [("Start", "Start", {"shape": "ellipse"}),
     ("i", "i = 0", {}),
     ("Cond", "i < len(list)?", {"shape": "diamond"}),
     ("Match", "list[i] == target?", {"shape": "diamond"}),
     ("Found", "Return i", {}),
     ("Inc", "i = i + 1", {}),
     ("Not", "Not found", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("Start", "i", ""), ("i", "Cond", ""), ("Cond", "Match", "Yes"),
     ("Match", "Found", "Yes"), ("Match", "Inc", "No"), ("Inc", "Cond", ""),
     ("Cond", "Not", "No"), ("Found", "End", ""), ("Not", "End", "")]
)
create_diagram("week10-counting-elements",
    [("List", "List: [a, b, a, c]", {}),
     ("Init", "count = 0", {}),
     ("Loop", "For each x", {"shape": "diamond"}),
     ("Check", "x == 'a'?", {"shape": "diamond"}),
     ("Add", "count += 1", {}),
     ("Result", "count = 2", {"shape": "parallelogram"})],
    [("List", "Init", ""), ("Init", "Loop", ""), ("Loop", "Check", "Yes"),
     ("Check", "Add", "Yes"), ("Add", "Loop", ""), ("Check", "Loop", "No"),
     ("Loop", "Result", "No")]
)
create_diagram("week10-frequency-dictionary",
    [("Start", "words = ['a','b','a']", {}),
     ("Dict", "freq = {}", {}),
     ("Loop", "For word", {"shape": "diamond"}),
     ("In", "word in freq?", {"shape": "diamond"}),
     ("Set", "freq[word] = 1", {}),
     ("Up", "freq[word] += 1", {}),
     ("End", "freq = {'a':2, 'b':1}", {"shape": "parallelogram"})],
    [("Start", "Dict", ""), ("Dict", "Loop", ""), ("Loop", "In", "Yes"),
     ("In", "Up", "Yes"), ("In", "Set", "No"), ("Set", "Loop", ""),
     ("Up", "Loop", ""), ("Loop", "End", "No")]
)

# Week 11 (3 diagrams)
plot_big_o("week11-bigO-growth.png", "Algorithm Complexity Growth (Big-O)")
create_diagram("week11-loop-comparison",
    [("Single", "Single Loop:\nfor i in range(n)\n→ O(n)", {"fillcolor": "#b3e5fc"}),
     ("Nested", "Nested Loop:\nfor i in range(n):\n  for j in range(n)\n→ O(n²)", {"fillcolor": "#ffcdd2"})],
    [], rankdir="LR"
)
create_diagram("week11-optimization-flow",
    [("Slow", "Before:\nCheck all items\n(inefficient)", {"fillcolor": "#ffcdd2"}),
     ("Fast", "After:\nEarly exit / Use dict\n(optimized)", {"fillcolor": "#c8e6c9"})],
    [("Slow", "Fast", "Apply optimization")], rankdir="LR"
)

# Week 12 (3 diagrams)
create_diagram("week12-project-data-flow",
    [("In", "Input: Student Grades (CSV)", {}),
     ("Load", "Load Data into Memory", {}),
     ("Analyze", "Compute:\n- Average\n- Max/Min\n- Pass/Fail", {}),
     ("Report", "Generate Summary Report", {}),
     ("Out", "Display or Save Results", {})],
    [("In", "Load", ""), ("Load", "Analyze", ""), ("Analyze", "Report", ""), ("Report", "Out", "")]
)
create_diagram("week12-function-interaction",
    [("Main", "main()", {}),
     ("Read", "read_grades_file()", {"fillcolor": "#b3e5fc"}),
     ("Stats", "calculate_stats()", {"fillcolor": "#b3e5fc"}),
     ("Report", "generate_report()", {"fillcolor": "#b3e5fc"})],
    [("Main", "Read", ""), ("Read", "Stats", ""), ("Stats", "Report", ""), ("Report", "Main", "Return")]
)
create_diagram("week12-search-count-flow",
    [("Input", "Enter student name", {"shape": "parallelogram"}),
     ("Search", "Linear search in list", {}),
     ("Found", "Found?", {"shape": "diamond"}),
     ("Count", "Count grades", {}),
     ("Show", "Display count", {}),
     ("NotFound", "Student not found", {}),
     ("End", "End", {"shape": "ellipse"})],
    [("Input", "Search", ""), ("Search", "Found", ""), ("Found", "Count", "Yes"),
     ("Count", "Show", ""), ("Show", "End", ""), ("Found", "NotFound", "No"), ("NotFound", "End", "")]
)

print("✅ Part 3 (Week 9–12): 12 diagrams generated.")