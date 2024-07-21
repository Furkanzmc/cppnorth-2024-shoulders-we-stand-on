# Act 4: Building the Infrastructure

Developing the infrastructure that supports modern computing and connectivity, transforming theoretical advancements into practical systems.

---

## Robert Noyce (1927-1990)

**"Mayor of Silicon Valley"**

```mermaid {scale: 0.5}
timeline
    title Key Career Milestones
    section Early Work
    1953 : Joins Philco Corporation
    1956 : Moves to Shockley Semiconductor Laboratory
    section Fairchild
    1957 : Co-founds Fairchild Semiconductor
    1959 : Co-invents the integrated circuit independently
    1960 : Fairchild produces the first commercially viable integrated circuits
    section Intel
    1968 : Co-founds Intel with Gordon Moore
```

---
layout: center
---

# Noyce's Early Work

<div style="text-align: center;">
<div style="auto">

```mermaid {scale: 0.5}
timeline
    title Robert Noyce's Impactful Work and Cultural Influence
    section Early Work
    1953 : Joins Philco Corporation
        : Works on transistor technology
    1956 : Moves to Shockley Semiconductor Laboratory under William Shockley
        : Experiences a rigid management style
```

</div>
</div>

---

# Fairchild and the First Integrated Circuit

<div style="text-align: center;">
<div style="auto">

```mermaid {scale: 0.5}
timeline
    title Robert Noyce's Impactful Work and Cultural Influence
    section Fairchild Semiconductor
    1957 : Co-founds Fairchild Semiconductor with seven other engineers (the "Traitorous Eight")
        : Learns from Shockley's mistakes
        : Embraces a collaborative and egalitarian work environment
        : Promotes openness, innovation, and the free exchange of ideas
    1959 : Co-invents the integrated circuit independently around the same time as Jack Kilby at Texas Instruments
    1960 : Fairchild produces the first commercially viable integrated circuits
        : Revolutionizes the electronics industry
```

</div>
</div>

---

# Intel and the Future

<div style="text-align: center;">
<div style="auto">

```mermaid {scale: 0.5}
timeline
    title Robert Noyce's Impactful Work and Cultural Influence
    section Intel Corporation
    1968 : Co-founds Intel with Gordon Moore
        : Expands the open culture with a flat hierarchy, open communication, and employee autonomy
    1971 : Launches the world's first commercially available microprocessor, the Intel 4004
        : Plays a key role in Intel's development and growth
    1970s : Creates significant advances in semiconductor technology
        : Establishes Intel as a model for open organizational culture
        : Solidifies key principles in the industry that became characteristic of Silicon Valley
```

</div>
</div>

---

## Mark Dean (1957-present)

**Co-creator of the IBM personal computer (1981)**

## Key Contributions

- **Pioneering Innovations**: Co-inventor of the ISA Bus, foundational to the personal computer.
- **Multiple Patents**: Holds 44 U.S. patents, reflecting a prolific and impactful career.
- **Diverse Contributions**: From computer architecture to artificial intelligence, his work spans multiple critical areas in technology.
- **Educational Impact**: Professor Emeritus at the University of Tennessee, shaping the next generation of engineers.

---

# Co-invention of the ISA Bus

```mermaid
graph TD
    A[Patent No. 4,528,626<br>ISA Bus<br>1985]
    B[Patent No. 6266745<br>Utilization of Nodes by Threads<br>2001]
    C[Patent No. 6336170<br>Shared-Memory Data Processing<br>2002]
    D[Patent No. 7206163<br>Magnetic Thread Storage<br>2007]
    E[Patent No. 20150106311<br>Artificial Neural Networks<br>2015]
    F[Patent No. 20150106316<br>Real-Time Monitoring of Neural Networks<br>2015]
    G[Color Graphics Adapter<br>First color display on IBM PCs]
    H[First Gigahertz Microprocessor<br>Significant advance in processor speed]

    A --> B
    B --> C
    C --> D 
    D --> E
    E --> F
    A --> G
    C --> H
    
    classDef grayout fill:transparent,stroke:transparent,stroke-width:0px,color:transparent;
    classDef highlight fill:#fbd91f,stroke:#33,stroke-width:4px;

    class A highlight;
    class B,C,D,E,F,H grayout;

    linkStyle 1,2,3,4,5,6 display:none;
```

