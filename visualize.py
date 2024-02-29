from automata.pda.npda import NPDA
from automata.base.exceptions import RejectionException
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg


class PushDownAutomata:
    def create_npda(self,
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

    def validate_npda(self, npda):
        if npda.validate():
            return False
        else:
            npda.show_diagram(path="static/npda/diagram.png")
            return True

    def simulate_npda(self, input_string, npda):
        is_accepted = npda.accepts_input(input_string)

        plot_path = f"static/npda/tests/test-{input_string}.png"

        if is_accepted:
            npda.show_diagram(input_str=input_string, path=plot_path, with_stack=True)
            return f"Input: {input_string} is accepted!"

        else:
            print("PDA rejected because of the following reason: ")
            return f"Input: {input_string} is not accepted!"
