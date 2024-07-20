---
layout: image-left
image: https://i.pinimg.com/736x/15/d5/e1/15d5e17569e6f3ef1595c61c8ab56518--fred-rogers-successful-people.jpg
---

> Would you just take, along with me, 10 seconds to think of the people who have helped you become
> who you are, those who cared about you and wanted what was best for you in life.
> 
> - Fred Rogers

---
dragPos:
  square: 247,129,476,287
---

<div v-click.hide="1">
    <img v-drag="'square'" src="/assets/how-did-i-get-here.jpg" style="border-radius: 50%;">
</div>

<v-click>

```mermaid
gitGraph
    commit id: "Born"
    commit id: "Uncle in IT"
    branch new-interest
    checkout new-interest
    commit id: "School resources"
    checkout main
    merge new-interest
    commit id: "Coming to Canada"
    commit id: "Start up life"
    commit id: "People I've met"
    branch social-life
    checkout social-life
    commit id: "People I can depend on"
    commit id: "Friend who pushes me"
    checkout main
    commit id: "A bunch of other stuff"
    checkout social-life
    branch career
    checkout career
    commit id: "Mentors"
    commit id: "C++ Study Group"
    checkout social-life
    merge career
    checkout main
    merge social-life
    commit id: "Here"
```

</v-click>

<!--
- We have to pick a starting point.
- Different choices would different versions of me.
-->

---
dragPos:
  square: 356,27,167,_,-8
---

<img v-drag="'square'" src="/assets/people/alan-turing.jpg" style="border-radius: 50%;">

<v-drag pos="801,91,167,_,-8">
    <img src="/assets/people/edsger-dijkstra.jpg" style="border-radius: 50%;">
</v-drag>

<v-drag pos="38,342,167,_,-8">
    <img src="/assets/people/charles-babbage.jpg" style="border-radius: 50%;">
</v-drag>

<v-drag pos="562,5,261,_,-15">
    <img src="/assets/people/dennis-ritchie-ken-thomson.jpg" style="border-radius: 50%;">
</v-drag>

<v-drag pos="582,210,261,_,12">
    <img src="/assets/people/grace-hopper.jpg" style="border-radius: 50%;">
</v-drag>

<v-drag pos="43,1,261,_,-15">
    <img src="/assets/people/linus-torvalds.jpg" style="border-radius: 50%;">
</v-drag>

<v-drag pos="223,287,261,_,-15">
    <img src="/assets/people/margaret-hamilton.jpeg" style="border-radius: 50%;">
</v-drag>

---
layout: image
image: /assets/placeholder-graph.png
---

<!--
- Imagine this was your dependency graph.
- But this is how advancements in human knowledge works. One person depending on another, one giant
  standing on the shoulder of another.
