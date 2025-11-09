# generate_images_part5.py
# Additional Diagrams (5): Complete the set to 58
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

# Helper for alternative Big-O plot
def plot_big_o_alt(filename, title):
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(1, 20, 300)
    plt.figure(figsize=(6, 4), dpi=DPI)
    plt.plot(x, np.log(x), label='O(log n)', linewidth=2, color='#1f77b4')
    plt.plot(x, x, label='O(n)', linewidth=2, color='#ff7f0e')
    plt.plot(x, x * np.log(x), label='O(n log n)', linewidth=2, color='#2ca02c')
    plt.plot(x, x**2, label='O(n²)', linewidth=2, color='#d62728')
    plt.plot(x, x**3, label='O(n³)', linewidth=2, color='#9467bd')
    plt.ylim(0, 100)
    plt.title(title, fontsize=13)
    plt.xlabel('Input Size (n)', fontsize=11)
    plt.ylabel('Time Complexity', fontsize=11)
    plt.legend(fontsize=9)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join("images", filename), dpi=DPI)
    plt.close()

# 54. Computational Thinking Overview
create_diagram("week1-computational-thinking",
    [("CT", "Computational Thinking:\n• Decompose problems\n• Recognize patterns\n• Abstract details\n• Design algorithms", {})],
    []
)

# 55. Variables & Types Overview
create_diagram("week2-variables-types",
    [("VT", "Variables & Data Types:\n• Variables: named containers\n• Types: int, float, str, bool\n• Dynamic typing in Python", {})],
    []
)

# 56. Conditions & Loops Integration
create_diagram("week3-conditions-loops",
    [("CL", "Control Flow:\n• if/elif/else → decision making\n• for/while → repetition\n• Combined: e.g., validate input in loop", {})],
    []
)

# 57. Simple Calculator Workflow
create_diagram("week4-simple-calculator",
    [("Start", "Start", {"shape": "ellipse"}),
     ("Input", "Input: num1, operator, num2", {"shape": "parallelogram"}),
     ("Op", "operator == '+'?", {"shape": "diamond"}),
     ("Add", "result = num1 + num2", {}),
     ("Sub", "result = num1 - num2", {}),
     ("Mul", "result = num1 * num2", {}),
     ("Div", "result = num1 / num2", {}),
     ("Output", "Display result", {"shape": "parallelogram"}),
     ("End", "End", {"shape": "ellipse"})],
    [("Start", "Input", ""), ("Input", "Op", ""),
     ("Op", "Add", "+"), ("Op", "Sub", "−"),
     ("Op", "Mul", "×"), ("Op", "Div", "÷"),
     ("Add", "Output", ""), ("Sub", "Output", ""),
     ("Mul", "Output", ""), ("Div", "Output", ""),
     ("Output", "End", "")]
)

# 58. Alternative Big-O Growth (UNIQUE NAME to avoid overwrite)
plot_big_o_alt("week11-bigO-growth-alt.png", "Big-O Complexity: Growth Comparison (Enhanced)")

print("✅ Part 5 (Additional): 5 diagrams generated.")
print("🎉 Total: 58 unique PNG files in 'images/' folder.")