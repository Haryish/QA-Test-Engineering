# Comprehensive Java Interview Guide: Theory & Code Examples

## 1. Java Basics

**What is Java? Explain its features.**
Java is a high-level, object-oriented, and platform-independent programming language. Features include: Object-Oriented, Simple, Secure, Platform-Independent, Robust, Multithreaded, and Distributed.

**Why is Java platform independent?**
Java code is compiled into bytecode (.class file). This bytecode is not native to any processor; instead, the Java Virtual Machine (JVM) interprets it on any operating system, executing "Write Once, Run Anywhere" (WORA).

**What is JVM, JRE, and JDK?**
*   **JDK (Java Development Kit):** The full toolkit for developing Java programs (contains JRE + development tools like `javac`).
*   **JRE (Java Runtime Environment):** Provides the environment to run Java applications (contains JVM + core libraries).
*   **JVM (Java Virtual Machine):** The engine that actually runs the bytecode line by line.

**What is bytecode?**
The intermediate representation of Java source code produced by the Java compiler (`javac`). It is executed by the JVM.

**What is the main method signature?**
```java
public static void main(String[] args) {
    // public: Accessible anywhere so JVM can invoke it
    // static: Can be invoked without creating an instance of the class
    // void: Returns no value to the JVM
    // String[] args: Command-line arguments
}
```

**Why is Java not 100% object-oriented?**
Because it uses primitive data types (like `int`, `char`, `boolean`, `double`) which are not objects, to improve performance.

**Difference between C++ and Java?**
*   **C++:** Supports pointers, multiple inheritance via classes, manual memory management.
*   **Java:** No pointers (for security), no multiple inheritance via classes, automatic Garbage Collection.

**What are identifiers and keywords?**
*   **Identifier:** Names given to variables, methods, classes.
*   **Keyword:** Reserved words with predefined meanings (e.g., `class`, `public`, `int`).

**What is a class and object?**
*   **Class:** A blueprint/template containing attributes and behaviors.
*   **Object:** A physical reality or instance of a class.

**What is a constructor? Types?**
A special method used to initialize objects. It has the same name as the class and no return type.
*   **Default Constructor:** No arguments.
*   **Parameterized Constructor:** Takes arguments to initialize with specific values.

```java
class Car {
    String color;
    // Default Constructor
    Car() { color = "Red"; }
    // Parameterized Constructor
    Car(String c) { color = c; }
}
```

---

## 🔥 2. OOPs Concepts

**What are the 4 pillars of OOP?**
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

**What is encapsulation? Real-time example?**
Wrapping data (variables) and code (methods) together as a single unit. It hides the internal state and requires all interactions to be performed through an object's methods.
*Example:* A Bank Account where balance is hidden (`private`) and accessed via `deposit()` and `withdraw()` methods.
```java
class BankAccount {
    private double balance; // Hidden data
    
    public double getBalance() { return balance; }
    public void setBalance(double balance) { this.balance = balance; }
}
```

**What is inheritance? Types?**
Acquiring properties and behaviors from a parent class. Types in Java: Single, Multilevel, Hierarchical. (Multiple is supported only via Interfaces).
```java
class Animal { void eat() { System.out.println("Eating"); } }
class Dog extends Animal { void bark() { System.out.println("Barking"); } } // Single Inheritance
```

**What is polymorphism?**
The ability of a single action to occur in different forms.
*   **Compile-time (Method Overloading):** Same method name, different parameters in the same class.
*   **Runtime (Method Overriding):** Same method signature in parent and child class.

```java
// Overloading (Compile-time)
void add(int a, int b) {}
void add(int a, int b, int c) {}

// Overriding (Runtime)
class Parent { void print() { System.out.println("Parent"); } }
class Child extends Parent { 
    @Override void print() { System.out.println("Child"); } 
}
```

**What is abstraction?**
Hiding implementation details and showing only functionality to the user (achieved via abstract classes or interfaces).
```java
abstract class Vehicle {
    abstract void start(); // No implementation
}
```

**Abstraction vs Encapsulation:**
*   **Abstraction:** Solves the problem at the design level (hiding details).
*   **Encapsulation:** Solves the problem at the implementation level (hiding data).

**What is `super` and `this` keyword?**
*   `this`: Refers to the current class instance.
*   `super`: Refers to the immediate parent class instance.

---

## 🔥 3. Data Types & Variables

**What are primitive data types?**
Predefined types holding basic values: `byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char`.

**What is type casting?**
Converting one primitive type to another.
*   **Implicit (Widening):** Smaller to larger type (e.g., `int` -> `double`). Automatic.
*   **Explicit (Narrowing):** Larger to smaller type. Requires manual casting (e.g., `int x = (int) 10.5;`).

**What are variables? (Local, Instance, Static)**
*   **Local:** Declared inside a method, destroyed when the method exits.
*   **Instance:** Declared inside a class but outside methods. Unique to each object.
*   **Static:** Declared with `static` keyword. Shared among all instances of the class.

**Difference between static and non-static variables?**
Static variables belong to the class and are loaded once. Non-static variables belong to objects and allocate memory per object creation.

