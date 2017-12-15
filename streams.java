// import java.util.stream;

public class Test {
    public void showMap() {
        Stream.of(1, 2, 3)
            .map(num -> num * num)
            .forEach(System.out::println);
    }
}
