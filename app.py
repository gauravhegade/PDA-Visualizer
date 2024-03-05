from flask import Flask, render_template, request
from visualize import PushDownAutomata as pda
from html2text import html2text
import ast

app = Flask("PDA Visualizer")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # get the states in the automata
        states = request.form.get("input_states")
        states = states.replace(" ", "")
        states = set(states.split(",")) if states else None

        # get the input symbols in the automata
        input_symbols = request.form.get("input_alphabets")
        input_symbols = input_symbols.replace(" ", "")
        input_symbols = set(input_symbols.split(",")) if input_symbols else None

        # get the stack symbols in the automata
        stack_symbols = request.form.get("stack_symbols")
        stack_symbols = stack_symbols.replace(" ", "")
        stack_symbols = set(stack_symbols.split(",")) if stack_symbols else None

        # get the transitions of the automata in json format
        transitions_str = request.form.get("transitions")
        transitions_str = html2text(transitions_str)
        try:
            transitions = ast.literal_eval(transitions_str)

        except (ValueError, SyntaxError) as e:
            print(f"Error parsing input: {e}")

        initial_state = request.form.get("initial_state")
        initial_state = initial_state.replace(" ", "") if initial_state else None

        initial_stack_symbol = request.form.get("initial_stack_symbol")
        initial_stack_symbol = (
            initial_stack_symbol.replace(" ", "") if initial_stack_symbol else None
        )

        final_states = request.form.get("final_states")
        final_states = final_states.replace(" ", "")
        final_states = set(final_states.split(",")) if final_states else None

        acceptance_mode = request.form.get("acceptance_mode")

        # # Get input strings to test from user
        test_strings = request.form.get("test_strings")
        test_strings = test_strings.replace(" ", "")
        test_strings = list(test_strings.split(",")) if test_strings else None

        states = states
        input_symbols = input_symbols
        stack_symbols = stack_symbols
        transitions = transitions
        initial_state = initial_state
        initial_stack_symbol = initial_stack_symbol
        final_states = final_states
        acceptance_mode = acceptance_mode

        # # Debugging
        # print(
        #     "\n STATES \n",
        #     states,
        #     "\n INPUT SYMBOLS \n",
        #     input_symbols,
        #     "\n STACK SYMBOLS \n",
        #     stack_symbols,
        #     "\n TRANSITIONS \n",
        #     transitions,
        #     "\n INITIAL STATE \n",
        #     initial_state,
        #     "\n INITIAL STACK SYMBOL \n",
        #     initial_stack_symbol,
        #     "\n FINAL STATES \n",
        #     final_states,
        #     "\n ACCEPTANCE MODE \n",
        #     acceptance_mode,
        # )

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

        res = []
        if test_strings is not None:
            for test_string in test_strings:
                res.append(pda.simulate_npda(test_string, npda))

        else:
            pass

        # TODO: FIND A BETTER WAY TO PRINT THE RESULT
        # ONE WAY: ATTACH THE TEST CASE RESULT TO THE TEST CASE ITSELF AND USE IT IN PRINTING THE DIAGRAMS
        # ANOTHER WAY: NEED TO BE THOUGHT OF

        context = {
            "npda": "static/npda/diagram.png",
            "result": res,
            "test_strings": test_strings,
        }

        return render_template("index.html", context=context)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8123)
