import argparse
import os
import re

# Constants
ANDROID_VAR_NAME = 'BUILD_NUMBER'
IOS_VAR_NAME = 'BUILD_IOS'


# Checks that the provided tag follows desired scheme : X.Y.Z, where X, Y and Z are integeres. 

def CheckTag(tag):
    # Check for letters
    if(any(c.isalpha() for c in tag)): 
        raise Exception("Exception: Tag must only contain numbers separated by dots, i.e 1.0.2, no letters allowed.")
    else:
        print(f"Tag <{tag}> is a valid version string")

# Updates the version file. Changes string 'Version Interna' for the corresponding tag value. Increases the build counter for the iOS/Android variables.

def updateFile(path):

    # Check if path exists 
    if(not os.path.isfile(path)):
        raise Exception(f"Exception: Version/Build file <{path}> cannot be found!")
    
    else:
        print(f"Version/Build file is <{path}>")

    # Default values

    android_build_number = -1
    ios_build_number = -1

    # Read the current values

    with open(path, 'r') as f:
        readed_file = f.readlines()
        for line in readed_file:
            line = line.strip()
            if(ANDROID_VAR_NAME in line):
                android_build_number = int(re.findall(r'\d+', line)[0])
                print(f"Current Android build number is {android_build_number}")

            elif(IOS_VAR_NAME in line):
                ios_build_number = int(re.findall(r'\d+', line)[0])
                print(f"Current iOS build number is {ios_build_number}")

        
    # Check if both numbers where found
    if (android_build_number < 0):
        raise Exception(f"Exception: Android build number could not be found on <{path}>")
        
    if (ios_build_number < 0):
        raise Exception(f"Exception: iOS build number could not be found on <{path}>")
    
    with open(path, 'r') as f:
        data = f.read()

    # Update build numbers
    android_build_number +=1
    print(f"New Android build will have {android_build_number} build number")
    ios_build_number +=1
    print(f"New iOS build will have {ios_build_number} build number")

    # Write to file
    with open(path, 'w') as f:
        # Change Android build
        data = re.sub(ANDROID_VAR_NAME+" = "+r'\d+', f"{ANDROID_VAR_NAME} = {android_build_number}", data)
        # Change iOS build
        data = re.sub(IOS_VAR_NAME+" = "+r'\d+', f"{IOS_VAR_NAME} = {ios_build_number}", data)
        # Write to file
        f.write(data)




    



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
    
    parser.add_argument(
        "--version-file",
        required=True,
        type=str,
        help="File that holds the current build number and display version for the iOS/Android version."
    )

    args = parser.parse_args()
    
    # Tag-Check

    try:
        CheckTag(args.tag)

    except Exception  as e:
        print(e)
        exit(1)

    # Update version/build file
    updateFile(args.version_file)
