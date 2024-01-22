from automata.pda.npda import NPDA
from automata.base.exceptions import RejectionException
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class PushDownAutomata:
    def create_npda(
        input_states,
        input_alphabets,
        input_stack_alphabets,
        input_transitions,
        input_initial_state,
        input_initial_stack_symbol,
        input_final_states,
        input_acceptance_mode,
    ):
        npda = NPDA(
            states=input_states,
            input_symbols=input_alphabets,
            stack_symbols=input_stack_alphabets,
            transitions=input_transitions,
            initial_state=input_initial_state,
            initial_stack_symbol=input_initial_stack_symbol,
            final_states=input_final_states,
            acceptance_mode=input_acceptance_mode,
        )
        return npda

    def validate_npda(npda):
        if npda.validate():
            return False
        else:
            npda.show_diagram(path="static/npda/diagram.png")
            return True

    input_strings = "input input string here from html webpage in the form of a list"

    def simulate_npda(input_strings, npda):
        for test_case in input_strings:
            is_accepted = npda.accepts_input(test_case)

        plot_path = f"static/npda/tests/test-{test_case}.png"

        if is_accepted:
            npda.show_diagram(input_str=test_case, path=plot_path, with_stack=True)
            return f"Input: {test_case} is accepted!"

        else:
            npda.show_diagram(input_str=test_case, path=plot_path, with_stack=True)
            return f"Input: {test_case} is not accepted!"
