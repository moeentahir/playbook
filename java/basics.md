# Java basics
Java code flow  
Hello.java > Byte code > Java Enterprise APIs> Java standard edition APIs > JVM  

## Java EE
![Java EE](images/java-ee.png)

## Java versions
![Java versions](images/java-versions.png)

## What Java
![What Java](images/what-jdk.png)

## Considerations
![Considerations](images/considerations.png)

## JPA
- JPA describes the management of relational data in applications using Java.
- JPA (Java Persistence API) is an interface for persistence providers to implement.
- The JPA specification lets you define which objects should be persisted, and how those objects should be persisted in your Java applications.
- By itself, JPA is not a tool or framework; rather, it defines a set of concepts that can be implemented by any tool or framework.
- JPA's object-relational mapping (ORM) model was originally based on Hibernate
- JPA has spawned many compatible tools and frameworks; Hibernate is just one of them.
- While JPA's object-relational mapping (ORM) model was originally based on Hibernate, it has since evolved. Likewise, while JPA was originally intended for use with relational/SQL databases, some JPA implementations have been extended for use with NoSQL datastores. A popular framework that supports JPA with NoSQL is EclipseLink.
### JPA implementations:
- Hibernate: The most advanced and widely used. Pay attention for the classpath because a lot of libraries are used, especially when using JBoss. Supports JPA 2.1.
- Toplink: Only supports the basic JPA specs. (This was oracle’s free version of the JPA implementation)
- EclipseLink: Is based on TopLink, and is the intended path forward for persistence for Oracle and TopLink. Supports JPA 2.1
- Apache OpenJPA: Best documentation but seems very buggy. Open source implementation for JPA. Supports JPA 2.0
- DataNucleus: Well documented, open source (Apache 2 license), is also a JDO provider. Supports JPA 2.1
- ObjectDB: well documented
- CMobileCom JPA: light-weight JPA 2.1 implementation for both Java and Android.
#### Hibernate
- Hibernate ORM is one of the most mature JPA implementations, and still a popular option for ORM in Java.
- Hibernate ORM 5.3.8 (the current version as of this writing) implements JPA 2.2.
- Hibernate is one such implementation of JPA. When you use Hibernate with JPA you are actually using the Hibernate JPA implementation.

#### What collections to use
![What collection](images/what-colleciton-to-use.png)
