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

    def simulate_npda(input_string, npda):
        if input_string == "E":
            input_string = ""

        is_accepted = npda.accepts_input(input_string)

        if input_string == "":
            input_string = "E"
        plot_path = f"static/npda/tests/test-{input_string}.png"

        if is_accepted:
            if input_string == "E":
                input_string = ""
            npda.show_diagram(input_str=input_string, path=plot_path, with_stack=True)
            if input_string == "":
                input_string = "E"
            return True, input_string, f"{input_string} is accepted!"
        else:
            return False, input_string, f"{input_string} is not accepted!"
