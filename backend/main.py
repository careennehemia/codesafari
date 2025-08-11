from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import json
from typing import List, Dict, Optional
import uvicorn
import re

# Load environment variables
load_dotenv()

app = FastAPI(title="CodeSafari 101 API", description="Backend for CodeSafari 101 learning platform")

# CORS middleware to allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Pydantic models
class ChatRequest(BaseModel):
    question: str
    lab_id: str
    skill: str

class ChatResponse(BaseModel):
    response: str
    relevant: bool
    sources: Optional[List[str]] = None

class LabManager:
    def __init__(self):
        self.labs = self.load_lab_content()
    
    def load_lab_content(self) -> Dict:
        """Load comprehensive lab content for all skills"""
        return {
            "python": {
                "python-basics": {
                    "title": "Python Fundamentals & Data Structures",
                    "reading": """
# Python Fundamentals & Data Structures

## Chapter 1: Lists - Python's Most Versatile Data Structure

Lists are ordered, mutable collections that can store any type of data. They are one of the most important data structures in Python programming.

### 1.1 List Methods and Operations

Python lists come with powerful built-in methods:

**Adding Elements:**
- `append(x)`: Add item to end of list
- `extend(iterable)`: Add all items from iterable to list
- `insert(i, x)`: Insert item at given position

**Removing Elements:**
- `remove(x)`: Remove first occurrence of x
- `pop(i)`: Remove and return item at position i (last if no index)
- `clear()`: Remove all items from list

**Search and Count:**
- `index(x)`: Return index of first occurrence of x
- `count(x)`: Return number of times x appears in list

**Sorting and Reversing:**
- `sort()`: Sort items in place
- `reverse()`: Reverse elements in place
- `copy()`: Return shallow copy of list

### 1.2 Advanced List Techniques

**List Slicing:**
```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[1:4])      # ['banana', 'cherry', 'date']
print(fruits[::-1])     # Reverse the list
print(fruits[::2])      # Every second element
```

**List Comprehensions:**
A concise way to create lists based on existing lists:
```python
# Traditional approach
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# List comprehension (more Pythonic)
squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

**Nested List Comprehensions:**
```python
# Create a 3x4 matrix
matrix = [[i*j for j in range(4)] for i in range(3)]
# Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
```

### 1.3 Using Lists as Stacks and Queues

**Stack (LIFO - Last In, First Out):**
```python
stack = [3, 4, 5]
stack.append(6)    # Push
stack.append(7)    # Push
print(stack.pop()) # Pop: returns 7
# Stack is now [3, 4, 5, 6]
```

**Queue (FIFO - First In, First Out):**
For queues, use `collections.deque` for efficiency:
```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")     # Add to right
queue.append("Graham")    # Add to right
queue.popleft()           # Remove from left: 'Eric'
```

## Chapter 2: Dictionaries - Key-Value Powerhouses

Dictionaries are unordered collections of key-value pairs. They provide fast lookups and are essential for many algorithms.

### 2.1 Dictionary Fundamentals

**Creating Dictionaries:**
```python
# Various ways to create dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
tel3 = dict(sape=4139, guido=4127, jack=4098)
tel4 = {x: x**2 for x in (2, 4, 6)}  # Dict comprehension
```

**Dictionary Operations:**
```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127        # Add new key-value pair
print(tel['jack'])         # Access value: 4098
del tel['sape']            # Delete key-value pair
print(list(tel))           # Get all keys: ['jack', 'guido']
print('guido' in tel)      # Check membership: True
```

### 2.2 Advanced Dictionary Techniques

**Dictionary Methods:**
- `keys()`: Return view of dictionary's keys
- `values()`: Return view of dictionary's values  
- `items()`: Return view of dictionary's key-value pairs
- `get(key, default)`: Return value for key, or default if not found
- `setdefault(key, default)`: Get value or set and return default
- `update(other)`: Update dictionary with key-value pairs from other

**Iterating Through Dictionaries:**
```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# Iterate over keys and values
for k, v in knights.items():
    print(k, v)

# Iterate with enumerate for position
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

### 2.3 Sets - Unique Collections

Sets are unordered collections with no duplicate elements, perfect for membership testing and mathematical operations.

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'orange', 'banana', 'pear', 'apple'} - duplicates removed

# Set operations
a = set('abracadabra')
b = set('alacazam')
print(a - b)    # Letters in a but not b: {'r', 'd', 'b'}
print(a | b)    # Letters in a or b: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)    # Letters in both a and b: {'a', 'c'}
print(a ^ b)    # Letters in a or b but not both: {'r', 'd', 'b', 'm', 'z', 'l'}
```

## Chapter 3: Algorithm Complexity Analysis

### 3.1 Big O Notation
Understanding algorithm efficiency is crucial for writing scalable code:

- **O(1) - Constant Time**: Dictionary lookups, array access by index
- **O(log n) - Logarithmic Time**: Binary search, balanced tree operations
- **O(n) - Linear Time**: Linear search, single loop through data
- **O(n log n) - Linearithmic Time**: Efficient sorting algorithms (merge sort, heap sort)
- **O(n²) - Quadratic Time**: Nested loops, bubble sort
- **O(2ⁿ) - Exponential Time**: Recursive algorithms without memoization

### 3.2 Space Complexity
Consider memory usage alongside time complexity:
- **In-place algorithms**: O(1) extra space
- **Recursive algorithms**: O(n) space for call stack
- **Dynamic programming**: Often trades space for time efficiency

### 3.3 Practical Performance Tips
1. Use dictionaries for fast lookups instead of lists
2. Prefer list comprehensions over explicit loops
3. Use `collections.deque` for queue operations
4. Consider `set` for membership testing with large datasets
5. Profile your code to identify actual bottlenecks
                    """,
                    "exercises": [
                        "Implement a function to find all duplicates in a list using both O(n²) and O(n) approaches",
                        "Create a comprehensive word frequency analyzer that handles punctuation and case sensitivity",
                        "Build an LRU (Least Recently Used) cache using OrderedDict with get/put operations",
                        "Implement a spell checker using sets for fast word lookup",
                        "Create a student grade book with statistical analysis (mean, median, mode, standard deviation)"
                    ],
                    "lab_description": "Build a comprehensive student management system with grade analysis, statistical reporting, and data visualization. Implement efficient algorithms for searching, sorting, and analyzing student performance data."
                },
                "python-algorithms": {
                    "title": "Graph Algorithms & BFS/DFS",
                    "reading": """
# Graph Algorithms: Breadth-First Search and Depth-First Search

## Chapter 1: Graph Theory Fundamentals

### 1.1 What are Graphs?
A graph is a collection of vertices (nodes) connected by edges. Graphs model relationships between objects and are fundamental to computer science.

**Types of Graphs:**
- **Undirected Graph**: Edges have no direction (friendship networks)
- **Directed Graph**: Edges have direction (web page links, Twitter follows)
- **Weighted Graph**: Edges have associated costs/weights (road networks with distances)
- **Unweighted Graph**: All edges are equal (simple connections)

### 1.2 Graph Representation

**1. Adjacency List (Recommended)**
```python
# More memory efficient for sparse graphs
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

**2. Adjacency Matrix**
```python
# Better for dense graphs, O(1) edge lookup
# 0 = no edge, 1 = edge exists
matrix = [
    [0, 1, 1, 0, 0, 0],  # A connects to B, C
    [1, 0, 0, 1, 1, 0],  # B connects to A, D, E
    [1, 0, 0, 0, 0, 1],  # C connects to A, F
    [0, 1, 0, 0, 0, 0],  # D connects to B
    [0, 1, 0, 0, 0, 1],  # E connects to B, F
    [0, 0, 1, 0, 1, 0]   # F connects to C, E
]
```

## Chapter 2: Breadth-First Search (BFS)

BFS explores vertices level by level, visiting all neighbors before moving to the next level. It uses a queue data structure.

### 2.1 BFS Algorithm

**Core Algorithm:**
1. Create a queue and add the starting vertex
2. Mark the starting vertex as visited
3. While the queue is not empty:
   - Dequeue a vertex from the front
   - Process the vertex
   - For each unvisited neighbor:
     - Mark neighbor as visited
     - Add neighbor to the back of the queue

**Python Implementation:**
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Visit all unvisited neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Example usage
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [1, 2]
}

print("BFS traversal:", bfs(graph, 0))
# Output: [0, 1, 2, 3]
```

### 2.2 BFS for Shortest Path

BFS naturally finds the shortest path in unweighted graphs:

```python
def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found
```

### 2.3 BFS Applications

1. **Shortest Path in Unweighted Graphs**: Find minimum number of edges
2. **Level-Order Tree Traversal**: Process tree nodes level by level
3. **Connected Components**: Find all connected parts of a graph
4. **Bipartite Graph Testing**: Check if graph can be colored with two colors
5. **Web Crawling**: Systematically explore web pages
6. **Social Network Analysis**: Find degrees of separation

## Chapter 3: Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking. It can be implemented recursively or with a stack.

### 3.1 DFS Algorithm

**Recursive Implementation:**
```python
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    result = [vertex]
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result
```

**Iterative Implementation (using stack):**
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse order for consistent traversal)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

### 3.2 DFS Applications

1. **Cycle Detection**: Find if graph contains cycles
2. **Topological Sorting**: Order vertices in directed acyclic graphs
3. **Path Finding**: Find any path between two vertices
4. **Connected Components**: Identify separate graph components
5. **Maze Solving**: Navigate through maze paths
6. **Dependency Resolution**: Resolve build dependencies

### 3.3 Cycle Detection with DFS

```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}
    
    def dfs_visit(vertex):
        color[vertex] = GRAY
        
        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:  # Back edge found
                return True
            if color[neighbor] == WHITE and dfs_visit(neighbor):
                return True
        
        color[vertex] = BLACK
        return False
    
    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs_visit(vertex):
                return True
    return False
```

## Chapter 4: Algorithm Complexity Analysis

### 4.1 Time and Space Complexity

**BFS Complexity:**
- Time: O(V + E) where V = vertices, E = edges
- Space: O(V) for queue and visited set

**DFS Complexity:**
- Time: O(V + E)
- Space: O(V) for recursion stack or explicit stack

### 4.2 When to Use BFS vs DFS

**Use BFS when:**
- Finding shortest path in unweighted graphs
- Level-order processing is needed
- Graph is very deep (avoid stack overflow)
- Finding connected components in undirected graphs

**Use DFS when:**
- Memory is limited (less space overhead)
- Finding any path (not necessarily shortest)
- Topological sorting
- Detecting cycles
- Tree/graph traversal where order doesn't matter

## Chapter 5: Advanced Graph Algorithms

### 5.1 Flood Fill Algorithm

Used in image processing, paint bucket tools, and maze solving:

```python
def flood_fill(image, sr, sc, new_color):
    if not image or sr < 0 or sr >= len(image):
        return image
    
    original_color = image[sr][sc]
    if original_color == new_color:
        return image
    
    def dfs(r, c):
        if (r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or 
            image[r][c] != original_color):
            return
        
        image[r][c] = new_color
        
        # Fill in 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image
```

### 5.2 Finding Connected Components

```python
def find_connected_components(graph):
    visited = set()
    components = []
    
    for vertex in graph:
        if vertex not in visited:
            component = []
            stack = [vertex]
            
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.append(v)
                    stack.extend(graph[v])
            
            components.append(component)
    
    return components
```
                    """,
                    "exercises": [
                        "Implement BFS to find the shortest path between two nodes in an unweighted graph",
                        "Use DFS to detect cycles in both directed and undirected graphs",
                        "Implement flood fill algorithm for a 2D grid (like paint bucket tool)",
                        "Build a maze solver using both BFS and DFS, compare their performance",
                        "Create a social network analyzer that finds degrees of separation between people",
                        "Implement topological sorting using DFS for course prerequisite scheduling",
                        "Find all connected components in an undirected graph"
                    ],
                    "lab_description": "Build a comprehensive social network analysis tool that can find shortest connections between people, detect communities (connected components), analyze influence paths, and visualize network structures. Implement both BFS and DFS algorithms to solve real-world graph problems."
                },
                "python-advanced": {
                    "title": "Object-Oriented Design Patterns",
                    "reading": """
# Object-Oriented Programming & Design Patterns

## Classes and Objects
Classes are blueprints for creating objects with attributes and methods.

### Key Concepts:
- **Encapsulation**: Bundle data and methods together
- **Inheritance**: Create new classes based on existing ones
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hide complex implementation details

## Common Design Patterns

### Singleton Pattern
Ensures only one instance of a class exists:
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern
Creates objects without specifying exact classes:
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
```

### Observer Pattern
Allows objects to notify other objects about state changes.
                    """,
                    "exercises": [
                        "Implement a simple class hierarchy for shapes",
                        "Create a factory pattern for different data parsers",
                        "Build an observer pattern for event handling"
                    ],
                    "lab_description": "Design a game engine with modular components and design patterns"
                }
            },
            "javascript": {
                "js-fundamentals": {
                    "title": "Modern JavaScript & DOM Manipulation",
                    "reading": """
# Modern JavaScript & DOM Manipulation

## ES6+ Features
Modern JavaScript includes powerful features that make code cleaner and more efficient.

### Arrow Functions:
```javascript
const add = (a, b) => a + b;
const users = data.map(user => user.name);
```

### Destructuring:
```javascript
const {name, age} = person;
const [first, second] = array;
```

### Async/Await:
```javascript
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## DOM Manipulation
The Document Object Model (DOM) allows JavaScript to interact with HTML elements.

### Selecting Elements:
- `document.getElementById('myId')`
- `document.querySelector('.myClass')`
- `document.querySelectorAll('div')`

### Modifying Elements:
- `element.textContent = 'New text'`
- `element.style.color = 'red'`
- `element.classList.add('active')`

### Event Handling:
```javascript
button.addEventListener('click', (event) => {
    console.log('Button clicked!');
});
```
                    """,
                    "exercises": [
                        "Create an interactive to-do list with add/remove functionality",
                        "Build a dynamic form validator",
                        "Implement a simple image gallery with modal view"
                    ],
                    "lab_description": "Build an interactive dashboard with real-time data updates"
                },
                "js-algorithms": {
                    "title": "Data Structures in JavaScript",
                    "reading": """
# Data Structures in JavaScript

## Arrays and Array Methods
JavaScript arrays are dynamic and come with powerful built-in methods.

### Essential Methods:
- `map()`: Transform each element
- `filter()`: Select elements based on condition
- `reduce()`: Combine elements into single value
- `find()`: Find first matching element
- `sort()`: Sort elements

### Example:
```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);
```

## Objects and Maps
Objects are key-value pairs, while Maps provide more advanced key-value functionality.

### Objects:
```javascript
const person = {
    name: 'Alice',
    age: 25,
    greet() { return `Hello, I'm ${this.name}`; }
};
```

### Maps:
```javascript
const cache = new Map();
cache.set('key1', 'value1');
cache.get('key1'); // 'value1'
```

## Implementing Data Structures

### Stack:
```javascript
class Stack {
    constructor() { this.items = []; }
    push(item) { this.items.push(item); }
    pop() { return this.items.pop(); }
    peek() { return this.items[this.items.length - 1]; }
}
```

### Queue:
```javascript
class Queue {
    constructor() { this.items = []; }
    enqueue(item) { this.items.push(item); }
    dequeue() { return this.items.shift(); }
}
```
                    """,
                    "exercises": [
                        "Implement a binary search algorithm",
                        "Create a hash table with collision handling",
                        "Build a simple graph data structure with BFS/DFS"
                    ],
                    "lab_description": "Implement a text search engine with indexing and ranking"
                },
                "js-react": {
                    "title": "React Components & State Management",
                    "reading": """
# React Components & State Management

## Functional Components & Hooks
Modern React uses functional components with hooks for state management.

### useState Hook:
```javascript
const [count, setCount] = useState(0);
const increment = () => setCount(count + 1);
```

### useEffect Hook:
```javascript
useEffect(() => {
    // Side effect code
    document.title = `Count: ${count}`;
    
    // Cleanup function
    return () => {
        document.title = 'React App';
    };
}, [count]); // Dependency array
```

### Custom Hooks:
```javascript
function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() => {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : initialValue;
    });
    
    const setStoredValue = (value) => {
        setValue(value);
        localStorage.setItem(key, JSON.stringify(value));
    };
    
    return [value, setStoredValue];
}
```

## Component Patterns

### Composition:
```javascript
function Card({ children, title }) {
    return (
        <div className="card">
            <h3>{title}</h3>
            {children}
        </div>
    );
}
```

### Render Props:
```javascript
function DataFetcher({ render }) {
    const [data, setData] = useState(null);
    // ... fetch logic
    return render(data);
}
```
                    """,
                    "exercises": [
                        "Build a reusable modal component",
                        "Create a custom hook for API calls",
                        "Implement a shopping cart with context"
                    ],
                    "lab_description": "Build a full-featured task management app with React"
                }
            }
        }
    
    def get_relevant_content(self, question: str, skill: str, lab_id: str) -> str:
        """Simple keyword-based RAG to find relevant lab content"""
        if skill not in self.labs or lab_id not in self.labs[skill]:
            return ""
        
        lab_data = self.labs[skill][lab_id]
        question_lower = question.lower()
        
        # Check if question contains programming-related keywords
        programming_keywords = [
            'algorithm', 'algorithms', 'function', 'functions', 'code', 'implement', 'debug', 'error', 
            'variable', 'variables', 'loop', 'loops', 'array', 'arrays', 'list', 'lists', 
            'dict', 'dictionary', 'dictionaries', 'class', 'classes', 'object', 'objects',
            'bfs', 'dfs', 'graph', 'graphs', 'tree', 'trees', 'sort', 'sorting', 'search', 
            'python', 'javascript', 'react', 'html', 'css', 'programming', 'syntax',
            'data', 'structure', 'structures', 'comprehension', 'comprehensions',
            'what', 'how', 'why', 'when', 'where', 'explain', 'help', 'tutorial'
        ]
        
        # Check if question is programming-related
        if not any(keyword in question_lower for keyword in programming_keywords):
            return ""
        
        # Combine all lab content for context
        context_parts = [
            f"Lab Title: {lab_data['title']}",
            f"Reading Material:\n{lab_data['reading']}",
            f"Exercises: {', '.join(lab_data['exercises'])}",
            f"Lab Project: {lab_data['lab_description']}"
        ]
        
        return "\n\n".join(context_parts)

