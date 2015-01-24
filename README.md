# Matrix multiplication bechmark

I wanted to learn how to write modules for python in C++. In particular I 
wanted to learn how to use [Boost.Python]. I wanted a practical example to see
how it can be used and to see a real example of the speed gains.

I found in the blog of [Martin Thoma] a benchmark between python vs java vs c++ for matrix multiplication using the naive algorithm. Here I will try to extend
this benchmark by creating a python module in c++ and calling that module from python.

I wanted to do as fewer modification in the python code. In practice the
only modification I did is that I imported the module I created and run a function
`standardMatrixProduct` with the same arguments as the original python code.

The results are impressive for the effort I put. I just rewrite the function
`standardMatrixProduct` in C++ and exposed it to python using the Boost.Python library.
### Results
Here are a plot of the results:
![alt tag](https://raw.github.com/username/projectname/branch/path/to/img.png)

###Comments
I know that the matrix multiplication method is not the proper.
Probably for the matrix multiplication problem if you use python you would use [NumPy] or a similar special library.
The point here was to show how easy you can speedup your code using modules written in C++ using Boost.Python.

[Boost.Python]:http://www.boost.org/doc/libs/1_57_0/libs/python/doc/index.html
[Martin Thome]:http://martin-thoma.com/matrix-multiplication-python-java-cpp/
[NumPy]:http://www.numpy.org/