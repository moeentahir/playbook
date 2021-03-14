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

##### Creating record
```Java
public record Person(String name, String gender, int age) {}
```

##### Using  records
```Java
      Person person = new Person("Jenny", "Female", 35);
      System.out.println(person.name());
      System.out.println(person.gender());
      System.out.println(person.age());
      System.out.println(person);
```

##### Limitations with records
- Records cannot extend other classes
- Records can implement interfaces
- Records cannot create extra instance fields
- The static methods, static fields, static initializers are allowed
- We can declare constructors
- We can add explicit accessors
- Nested records are allowed
- Generic records are allowed
- Records can be annotated
- Records cannot be abstract
- Records are final
- Extra instance methods are allowed
- The components of a record are implicitly final

### Helpful NullPointerException
Before

```Java
Exception in thread "main" java.lang.NullPointerException
```

After
```
Exception in thread "main" java.lang.NullPointerException: Cannot read field "c" because "a.b" is null
```

### Switch Expressions And Statements
Switch Statements

```Java
package com.logicbig.example;

import java.time.LocalDate;
import java.time.Month;

public class SwitchStatementExample {
  public static void main(String[] args) {
      showQuarter(LocalDate.now().getMonth());
  }

  public static void showQuarter(Month month) {
      switch (month) {
          case JANUARY, FEBRUARY, MARCH -> System.out.println("First Quarter");//no break needed
          case APRIL, MAY, JUNE -> System.out.println("Second Quarter");
          case JULY, AUGUST, SEPTEMBER -> System.out.println("Third Quarter");
          case OCTOBER, NOVEMBER, DECEMBER -> System.out.println("Forth Quarter");
          default -> System.out.println("Unknown Quarter");
      }
  }
}
```
Switch Expressions

```Java
package com.logicbig.example;

import java.time.LocalDate;
import java.time.Month;

public class SwitchExpressionExample {
  public static void main(String[] args) {
      showQuarter(LocalDate.now().getMonth());
  }

  public static void showQuarter(Month month) {
      String quarter = switch (month) {
          case JANUARY, FEBRUARY, MARCH -> "First Quarter"; //must be a single returning value
          case APRIL, MAY, JUNE -> "Second Quarter";
          case JULY, AUGUST, SEPTEMBER -> "Third Quarter";
          case OCTOBER, NOVEMBER, DECEMBER -> "Forth Quarter";
          default -> "Unknown Quarter";
      };
      System.out.println(quarter);
  }
}
```

##### Switch and yield

```Java
package com.logicbig.example;

import java.time.LocalDate;
import java.time.Month;

public class SwitchExpressionWithYieldAndArrow {
  public static void main(String[] args) {
      showQuarter(LocalDate.now().getMonth());
  }

  public static void showQuarter(Month month) {

      String result = switch (month) {
          case JANUARY,
                  FEBRUARY,
                  MARCH -> {
              //multiple statements can be used here
              yield "First Quarter";
          }
          case APRIL, MAY, JUNE -> {
              //multiple statements can be used here
              yield "Second Quarter";
          }
          case JULY, AUGUST, SEPTEMBER -> "Third Quarter";
          case OCTOBER, NOVEMBER, DECEMBER -> {
              //multiple statements can be used here
              yield "Forth Quarter";
          }
          default -> "Unknown Quarter";
      };
      System.out.println(result);
  }
}
```

## Java 13
### Text Blocks (JEP 355)
- a multi-line string literal that can be written without + concatenation
- avoids the need for most escape sequences. That means we don't have to escape character like double quote (")
- automatically formats the string in a predictable way, and gives the developer control over format when desired
```java
package com.logicbig.example;

public class TextBlockExample2 {
  public static void main(String[] args) {
      String inputElement = """
                            Name: Jenny
                        Phone: 8675309
                            age: 35
                            """;

      System.out.println(inputElement);
  }
}
```
Output: Notice relative indenting

```
    Name: Jenny
Phone: 8675309
    age: 35
```

## Java 12
### Switch Statements
Switch statements in java 12 were introduced as preview feature which was later added as permanent feature in Java 14

### String Changes

##### Indenting Strings
Inserts 'n' number of space characters
```Java
public class IndentExample {
  public static void main(String[] args) {
      String str = "a test string";
      System.out.println(str);
      System.out.println(str.length());
      System.out.println("-- indented string --");
      String indentedStr = str.indent(5);
      System.out.println(indentedStr);
      System.out.println(indentedStr.length());
  }
}
```
```
a test string
13
-- indented string --
     a test string

19
```
##### Transforming Strings
Allows us to apply a lambda function to string.

```Java
public class TransformExample {
  public static void main(String[] args) {
      String str = "1000";
      Integer integer = str.transform(Integer::parseInt);
      System.out.println(integer);
  }
}
```
```
1000
```
### Compact Number Formatting support
##### Compact Formatting
```Java
package com.logicbig.example;

import java.text.NumberFormat;
import java.util.List;
import java.util.Locale;
import java.util.stream.IntStream;

public class CompactNumberFormatExample {
  public static void main(String[] args) {
      formatForLocale(Locale.US);
      formatForLocale(Locale.GERMANY);
  }

  private static void formatForLocale(Locale locale) {
      List<Integer> numbers = List.of(1000, 1000000, 1000000000);
      System.out.printf("-- SHORT format for locale=%s --%n", locale);
      numbers.stream().forEach((num) -> {
          NumberFormat nf = NumberFormat.getCompactNumberInstance(locale, NumberFormat.Style.SHORT);
          String format = nf.format(num);
          System.out.println(format);
      });
      System.out.printf("-- LONG format for locale=%s --%n", locale);
      numbers.stream().forEach((num) -> {
          NumberFormat nf = NumberFormat.getCompactNumberInstance(locale, NumberFormat.Style.LONG);
          String format = nf.format(num);
          System.out.println(format);
      });
  }
}
```
```
-- SHORT format for locale=en_US --
1K
1M
1B
-- LONG format for locale=en_US --
1 thousand
1 million
1 billion
-- SHORT format for locale=de_DE --
1.000
1 Mio.
1 Mrd.
-- LONG format for locale=de_DE --
1 Tausend
1 Million
1 Milliarde
```
[Other notable features](https://www.logicbig.com/tutorials/core-java-tutorial/java-12-changes.html)