<!-- 
In 1985, Mark Dean co-invented the ISA Bus, with Patent No. 4,528,626. This innovation was groundbreaking because it allowed different peripherals like keyboards, disk drives, and printers to connect seamlessly to computers. This development made it possible for PCs to become more modular and user-friendly, facilitating the widespread adoption of personal computers.

Beyond these patents, Dean played a crucial role in developing the Color Graphics Adapter, which brought color displays to IBM PCs. The relationship between the ISA bus and the CGA is pivotal: the ISA bus provided the necessary infrastructure that allowed peripheral devices, like the CGA, to connect and function effectively. This synergy exemplified how Dean's innovations worked together to enhance the IBM PC’s capabilities.
 -->

---

# Efficiency of Distribution Computing Systems

```mermaid
graph TD
    A[Patent No. 4,528,626<br>ISA Bus<br>1985]
    B[Patent No. 6266745<br>Utilization of Nodes by Threads<br>2001]
    C[Patent No. 6336170<br>Shared-Memory Data Processing<br>2002]
    D[Patent No. 7206163<br>Magnetic Thread Storage<br>2007]
    E[Patent No. 20150106311<br>Artificial Neural Networks<br>2015]
    F[Patent No. 20150106316<br>Real-Time Monitoring of Neural Networks<br>2015]
    G[Color Graphics Adapter<br>First color display on IBM PCs]
    H[First Gigahertz Microprocessor<br>Significant advance in processor speed]

    A --> B
    B --> C
    C --> D 
    D --> E
    E --> F
    A --> G
    C --> H

    classDef grayout fill:transparent,stroke:transparent,stroke-width:0px,color:transparent;
    classDef highlight fill:#fbd91f,stroke:#33,stroke-width:4px;

    class B,C,D,H highlight;
    class E,F grayout;

    linkStyle 4,5,6 display:none;
```

<!-- 
Dean didn't stop there. In 2001, he received Patent No. 6266745 for a method that improved the efficiency of distributed computing systems by determining the utilization of nodes by executed threads. This innovation enhanced the performance of complex computing tasks across multiple processors, which is critical for modern data centers and cloud computing.

The following year, in 2002, he was granted Patent No. 6336170, which focused on determining the utilization of shared memory within distributed processing systems. This work further contributed to making distributed computing more efficient and reliable.

This led to another monumental achievement was his work on the first gigahertz microprocessor, which marked a significant leap in processing speed. This innovation paved the way for faster and more powerful computers, influencing everything from personal computing to enterprise servers.

This in turn influenced his work on the first gigahertz microprocessor, which marked a significant leap in processing speed. This innovation paved the way for faster and more powerful computers, influencing everything from personal computing to enterprise servers.

In 2007, his innovative approach to data storage led to Patent No. 7206163 for a magnetic thread storage device. This invention improved data handling capabilities, making storage systems more efficient and robust.
 -->

---

```mermaid
graph TD
    A[Patent No. 4,528,626<br>ISA Bus<br>1985]
    B[Patent No. 6266745<br>Utilization of Nodes by Threads<br>2001]
    C[Patent No. 6336170<br>Shared-Memory Data Processing<br>2002]
    D[Patent No. 7206163<br>Magnetic Thread Storage<br>2007]
    E[Patent No. 20150106311<br>Artificial Neural Networks<br>2015]
    F[Patent No. 20150106316<br>Real-Time Monitoring of Neural Networks<br>2015]
    G[Color Graphics Adapter<br>First color display on IBM PCs]
    H[First Gigahertz Microprocessor<br>Significant advance in processor speed]

    A --> B
    B --> C
    C --> D 
    D --> E
    E --> F
    A --> G
    C --> H

    classDef highlight fill:#fbd91f,stroke:#33,stroke-width:4px;

    class E,F highlight;
```
<!-- 
Mark Dean’s contributions to artificial intelligence are also noteworthy. In 2015, he was awarded two patents related to neural networks. Patent No. 20150106311 focused on constructing and reusing components of artificial neural networks, while Patent No. 20150106316 provided methods for real-time monitoring of these networks. These patents are significant in advancing the field of AI, enabling more efficient and adaptive neural network models.
 -->

