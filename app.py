from flask import Flask, render_template, request, redirect
from visualize import determine_pushdown_automaton as determine_pushdown_automaton
from visualize import (
    nondeterministic_pushdown_automaton as nondeterministic_pushdown_automaton,
)
from html2text import html2text
import ast

app = Flask("PDA Visualizer")


@app.route("/")
def index():
    return redirect("/npda" or "/dpda")


@app.route("/npda", methods=["POST", "GET"])
def npda():
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

        pda = nondeterministic_pushdown_automaton.create_npda(
            states,
            input_symbols,
            stack_symbols,
            transitions,
            initial_state,
            initial_stack_symbol,
            final_states,
            acceptance_mode,
        )

        if nondeterministic_pushdown_automaton.validate_npda(pda):
            print("NPDA validated")

        else:
            print("NPDA not validated")

        res = []
        if test_strings is not None:
            for test_string in test_strings:
                res.append(
                    nondeterministic_pushdown_automaton.simulate_npda(test_string, pda)
                )

        else:
            pass

        context = {
            "mode": "NPDA",
            "npda": "static/npda/diagram.png",
            "result": res,
            "test_strings": test_strings,
        }

        return render_template("index.html", context=context)

    return render_template("index.html", mode="NPDA")


@app.route("/dpda", methods=["POST", "GET"])
def dpda():
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

        pda = determine_pushdown_automaton.create_dpda(  # Use create_dpda instead of create_npda
            states,
            input_symbols,
            stack_symbols,
            transitions,
            initial_state,
            initial_stack_symbol,
            final_states,
            acceptance_mode,
        )

        if determine_pushdown_automaton.validate_dpda(
            pda
        ):  # Use validate_dpda instead of validate_npda
            print("DPDA validated")  # Update message

        else:
            print("DPDA not validated")  # Update message

        res = []
        if test_strings is not None:
            for test_string in test_strings:
                res.append(determine_pushdown_automaton.simulate_dpda(test_string, pda))

        else:
            pass

        context = {
            "mode": "DPDA",
            "dpda": "static/dpda/diagram.png",  # Update path
            "result": res,
            "test_strings": test_strings,
        }

        return render_template("index.html", context=context)

    return render_template("index.html", mode="DPDA")


if __name__ == "__main__":
    app.run(debug=True, port=8123)
