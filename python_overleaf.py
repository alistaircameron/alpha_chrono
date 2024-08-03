# Overleaf Version.

# Toggle this between "alpha" and "chrono". "alpha" will sort alphabetically, "chrono" will sort chronologically.
alpha_chrono = "chrono" 

# Define the patterns to search for
patterns = [
    r'\\cite\{([^}]*)\}',
    r'\\citep\{([^}]*)\}',
    r'\\citet\{([^}]*)\}'
]

import re
def clean_cites(tex_file = "tex_file", patterns = [r'\\cite\{([^}]*)\}'], alpha_chrono = "alpha"):
    for pattern in patterns:

        # Find all occurrences of the pattern
        matches = list(re.finditer(pattern, tex_file))

        # Loop through the matches in reverse order
        for match in matches[::-1]:
            # Get the start and end positions of the occurrence
            start, end = match.span()

            if match:
                raw = match.group(1) if match.group(1) else match.group(2)
                raw = raw.split(", ")

                if alpha_chrono == "chrono":
                    years = [re.search(r'\d{4}', x).group() for x in raw]
                    edited = [x for _, x in sorted(zip(years, raw))]

                if alpha_chrono == "alpha":
                    edited = sorted(raw)

                # Extract the literal part of the pattern
                literal_string = re.sub(r'\(\[\^\}\]\*\)', '', pattern)

                # Replace double backslashes with a single backslash
                literal_string = literal_string.replace('\\{', '{').replace('\\}', '').replace('\\\\', '\\')

                tex_file = tex_file[:start] + literal_string + ", ".join(edited) + "}" + tex_file[end:]

    return tex_file

    
with open("main.tex", "r") as f:
    tex_file = f.read()

tex_file = clean_cites(tex_file, patterns, alpha_chrono)

with open("corrected_citations.tex", "w") as f:
    f.write(tex_file)