# /usr/bin/env julia1.6.1

""" install if needed
    using Pkg; Pkg.add("CSV"); Pkg.add("DataFrames"); Pkg.add("Time");
"""

using CSV
using DataFrames
using Logging


avg = 0.0
sum = 0.0
the_end = 1000
logger = SimpleLogger(open("log/test_df_jl.txt", "a+"))


function main()
    df = DataFrame(CSV.File("database/source.csv"))
    return 0
end;


for i = 0:the_end
    clock = @elapsed main()
    global sum += clock
    with_logger(logger) do
        @info(clock)
    end
end;

avg = sum/the_end
with_logger(logger) do
    @info("mean", avg)
end