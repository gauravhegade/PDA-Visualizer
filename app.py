from flask import Flask, render_template, request
from visualize import PushDownAutomata as pda

app = Flask("PDA Visualizer")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # This is the code for debugging purposes
        name = request.form.get("name")
        print(name) if name else print("No name provided")

        states = {"q0", "q1", "qf"}
        input_symbols = {"a", "b"}
        stack_symbols = {"Z", "A", "B"}
        transitions = {
            "q0": {
                "": {
                    "Z": {("qf", "")},
                    "B": {("q1", ("B"))},
                },
                "a": {
                    "Z": {("q0", ("A", "Z"))},
                    "B": {("q0", ("A", "B"))},
                },
                "b": {
                    "A": {
                        ("q0", ("B", "A")),
                    }
                },
            },
            "q1": {
                "": {"Z": {("qf", "")}},
                "a": {
                    "A": {("q1", "")},
                    "B": {("q1", "")},
                },
            },
        }
        initial_state = "q0"
        initial_stack_symbol = "Z"
        final_states = {"qf"}
        acceptance_mode = "empty_stack"

        npda = pda.create_npda(
            states,
            input_symbols,
            stack_symbols,
            transitions,
            initial_state,
            initial_stack_symbol,
            final_states,
            acceptance_mode,
        )

        if pda.validate_npda(npda):
            print("NPDA validated")

        else:
            print("NPDA not validated")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8123)
