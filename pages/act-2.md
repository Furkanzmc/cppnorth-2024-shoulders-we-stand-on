
# Act 2: The Theoretical Foundations

Establishing the core principles and theories that underpin modern technology, building upon the visionaries' ideas from Act 1.

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
```

---

# John McCarthy

## Coined Artificial Intelligence

## Lisp

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 2
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    end
```

---

# Edsger W. Dijkstra

## Finding the Shortest Path

## Intro of Structured and Distributed Programming

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 2
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    B2("Edsger W. Dijkstra\nStructured programming principles (1959)") --> A3
    end
```

---

# Donald Knuth

## The Art of Computer Programming

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 2
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    B2("Edsger W. Dijkstra\nStructured programming principles (1959)") --> A3
    B3("Donald Knuth\n'The Art of Computer Programming' (1968)") --> A3
    end
```

---

# Niklaus Wirth

## A Learner's Language, Pascal

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 2
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    B2("Edsger W. Dijkstra\nStructured programming principles (1959)") --> A3
    B3("Donald Knuth\n'The Art of Computer Programming' (1968)") --> A3
    B4("Niklaus Wirth\nDevelopment of Pascal (1970)") --> B2
    end
```

---

# Alan Kay

## Usability and efficiency with Smalltalk, OOP, GUI

---

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 2
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    B2("Edsger W. Dijkstra\nStructured programming principles (1959)") --> A3
    B3("Donald Knuth\n'The Art of Computer Programming' (1968)") --> A3
    B4("Niklaus Wirth\nDevelopment of Pascal (1970)") --> B2
    B5("Alan Kay\nDevelopment of Smalltalk (1972)") --> A7
    end
```

---

# Karen Spärck Jones

## Information retrieval with IDF

---

```mermaid
flowchart LR
    subgraph Act 1
    A1("Charles Babbage\nDesigned the Analytical Engine (1837)")
    A2("Ada Lovelace\nNotes on the Analytical Engine (1842)") --> A1
    A3("Alan Turing\n'On Computable Numbers' (1936)") --> A1
    A3 --> A2
    A4("Vannevar Bush\n'As We May Think' (1945)") --> A3
    A5("John von Neumann\nComputer architecture papers (1945)") --> A3
    A6("J.C.R. Licklider\n'Man-Computer Symbiosis' (1960)") --> A4
    A7("Douglas Engelbart\nInvented the computer mouse (1964)") --> A6
    A8("Ivan Sutherland\nDeveloped Sketchpad (1963)") --> A7
    end
    subgraph Act 1
    B1("John McCarthy\nDevelopment of Lisp (1958)") --> A3
    B2("Edsger W. Dijkstra\nStructured programming principles (1959)") --> A3
    B3("Donald Knuth\n'The Art of Computer Programming' (1968)") --> A3
    B4("Niklaus Wirth\nDevelopment of Pascal (1970)") --> B2
    B5("Alan Kay\nDevelopment of Smalltalk (1972)") --> A7
    B6("Karen Spärck Jones\nInverse Document Frequency (1972)") --> B1
    end
```