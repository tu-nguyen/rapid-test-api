import sys
import json
import argparse


SIMPLE_MAPPING = {
    "FastAPI": {
        "default": "@app.get(\"/\")\ndef read_default():\n\t\treturn \"Hello, World!\"",
        "string": """@app.get(\"/{route}\")\ndef read_{route}():\n\t\treturn \"{endpoint}\"""",
        "json": """@app.get(\"/{route}\")\ndef read_{route}():\n\t\treturn {endpoint}""",
    },
    "flask": {
        "default": "@app.route(\"/\")\ndef read_default():\n\t\treturn \"Hello, World!\"",
        "string": """@app.route(\"/{route}\")\ndef {route}():\n\t\treturn \"{endpoint}\"""",
        "json": """@app.route(\"/{route}\")\ndef {route}():\n\t\treturn {endpoint}""",
    },
}

port = 5000


def simple_route(app, endpoints):
    if not app:
        raise Exception

    try:
        cl = app.title
    except AttributeError:
        cl = "flask"

    if not endpoints or (endpoints and ("" not in endpoints or "/" not in endpoints)):
        exec(SIMPLE_MAPPING[cl]["default"])

    if endpoints:
        for route, endpoint in endpoints.items():
            if isinstance(endpoint, str):
                exec(SIMPLE_MAPPING[cl]["string"].format(route=route, endpoint=endpoint))
            elif isinstance(endpoint, dict):
                exec(SIMPLE_MAPPING[cl]["json"].format(route=route, endpoint=endpoint))


def init_fastapi(endpoints=None, models=None):
    import uvicorn
    from fastapi import FastAPI

    app = FastAPI()

    simple_route(app, endpoints=endpoints)

    uvicorn.run(app, port=port)


def init_flask(endpoints=None, models=None):
    from flask import Flask

    app = Flask(__name__)

    simple_route(app, endpoints=endpoints)

    app.run(debug=True, port=port)


def main():
    parser = argparse.ArgumentParser(description="A rapid API prototyping application")
    parser.add_argument("--fastapi", action="store_true", help="Use FastAPI")
    parser.add_argument("--flask", action="store_true", help="Use Flask")
    parser.add_argument("-p", "--port", type=str, default=port, help="Choose port to use")
    parser.add_argument("-m", "--model", type=str, help="Use JSON file to generate models")
    parser.add_argument("-e", "--endpoint", type=str, help="Use JSON file to generate endpoints")
    args = parser.parse_args()

    if args.fastapi and args.flask:
        print("Cannot use both at the same time!")

    endpoints = None
    if args.endpoint:
        try:
            with open(f"{args.endpoint}") as f:
                endpoints = (json.load(f))
        except Exception:
            print(f"Error loading json file at {args.endpoint}")
    else:
        print("Warning: No additional endpoint given, only /hello will be generated")

    models = None
    if args.model:
        try:
            with open(f"{args.model}") as f:
                models = (json.load(f))
        except Exception:
            print(f"Error loading json file at {args.model}")

    if not args.fastapi and not args.flask:
        args.flask = True

    if args.fastapi:
        init_fastapi(endpoints, models)

    if args.flask:
        init_flask(endpoints, models)


if __name__ == "__main__":
    main()
