import argparse

# Checks that the provided tag follows desired scheme : X.Y.Z, where X, Y and Z are integeres. 


def CheckTag(tag):
    # Check for letters
    if(any(c.isalpha() for c in tag)): 
        raise Exception("Exception: Tag must only contain numbers separated by dots, i.e 1.0.2, no letters allowed.")
    
    



if __name__ == "__main__":

    # Establish parser
    parser = argparse.ArgumentParser(
        description= "Check if the repository tag follows the guidelines for build."
    )

    parser.add_argument(
        "--tag",
        required=True,
        type=str,
        help="The tag obtained from the GITHUB_REF variable"
        )

    args = parser.parse_args()
    
    try:
        CheckTag(args.tag)

    except Exception  as e:
        print(e)
        exit(1)