# Data Engineering Coding Challenges

## Docker - Run End To End - Generate Fixed Width File And Convert To CSV

`docker build -t justinbarton:0.1 .`

`docker run --rm -v "$PWD":/tmp justinbarton:0.1`

## Python - Test

`python -m pytest`

## Python - Generate Fixed Width File

- Example, using spec file :

`python generate_fwf.py --num_lines 100 --spec_file ./fixed_width/spec.json --output_file fwf.txt`

- Example, using parameters:

`python generate_fwf.py --header f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 --num_lines 100 --offsets 3 12 3 2 13 1 10 13 3 13 --output_file fwf.txt`

## Python - Convert Fixed Width File To CSV

- Example, using spec file:

`python fwf_to_csv.py --input_file fwf.txt --output_file output.csv --spec_file ./fixed_width/spec.json`

## Background info

### Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

### Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file. 
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding



