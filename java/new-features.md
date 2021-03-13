# Java new features

## Java 15
### Sealed classes
- Control what classes can inherit a sealed class or what interfaces can inplement  a sealed interface
- Works on both interface and classes
- Final restricts for all the classes whereas sealed allows a few classes to be ingerited

```Java
public sealed class Account permits SavingsAccount, CheckingAccount {
}
public final class SavingsAccount extends Account {
}
public final class CheckingAccount extends Account{
}
```

## Java 14
### Instanceof Operator
instanceof operator is extended to take a type test pattern instead of just a type 

* Before Java 14

```Java
if (obj instanceof String) {
    String s = (String)obj;
}
```

* After Java 14

```Java
if (obj instanceof String s) {
    // can use s here
}
```
```Java
if (obj instanceof String s && s.length() > 5) {
  //
}
```
### Records
Records provide a compact syntax for declaring classes which are plain immutable data carriers.

* Creating record
```Java
public record Person(String name, String gender, int age) {}
```
* Using  record
```Java
      Person person = new Person("Jenny", "Female", 35);
      System.out.println(person.name());
      System.out.println(person.gender());
      System.out.println(person.age());
      System.out.println(person);
```