# Initialize lab manager
lab_manager = LabManager()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "CodeSafari 101 API is running!"}

@app.get("/labs")
async def get_labs():
    """Get all available labs organized by skill"""
    return lab_manager.labs

@app.get("/labs/{skill}/{lab_id}")
async def get_lab_detail(skill: str, lab_id: str):
    """Get detailed content for a specific lab"""
    if skill not in lab_manager.labs or lab_id not in lab_manager.labs[skill]:
        raise HTTPException(status_code=404, detail="Lab not found")
    
    return lab_manager.labs[skill][lab_id]

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """RAG-powered chatbot endpoint"""
    try:
        # Get relevant content using simplified RAG
        context = lab_manager.get_relevant_content(request.question, request.skill, request.lab_id)
        
        # Check if question is relevant to lab content
        if not context:
            return ChatResponse(
                response="I can only help with questions related to the current lab. Please ask about the lab content, concepts, exercises, or implementation details.",
                relevant=False
            )
        
        sources = ["Lab content"]
        
        # Create GPT prompt with RAG context
        system_prompt = f"""You are a helpful coding tutor for CodeSafari 101, specifically helping with lab exercises. 

You can only answer questions related to the current lab content provided below. If a question is unrelated to programming, algorithms, or the specific lab content, politely redirect the student to focus on the lab.

Current Lab Context:
{context}

Guidelines:
- Provide hints and guidance, not complete solutions
- Ask follow-up questions to help students think through problems
- Reference specific parts of the lab content when helpful
- Keep responses concise and educational
- If asked about unrelated topics (like celebrities, sports, etc.), politely redirect to lab content
"""

        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.question}
            ],
            max_tokens=400,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        return ChatResponse(
            response=ai_response,
            relevant=True,
            sources=sources
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
