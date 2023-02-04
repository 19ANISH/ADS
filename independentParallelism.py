print("Operations that are not depending on each other can be executed in parallel at different processors. This is called as Independent Parallelism.
For example, in the expression r1 ⋈ r2 ⋈ r3 ⋈ r4, the portion r1 ⋈ r2 can be done in one processor, and r3 ⋈ r4 can be performed in the other processor. Both results can be pipelined into the third processor to get the final result.
Disadvantages:
Does not work well in case of high degree of parallelism.")