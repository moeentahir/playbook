Developer - Technical Interview Questions

Technical Depth

What technology/language/tool that you're currently playing with excites you the most? Why?
What technologies out there do you NOT like? Why?
What’s the difference between an Abstract class and an Interface? In other words, when would you choose one over the other?
What are the 3 characteristics of an Object Oriented Language? What do you find useful about Object Oriented Programming Languages? What about static - vs. -dynamic languages? What are your experiences (if any) with them? Compare.
What is the difference between extends and implements keywords? (extends is used to increase the vocabulary within the class, implements alerts clients that they can rely on a certain contract.) What similar purposes do they serve? How do they differ? (Usually, how deep their understanding of the difference between the two and when to use each gives a pretty good feel for their depth of OO and Java experience).



Technical Breadth

What are the differences between Java/Ruby or .NET?
Do you consider yourself to be a pure Java, .NET or Ruby developer?  Would you feel comfortable doing a project in another language?
What are 3 characteristics of an OO language?  What do you find useful about OOP languages?  What about static vs. dynamic languages?  What are your experiences (if any) with them?
What are the top level keywords that can appear in an SQL query and what order do they come in? SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY

Conceptual Java Questions

Java Generics
Question:
           Object[] array = new String[1]; 
List<Object> list = new ArrayList<String>(); 
Comment on the above 2 lines of code.
Interviewer Notes: Covariance in arrays versus Invariance in generics. Why covariance vs invariance? For greater depth, how do you model covariance and contravariance in generics. The rationale behind the Java design decision for arrays to be covariant and lists to be invariant. How does this factor in working with arrays and collections in conjunction?
Java Lambdas
Question: What are the implicit finals in the context of lambdas? 
Interviewer Notes: How do closures work in Java? Discuss SAM types. Need for implicit finals (multi-threading)
Java Concurrency
Question: Compare and contrast Java concurrency with database concurrency control. 
Interviewer Notes:  Consider atomicity, consistency, isolation and durability in database transactions and which of these properties map to Java concurrency, and how they differ. Basics of Java Memory Model - visibility and ordering. For greater depth, explore pessimistic locking vs optimistic CAS. 
Hotspot
Question: Discuss JIT compilation in Java.
Interviewer Notes: Basic explanation of JIT compilation.  Improvements/optimisations offered by a JIT compiler. Synchronization during JIT compilation. Perhaps a detour into GraalVM.
Garbage Collection
Question: How does garbage collection in Java work?
Interviewer Notes: What’s the candidate’s understanding of generational garbage collection? Also GC algorithms - mark and sweep versus G1. For greater depth, any experiences in troubleshooting and/or optimising GC?
Data Structures
Question: When/why would you use a TreeMap over HashMap? 
Interviewer Notes: Compare/contrast computational complexity of TreeMap and HashMap operations and the ordering implications. For greater depth, delve into implementation (hashing, buckets, red-black trees etc)
Distributed Systems
Question: Explain CAP theorem 
Interviewer notes: What is CAP theorem? What is partition tolerance? What is the trade-off between consistency and availability? What is the specific meaning of consistency in the context of CAP theorem? What are the other meanings of consistency? Consider exploring the value of replication and sharding.
Design Sense
Question: How would you assess an existing Java architecture?
Interviewer notes: What metrics does the candidate come up with? What defines a good architecture for the candidate? Discuss coupling, cohesion and Kent Beck’s 4 rules for simple design. Consider SOLID principles and evolutionary design.


Advanced Java Questions

What is the effect of the static modifier added to an inner class?
On the whiteboard, give a coding problem. A good one is an abstract class Dog, an interface Hound. Create a constructor and an abstract method in Dog. Add a method to Hound. Ask the candidate to implement a class Beagle which incorporates features of Dog and Hound.
In an application server, what are some techniques for debugging classloader issues?
What should be the first line of every Unix shell script?
What is the effect of adding –Pd to the cvs update command.
In container managed transactions, what is the effect of “requires” and “requires new”? Explain the transactional effects of interactions between the two.

Advanced .NET Questions

What is the keyword in C# to declare a type safe function pointer?
What interface must an object inherit from to be used in a ‘Using’ statement?  What is "using" statement in C# used for?  What is good about a "using" block?
What is the difference between a ‘value’ type and a ‘reference’ type?
In C#, what is ‘boxing’?
What is the ADO.NET object used to fill a DataSet?
Do they know delegate, delegate chain?
Have they used any advanced language features (i.e. Attributes, Delegates, Remoting)?