---

## Impact on Computing

- **Widespread Influence**: Innovations have shaped modern computing, making technology more accessible and powerful.
- **Educational Contributions**: Mentored and taught the next generation of engineers, ensuring the continuation of technological advancement.
- **Recognition**: His work has been acknowledged with numerous awards and honors, cementing his legacy in the field of computer science.


---

## Vint Cerf (1943-present) & Robert Kahn (1938-present)

**Co-design of the TCP/IP protocols (1973)**

- **Network Compatibility:**
  - Enabled different networks to communicate, creating the "internet"
  - Simplified data transmission and scalability

```plantuml
@startuml
actor "Vint Cerf (1943-present)" as VC
actor "Robert Kahn (1938-present)" as RK

VC -> RK: Meet at UCLA (Early 1970s)
VC -> RK: Collaborate on ARPANET testing
RK -> IPTO: Kahn joins IPTO (Late 1972)
RK -> NetworkSecurity: Works on network security, digital speech transmission, packet radio
RK -> VC: Proposes interconnecting ARPA’s networks (1973)
VC -> RK: Invite global experts for TCP/IP development (June 1973)
VC -> RK: Collaborate on protocol design
VC -> World: Introduce TCP/IP in a 1974 paper
TCP -> World: Ensure reliable, ordered, and error-checked data delivery
IP -> World: Manage addressing and routing of data packets

note over World: Impact of TCP/IP
World -> Internet: Enable different networks to communicate
World -> Internet: Create a network of networks
World -> Internet: Provide seamless data transmission and scalability
World -> Internet: Establish unified communication standard

@enduml
```

---

## Impact and Influence

- **Modern Internet:**
  - Laid the groundwork for global communication and information sharing
  - Influenced network design and cybersecurity

- **Influence:**
  - Cerf was inspired by Robert Noyce’s innovations and culture of innovation

---

## Tim Berners-Lee (1955-present)

**Inventor the World Wide Web (1989)**

## Key Contributions

- **World Wide Web:**
  - Developed HTML, HTTP, and URLs
  - Created the foundation for accessing and sharing information globally

- **Web Technologies:**
  - Transformed communication, commerce, education, and entertainment
  - Enabled countless web-based applications and services

---

# The Problem at CERN

- Challenges in sharing information among scientists
- Different computers and software systems
- Need for a universal system to share information

---

# Invention of the World Wide Web

- Proposed the World Wide Web in 1989
- Created HTML, URI, and HTTP
- Foundation of web navigation and linking

---

# The First Website

- Went live in 1991
- Explained the concept and usage of the World Wide Web
- Beginning of the web as we know it

---

# Global Impact

- Revolutionized communication, business, education, entertainment
- Rapid growth of the internet
- Creation of the digital economy

<img src="/assets/global-internet-use.png" style="border-radius: 8%; height: 70%;">

--- 

# W3C and Web Standards

- Founded World Wide Web Consortium (W3C) in 1994
- Ensuring open standards and accessibility
- Crucial role in developing web standards

---

# Current and Future Work

- Advocates for a free and open web
- Current project: Solid - decentralizing the web
- Vision for a universal and open platform

## The Problem

- Centralized platforms control user data
- Privacy concerns and data misuse
- Limited interoperability between services

## Solid's Vision

- Decentralization: Data is stored in "pods" that users control
- Interoperability: Standardized protocols for data exchange
- User Empowerment: Users decide who can access their data and how

---

## How Solid Works

- Data Pods: Personal online data stores
- Users host their own data or use trusted pod providers
- Applications interact with data pods via standard protocols

## Benefits of Solid

- Privacy: Users have full control over their data
- Portability: Data can be moved easily between services
- Innovation: New applications can be built on a standardized, open data infrastructure

### Current Status and Future Plans

- Growing community of developers and organizations
- Ongoing development and pilot projects
- Vision for a more equitable and user-centric web

---
