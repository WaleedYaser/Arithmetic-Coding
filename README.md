# Arithmatic Coding
My implementation for My implementation for Arithmetic Coding algorithm.

## Getting Started
You can view [__testSample.py__](testSample.py) code to get an idea about how to use the __ArithmaticCoding__ class.

### Prerequisites
* [Python 2.7](https://www.python.org/downloads/)

## Basic Arithmetic Coding Algorithm
I have implemented the algorithm from [_Fundamentals of Multimedia_](https://books.google.com.eg/books/about/Fundamentals_of_Multimedia.html?id=R6vBBAAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false) book, the
algorithms are _Algorithm 7.5_, _Procedure 7.2_, _Algorithm 7.6_.

### Arithmetic Coding Encoder
```
BEGIN
  low = 0.0; high = 1.0; range = 1.0;
  initialize symbol;     // so symbol != terminator

  while (symbol != terminator)
  {
    get (symbol);
    low = low + range * Range_low(symbol);
    high = low + range * Range_high(symbol);
    range = high - low;
  }
  output a code so that low <= code < high;
END
```

### Generating Codeword for Encoder
```
BEGIN
  code = 0;
  k = 1;
  while (value(code) < low)
  {
    assign 1 to the kth binary fraction bit;
    if (value(code) > high)
      replace the kth bit by 0;
    k = k + 1;
  }
END
```
### Arithmetic Coding Decoder
```
BEGIN
  get binary code and convert to decimal value = value(code);
  Do
  {
    find a symbol s so that
      Range_low(s) <= value < Range_high(s);
    output s;
    low = Rang_low(s);
    high = Range_high(s);
    range = high - low;
    value = [value - low] / range;
  }
  Until symbol s is a terminator
END
```

## Notes
I have not handled any exceptions, just the basic algorithm.

## References
* [_Fundamentals of Multimedia_](https://books.google.com.eg/books/about/Fundamentals_of_Multimedia.html?id=R6vBBAAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