- Jonathan Blows talk [Preventing the Collapse of
  Civilization](https://www.youtube.com/watch?v=ZSRHeXYDLko) gives similar examples. He talks about
  how we need to create a culture of teaching each other and keeping knowledge alive to keep
  progressing the technology. Recommended watch.
- If anybody there didn't have the influence or the life they did, we could have ended up in a
  different place.
- Let's listen to Mr Rogers, and do him one better, and instead of taking 10 seconds, take the rest
  of the talk to go through these influences, discover what they did for us, and exercise our minds
  about how things could have turned out if that person ended up in a different path.
-->

---
layout: image-left
image: /assets/people/charles-babbage.jpg
---

# Charles Babbage

<!--
- Every journey has a beginning. The beginning for this one is endless, but we'll have to choose
  somewhere. So this is where we begin.
-->

---
layout: center
clicks: 2
dragPos:
  square: 686,55,268,408,11
---

```mermaid
timeline
    Early Days : Afluent family
               : Life-threatening fever**
               : Good school
```



<div v-if="$slidev.nav.clicks === 1">

<img v-drag="'square'" src="/assets/charles-babbage-brain.png" style="border-radius: 10%;">

</div>

<!--
## Intro

- He was quite a chap!
- Keen interest in mathematics. A number driven person.
- Known as the father of computers.
- His father was a banker and when he died, he left a considerable inheritance for him. During this
  university years, he relied on his father's support.
- Had a Life-threatening fever, what would have happened if he died?...
- Went to good schools, had access to books and tutors. Pivotal moment!
-->

---
clicks: 3
---

<div style="text-align: center;" v-if="$slidev.nav.clicks < 3">
<div style="auto">

```mermaid
timeline
    University Years : University of Cambridge
                     : The Ghost Club**
                     : Analytical Society
```

</div>
</div>

<div style="text-align: center;" v-if="$slidev.nav.clicks === 3">
<div style="auto">

```mermaid
timeline
    Early Days : Afluent family
               : Life-threatening fever**
               : Good school
    University Years : University of Cambridge
                     : The Ghost Club**
                     : Analytical Society
```

</div>
</div>

<div v-if="$slidev.nav.clicks === 1">

<v-drag pos="601,54,334,_,-6">
    <img src="/assets/the-ghost-club.png" style="border-radius: 8%;">
</v-drag>

</div>

<div v-if="$slidev.nav.clicks === 2">

<v-drag pos="601,54,300,_,-6">
    <img src="/assets/1812-human-computers-french.png" style="border-radius: 8%;">
</v-drag>

</div>

<!--
- During university, came in contact with other mathematicians and influential people.
- He joined [The Ghost Club](https://www.ghostclub.org.uk/), which is still active today! What would
  have happened if he got too into it and didn't pursue science?
- In 1812, the French government calculated these tables in a different way. Their mathematicians
  distributed the work to 80 human computers who only knew what work they were doing and subtraction
  and addition. For the first time, mass production was applied to mathematics and Babbage thought
  this work could be taken over by machines entirely.
-->

---
clicks: 3
---

<div style="text-align: center;" v-if="$slidev.nav.clicks < 3">
<div style="auto">

```mermaid
timeline
    Later Years : Royal Astronomical Society
                : The Difference Engine
                : Analytical Engine**
                
```

</div>
</div>

<div style="text-align: center;" v-if="$slidev.nav.clicks === 3">
<div style="auto">

```mermaid
timeline
    Early Days : Afluent family
               : Life-threatening fever**
               : Good school
    University Years : University of Cambridge
                     : The Ghost Club**
                     : Analytical Society
    Later Years : Royal Astronomical Society**
                : The Difference Engine
                : Analytical Engine**
                
```

</div>
</div>

<div v-if="$slidev.nav.clicks === 1">

<v-drag pos="237,72,544,_,6">
    <img src="/assets/charles-babbage-difference-engine.jpg" style="border-radius: 8%;">
</v-drag>

</div>

<div v-if="$slidev.nav.clicks === 2">

<v-drag pos="106,-15,813,_,-6">
    <img src="/assets/analytical-engine.jpg" style="border-radius: 8%;">
</v-drag>

</div>

<!--
## Difference Engine

- Difference engine was meant for solving polynomial equations. He created this to help with
  mathematical tables for the nautical almanac.
- This first difference engine would have been composed of around 25,000 parts, weighed fifteen
  short tons (13,600 kg), and would have been 8 ft (2.4 m) tall. **If a moth flew into this, it
  would have just died. Imagine having "bug free" apps!**
- It was never built because the machinist responsible for building the machine refused to do it
  unless he was prepaid. The machinist who was building it Joseph Clement. He was one of the
  greatest at the time, and the tools he built were high quality.
  He demanded too much money and they didn't finish the project.
- Difference Engine inspired the novel... [The Difference Engine](https://en.wikipedia.org/wiki/The_Difference_Engine)

## Analytical Engine

- Before the construction of the Difference Engine began, he started working on Analytical Engine.
- Difference Engine was meant for a mechanized computation. But Analytical Engine could handle any
  computation, making it a general purpose computer.
- It was programmed using punch cards. It allowed for sequential control, looping, and branching.
- Despite the importance of his work, the analytical engine was unknown to the builders of the
  electromechanical and electronic computing machines in 1930s and 1940s. J. Presper Eckert and John
  W. Mauchly similarly were not aware of the details of Babbage's analytical engine work prior to
  the completion of their design for the first electronic general-purpose computer, the ENIAC.
- Vannevar Bush's paper Instrumental Analysis (1936) included several references to Babbage's work.
  In the same year he started the Rapid Arithmetical Machine project to investigate the problems of
  constructing an electronic digital computer.
-->

---
layout: image-left
image: /assets/people/lady-ada-lovelace.png
---

# Lady Ada Lovelace

<!--
- Next up, Lady Ada Lovelace. She was the first computer programmer. But I learned something that
  makes her even more impressive than that...
-->

---
layout: center
clicks: 2
dragPos:
  square: 684,186,255,266,11
---

<div v-if="[0, 2, 3].indexOf($slidev.nav.clicks) > -1">

```mermaid
timeline
    Early Days : Poet father, mathmatician mother
               : Mother encouraged math**
```

</div>

<div v-if="$slidev.nav.clicks === 1">

## ~~Lady~~ Diva Ada Lovelace

<img v-drag="'square'" src="/assets/diva-ada-lovelace.png" style="border-radius: 10%;">

</div>

<!--
## Intro

- Lady Ada Lovelace was the daughter of the famous poet Lord Byron, although she never had a
  relationship with him due to her parents' separation when she was just a month old.
- Her mother, Lady Byron, was a skilled mathematician and encouraged Ada's interest in mathematics
  and logic as a way to steer her away from her father's artistic temperament.
-->

---
clicks: 1
---

<div style="text-align: center;">
<div style="auto">

```mermaid
graph LR
    Lovelace -- 🕊️🎶♥️🦌🌎 --> Babbage
    Babbage -- 01001101 01100001 01110100 01101000 --> Lovelace
```

</div>
</div>

<div v-if="$slidev.nav.clicks === 1">

> Supposing, for instance, that the fundamental relations of pitched sounds in the science of
> harmony and of musical composition were susceptible of such expression and adaptations, the engine
> might compose elaborate and scientific pieces of music of any degree of complexity or extent.

</div>

<!--
- Charles Babbage considered the Analytical Engine to be a merely a calculation machine. But Ada
  Lovelace saw a potential for representing natural objects with numbers.
-->

---
layout: image-left
image: /assets/people/alan-turing.jpg
---

# Alan Turing

<!--
- Let's fast word to Alan Turing. He was a mathematician, logician, and computer scientist who
  played a pivotal role in the development of theoretical computer science and artificial
  intelligence.
-->

---
layout: center
clicks: 2
dragPos:
  square: 686,55,268,408,11
---

```mermaid
timeline
    Early Days : Loved math and science
               : Friendship Christopher Morcom**
               : King's College, Cambridge
```

<!--
## Intro

- He had great interest in math and science from an early age.
- In public school, his great skills were not appreciated because the school placed more emphasis on
  classics.
- Developed a friendship with Christopher Morcom, who shared his interest in science and
  mathematics. Sadly, he died early from TB that he got from drinking contaminated milk.
- Turing coped with this grief by working even harder. What would have happened if Turing was the
  one who died?
-->

---
clicks: 3
---

<div style="text-align: center;" v-if="$slidev.nav.clicks < 3">
<div style="auto">

```mermaid
timeline
    University Years : King's College, Cambridge
                     : Studied under Alonzo Church
                     : Developed the Turing Machine**
```

</div>
</div>

<!--
- During his time at Cambridge, he studied under the mathematician Alonzo Church.
- He developed the concept of the Turing Machine, a fundamental model of computation that underpins
  much of computer science theory.
> "von Neumann ... firmly emphasised to me, and to others I am sure, that the fundamental conception
> is owing to Turing—insofar as not anticipated by Babbage, Lovelace and others." Letter by Stanley
> Frankel to Brian Randell, 1972, quoted in Jack Copeland (2004) The Essential Turing, p. 22.
-->

---
clicks: 3
---

<div style="text-align: center;" v-if="$slidev.nav.clicks < 3">
<div style="auto">

```mermaid
timeline
    Later Years : Great runner!
                : Bletchley Park
                : Cracked Enigma**
                : Artificial Intelligence**
                
```

</div>
</div>

<div v-if="$slidev.nav.clicks === 1">

<v-drag pos="601,54,300,_,-6">
    <img src="/assets/on-your-left.gif" style="border-radius: 8%;">
</v-drag>

</div>

<div style="text-align: center;" v-if="$slidev.nav.clicks === 3">
<div style="auto">

```mermaid
timeline
    Early Days : Loved math and science
               : Friendship Christopher Morcom**
               : King's College, Cambridge
    University Years : King's College, Cambridge
                     : Studied under Alonzo Church
                     : Developed the Turing Machine
    Later Years : Great runner!
                : Bletchley Park
                : Cracked Enigma**
                : Artificial Intelligence**
                
```

</div>
</div>

<!--
## Bletchley Park and Enigma

- During World War II, Turing worked at Bletchley Park, the UK's codebreaking center.
- He played a pivotal role in cracking the German Enigma code, significantly contributing to the
  Allied victory.
- His work laid the groundwork for modern computing and artificial intelligence.
- Turing's contributions extended beyond codebreaking; he proposed the concept of artificial
  intelligence and the famous Turing Test to evaluate a machine's ability to exhibit intelligent
  behavior equivalent to that of a human.
> I have such a stressful job that the only way I can get it out of my mind is by running hard; it's
> the only way I can get some release.
- He was Walton Athletic Club's best runner, a fact discovered when he passed the group while
  running alone.
-->
