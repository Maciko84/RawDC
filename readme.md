# RawDC
> [!CAUTION]
> You need to have python version 3.5 ( Or Higher ) and Git to Run & Clone this repository.
## Cloning
to start working with `RawDC` format you need to clone this repository with following git command:
```
git clone https://github.com/Maciko84/RawDC.git
```
next, you need to install `jsonc-parser` from pip:
```
pip install jsonc-parser
```
### Done!

## RawDC format
RawDC format is a JsonC. There is a sample code showcasing every node:
```jsonc
{
    "rawtext": [ 
        {
            "type": "PLAIN_TEXT", // Node of type PLAIN_TEXT
            "content": [
                "Hello, this is a sample message in the RawDC format.",
                "We can write MULTIPLE LINES :clap:"
            ]
        },
        {
            "type": "EMOJI_TEXT", // Node of type EMOJI_TEXT
            "content": [
                "Have a nice day!",
                "Made by Maciko84"
            ]
        },
        {
            "type": "USER_MENTION", // Node of type USER_MENTION
            "content": [
                "1021057577339080744",
                "678344927997853742"
            ]
        },
        {
            "type": "ROLE_MENTION", // Node of type ROLE_MENTION
            "content": [
                "1156582076456374343"
            ]
        },
        {
            "type": "CHANNEL", // Node of type CHANNEL
            "content": [
                "169256939211980800"
            ]
        },
        {
            "type": "TITLE", // Node of type TITLE
            "content": [
                "Message of the Day",
                "IMPORTANT"
            ]
        }
    ]
}
/*
Multi
Line
Comment!
*/
```
To run your code use following command in cloned repository directory:
```
python . --input <path to jsonc file> -o <path to output txt file>
```

## Modding
You can add own node types by adding them into `nodes.py` file, for example:
```py
@Node("PLAIN_TEXT")
def NODE_PLAIN_TEXT(content: list[str]):
    return '\n'.join(content) + '\n'

```

# HAPPY MESSAGE WRITING!