**What is the `final` keyword?**
Used to restrict the user.
*   Variable: Cannot change value (constant).
*   Method: Cannot be overridden.
*   Class: Cannot be inherited.

---

## 🔥 4. Strings

**Difference between String, StringBuilder, StringBuffer**
*   **String:** Immutable (cannot change). Stored in String Pool.
*   **StringBuffer:** Mutable, Synchronized (Thread-safe, slower).
*   **StringBuilder:** Mutable, Non-synchronized (Not thread-safe, faster).

**Why String is immutable?**
For security, synchronization (thread-safety), caching, and performance optimization.

**What is String pool?**
A special storage area in the Java Heap memory where String literals are stored to optimize memory.

**Difference between `==` and `.equals()`**
*   `==`: Compares memory object references.
*   `.equals()`: Compares the actual content of the objects.

**What is `intern()` method?**
It checks if the string exists in the String pool. If yes, it returns the reference; if not, it adds it to the pool.

**How to reverse a string?**
```java
String str = "hello";
// Using StringBuilder
String reversed = new StringBuilder(str).reverse().toString();

// Manually
String rev = "";
for (int i = str.length() - 1; i >= 0; i--) {
    rev += str.charAt(i);
}
```

---

## 🔥 5. Collections Framework

**What is the Collection framework?**
An architecture to store and manipulate a group of objects. Provides ready-made interfaces (List, Set, Queue) and classes (ArrayList, HashSet, LinkedList, etc.).

**List vs Set vs Map**
*   **List:** Ordered, allows duplicates.
*   **Set:** Unordered, does NOT allow duplicates.
*   **Map:** Stores key-value pairs (keys must be unique).

**ArrayList vs LinkedList**
*   **ArrayList:** Uses a dynamic array. Fast for retrieval, slow for manipulation.
*   **LinkedList:** Uses a doubly linked list. Fast for manipulation (insert/delete), slow for retrieval.

**HashSet vs LinkedHashSet vs TreeSet**
*   **HashSet:** No guarantee of order, allows one null.
*   **LinkedHashSet:** Maintains insertion order.
*   **TreeSet:** Sorts elements in ascending order.

**HashMap vs Hashtable vs TreeMap**
*   **HashMap:** Not synchronized, allows one null key.
*   **Hashtable:** Synchronized (legacy), no null keys/values allowed.
*   **TreeMap:** Sorted based on keys.

**What is Iterator? Iterator vs ListIterator?**
*   **Iterator:** Traverse collections in the forward direction.
*   **ListIterator:** Traverse Lists in *both* forward and backward directions and allows modification.

**Comparable vs Comparator**
*   **Comparable:** "Natural" sorting order. Modifies the class itself (`compareTo()` method).
*   **Comparator:** Custom sorting order. External class/logic (`compare()` method).

---

## 🔥 6. Exception Handling

**What is an exception?**
An unwanted or unexpected event occurring during runtime that disrupts the normal flow of the program.

**Types of exceptions:**
*   **Checked:** Checked at compile-time (e.g., `IOException`, `SQLException`).
*   **Unchecked:** Checked at runtime. Inherit from `RuntimeException` (e.g., `NullPointerException`, `ArithmeticException`).

**throw vs throws:**
*   `throw`: Used to explicitly throw an exception object from within a method.
*   `throws`: Used in the method signature to declare that the method might throw exceptions.

**try-catch-finally:**
*   `try`: Code that might raise an exception.
*   `catch`: Code to handle the exception.
*   `finally`: Code that executes *always*, whether exception occurs or not (used for cleanup like closing files).

**Can the finally block be skipped?**
Yes, if `System.exit(0)` is called or if the JVM crashes before reaching it.

**Custom exception:**
```java
class InvalidAgeException extends Exception {
    public InvalidAgeException(String msg) { super(msg); }
}
// Throwing: throw new InvalidAgeException("Age < 18");
```

---

## 🔥 7. Keywords

*   **static:** Belongs to the class rather than instances.
*   **final:** Constant/cannot be changed or overridden/inherited.
*   **this:** Reference to the current object.
*   **super:** Reference to parent class object.
*   **abstract:** Used to declare abstract classes/methods (needs implementation in child).
*   **synchronized:** Locks a block/method to a single thread at a time.
*   **volatile:** Ensures visibility of variable changes across multiple threads.
*   **transient:** Prevents a variable from being serialized.

---

## 🔥 8. Access Modifiers

Determines the scope/visibility of fields, methods, classes.
*   **public:** Accessible entirely everywhere.
*   **protected:** Accessible within the same package and in subclasses in other packages.
*   **default (no keyword):** Accessible only within the same package.
*   **private:** Accessible only within the same class.

---

## 🔥 9. Interfaces & Abstract Classes

**What is an interface?**
A blueprint of a class containing only abstract methods (until Java 8) and public static final variables. Used for 100% abstraction and multiple inheritance.

**What is an abstract class?**
A class declared with the `abstract` keyword. It can have both abstract (no body) and concrete methods. Cannot be instantiated.

**Interface vs Abstract Class**
*   **Interface:** Supports multiple inheritance, methods are public abstract by default. Variables are static final.
*   **Abstract Class:** Doesn't support multiple inheritance, can have state (instance variables), can have constructors.

**Multiple inheritance in Java:**
Java classes do not support multiple inheritance to avoid ambiguity (the Diamond Problem). However, a class can implement multiple interfaces.
```java
interface A { void run(); }
interface B { void run(); }
class C implements A, B {
    public void run() { System.out.println("Running"); }
}
```

---

## 🔥 10. Multithreading

**What is a thread?**
A lightweight subprocess; the smallest unit of processing.

**Process vs Thread?**
A process is an executing program (heavyweight, independent memory space). A thread is a path of execution within a process (lightweight, shared memory).

**How to create thread?**
1. By extending the `Thread` class.
2. By implementing the `Runnable` interface (Preferred).
```java
class MyThread implements Runnable {
    public void run() { System.out.println("Thread running"); }
}
new Thread(new MyThread()).start();
```

**What is synchronization?**
The capability to control the access of multiple threads to any shared resource to prevent inconsistent results.

**Thread lifecycle:**
New -> Runnable -> Running -> Blocked/Waiting -> Terminated.

**sleep() vs wait()**
*   `sleep(ms)`: Pauses thread execution. DOES NOT release the lock. (From `Thread` class).
*   `wait()`: Pauses execution and RELEASES the lock. Wakes up via `notify()`. (From `Object` class, called within synchronized blocks).

---

## 🔥 11. File Handling

**What is the File class?**
An abstract representation of file and directory pathnames. (From `java.io.File`).

**BufferedReader vs FileReader:**
*   `FileReader`: Reads characters from a file one by one (slower).
*   `BufferedReader`: Wraps around FileReader to read chunks of data into a buffer, improving performance.

**What is serialization?**
The process of converting an object's state into a byte stream so it can be saved to a file or sent over a network. Reverse process is *Deserialization*.

---

## 🔥 12. Java Memory Management

**What is heap and stack?**
*   **Heap:** Where all objects are created in memory at runtime. Managed by Garbage Collector.
*   **Stack:** Where method execution frames and local primitive variables are stored.

**What is garbage collection?**
A daemon thread (JVM feature) that automatically destroys unused objects to free up heap memory (e.g., objects without references).

**What is a memory leak?**
When objects are no longer in use by the application, but the Garbage Collector cannot remove them because they still have active references holding them.

---

## 🔥 13. Important Concepts (Interview Favorites)

**What is a singleton class?**
A class that guarantees only one instance exists across the JVM.
```java
class Singleton {
    private static Singleton instance;
    private Singleton() {} // private constructor
    public static Singleton getInstance() {
        if (instance == null) instance = new Singleton();
        return instance;
    }
}
```

**What is an immutable class?**
A class whose state cannot be changed once created (like `String`). Provide `final` variables, `private` fields, and don't provide setters.

**What is a marker interface?**
An interface with no methods/fields. Used to signal the JVM to treat the class differently (e.g., `Serializable`, `Cloneable`).

**What is a wrapper class?**
Classes that wrap primitive types into an object (e.g., `int` -> `Integer`, `char` -> `Character`). Required for Collections which only handle objects.

**Autoboxing and unboxing:**
*   **Autoboxing:** Automatic conversion of primitive to wrapper (`int` -> `Integer`).
*   **Unboxing:** Automatic conversion of wrapper to primitive (`Integer` -> `int`).

**What is reflection?**
An API that allows examining or modifying the behavior of classes, interfaces, methods, and variables at runtime.

---

## 🔥 14. Java 8 Features

**Lambda Expressions:**
A concise way to represent anonymous functions.
```java
// Without lambda
Runnable r = new Runnable() { public void run() { System.out.println("Running"); } };
// With lambda
Runnable r2 = () -> System.out.println("Running");
```

**Functional Interfaces:**
An interface with exactly ONE abstract method (e.g., `Runnable`, `Callable`). Can be annotated with `@FunctionalInterface`.

**Streams & forEach:**
A sequence of elements allowing sequential/parallel operations (filter, map, reduce).
```java
List<String> list = Arrays.asList("Apple", "Banana", "Apricot");
list.stream()
    .filter(s -> s.startsWith("A"))
    .forEach(s -> System.out.println(s)); // Prints Apple, Apricot
```

**Default Methods:**
Java 8 allowed interfaces to have implemented methods using the `default` keyword to prevent breaking existing classes.

---

## 🔥 15. Arrays

**Difference between array and ArrayList?**
*   **Array:** Fixed size, can hold primitives and objects, faster in some specific static scenarios.
*   **ArrayList:** Resizable (dynamic length), holds ONLY objects (wrappers), provides many utility methods.

**How to sort an array?**
```java
int[] arr = {5, 2, 8, 1};
Arrays.sort(arr); // Quick built-in way
```

**Find duplicates in an array?**
```java
int[] arr = {1, 2, 3, 2, 4, 1};
HashSet<Integer> seen = new HashSet<>();

for (int num : arr) {
    if (!seen.add(num)) {
        System.out.println("Duplicate found: " + num);
    }
}
```
