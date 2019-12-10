import argparse
import jinja2
import glob

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--template", dest="templ")

args = parser.parse_args()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("C:\\Users\\johng\\Downloads\\Copy")
)
template = env.get_template(args.templ)
print(template.render(idoc_date="TestTestTestTestTestTestTestTestTestTestTestTest"))


# for filename in glob.glob("**/*.xml", recursive=True):
#     print(filename)