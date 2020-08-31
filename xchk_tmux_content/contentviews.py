from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class PairenMetVerschillendeAccountsView(ContentView):
    uid = 'xchk_tmux_content_pairen_met_verschillende_accounts'
    template = 'xchk_tmux_content/pairen_met_verschillende_accounts.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class NamedSessionsMakenView(ContentView):
    uid = 'xchk_tmux_content_named_sessions_maken'
    template = 'xchk_tmux_content/named_sessions_maken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class OverzichtWindowsEnSessiesView(ContentView):
    uid = 'xchk_tmux_content_overzicht_windows_en_sessies'
    template = 'xchk_tmux_content/overzicht_windows_en_sessies.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CommandModeActiverenView(ContentView):
    uid = 'xchk_tmux_content_command_mode_activeren'
    template = 'xchk_tmux_content/command_mode_activeren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class SendCommandView(ContentView):
    uid = 'xchk_tmux_content_send_command'
    template = 'xchk_tmux_content/send_command.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class LosmakenVanEenSessieView(ContentView):
    uid = 'xchk_tmux_content_losmaken_van_een_sessie'
    template = 'xchk_tmux_content/losmaken_van_een_sessie.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class EenVolledigPaneKopierenView(ContentView):
    uid = 'xchk_tmux_content_een_volledig_pane_kopieren'
    template = 'xchk_tmux_content/een_volledig_pane_kopieren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CustomConfiguratiefileGebruikenView(ContentView):
    uid = 'xchk_tmux_content_custom_configuratiefile_gebruiken'
    template = 'xchk_tmux_content/custom_configuratiefile_gebruiken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class OptiesDefaultShortcutsBekijkenView(ContentView):
    uid = 'xchk_tmux_content_opties_default_shortcuts_bekijken'
    template = 'xchk_tmux_content/opties_default_shortcuts_bekijken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class IngebouwdePaneLayoutsGebruikenView(ContentView):
    uid = 'xchk_tmux_content_ingebouwde_pane_layouts_gebruiken'
    template = 'xchk_tmux_content/ingebouwde_pane_layouts_gebruiken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class InhoudVanPaneNaarFileSchrijvenView(ContentView):
    uid = 'xchk_tmux_content_inhoud_van_pane_naar_file_schrijven'
    template = 'xchk_tmux_content/inhoud_van_pane_naar_file_schrijven.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class TmateView(ContentView):
    uid = 'xchk_tmux_content_tmate'
    template = 'xchk_tmux_content/tmate.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class TmuxCommandsUitvoerenBuitenEenSessieView(ContentView):
    uid = 'xchk_tmux_content_tmux_commands_uitvoeren_buiten_een_sessie'
    template = 'xchk_tmux_content/tmux_commands_uitvoeren_buiten_een_sessie.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CommandDelayView(ContentView):
    uid = 'xchk_tmux_content_command_delay'
    template = 'xchk_tmux_content/command_delay.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class KeyTablesView(ContentView):
    uid = 'xchk_tmux_content_key_tables'
    template = 'xchk_tmux_content/key_tables.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WindowZoekenOpTitelView(ContentView):
    uid = 'xchk_tmux_content_window_zoeken_op_titel'
    template = 'xchk_tmux_content/window_zoeken_op_titel.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VastmakenAanEenSessieView(ContentView):
    uid = 'xchk_tmux_content_vastmaken_aan_een_sessie'
    template = 'xchk_tmux_content/vastmaken_aan_een_sessie.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PanesSluitenView(ContentView):
    uid = 'xchk_tmux_content_panes_sluiten'
    template = 'xchk_tmux_content/panes_sluiten.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class KopierenEnPlakkenView(ContentView):
    uid = 'xchk_tmux_content_kopieren_en_plakken'
    template = 'xchk_tmux_content/kopieren_en_plakken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class BufferDoorzoekenView(ContentView):
    uid = 'xchk_tmux_content_buffer_doorzoeken'
    template = 'xchk_tmux_content/buffer_doorzoeken.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PaneTijdelijkMaximaliserenView(ContentView):
    uid = 'xchk_tmux_content_pane_tijdelijk_maximaliseren'
    template = 'xchk_tmux_content/pane_tijdelijk_maximaliseren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class HooksView(ContentView):
    uid = 'xchk_tmux_content_hooks'
    template = 'xchk_tmux_content/hooks.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class MouseModeView(ContentView):
    uid = 'xchk_tmux_content_mouse_mode'
    template = 'xchk_tmux_content/mouse_mode.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WatIsTmuxView(ContentView):
    uid = 'xchk_tmux_content_wat_is_tmux'
    template = 'xchk_tmux_content/wat_is_tmux.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class GroupedSessionsView(ContentView):
    uid = 'xchk_tmux_content_grouped_sessions'
    template = 'xchk_tmux_content/grouped_sessions.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class BufferStackView(ContentView):
    uid = 'xchk_tmux_content_buffer_stack'
    template = 'xchk_tmux_content/buffer_stack.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class TmuxConfigurerenView(ContentView):
    uid = 'xchk_tmux_content_tmux_configureren'
    template = 'xchk_tmux_content/tmux_configureren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class WindowsMakenNavigerenBasisSluitenView(ContentView):
    uid = 'xchk_tmux_content_windows_maken_navigeren_basis_sluiten'
    template = 'xchk_tmux_content/windows_maken_navigeren_basis_sluiten.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class BasisPairProgrammingView(ContentView):
    uid = 'xchk_tmux_content_basis_pair_programming'
    template = 'xchk_tmux_content/basis_pair_programming.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class VensterPaneView(ContentView):
    uid = 'xchk_tmux_content_venster_pane'
    template = 'xchk_tmux_content/venster_pane.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PanesMakenEnNavigerenView(ContentView):
    uid = 'xchk_tmux_content_panes_maken_en_navigeren'
    template = 'xchk_tmux_content/panes_maken_en_navigeren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class BeeindigenVanEenBestaandeSessieView(ContentView):
    uid = 'xchk_tmux_content_beeindigen_van_een_bestaande_sessie'
    template = 'xchk_tmux_content/beeindigen_van_een_bestaande_sessie.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class DoorOutputScrollenCopyModeView(ContentView):
    uid = 'xchk_tmux_content_door_output_scrollen_copy_mode'
    template = 'xchk_tmux_content/door_output_scrollen_copy_mode.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class ConfiguratieKleurenView(ContentView):
    uid = 'xchk_tmux_content_configuratie_kleuren'
    template = 'xchk_tmux_content/configuratie_kleuren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CopyModeKeyTableView(ContentView):
    uid = 'xchk_tmux_content_copy_mode_key_table'
    template = 'xchk_tmux_content/copy_mode_key_table.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PanesVerplaatsenView(ContentView):
    uid = 'xchk_tmux_content_panes_verplaatsen'
    template = 'xchk_tmux_content/panes_verplaatsen.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class StatusLineItemsView(ContentView):
    uid = 'xchk_tmux_content_status_line_items'
    template = 'xchk_tmux_content/status_line_items.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class TmuxInstallerenView(ContentView):
    uid = 'xchk_tmux_content_tmux_installeren'
    template = 'xchk_tmux_content/tmux_installeren.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CopyBufferOpslaanView(ContentView):
    uid = 'xchk_tmux_content_copy_buffer_opslaan'
    template = 'xchk_tmux_content/copy_buffer_opslaan.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PaneVensterView(ContentView):
    uid = 'xchk_tmux_content_pane_venster'
    template = 'xchk_tmux_content/pane_venster.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class IndexenVoorWindowsEnPanesInstellenView(ContentView):
    uid = 'xchk_tmux_content_indexen_voor_windows_en_panes_instellen'
    template = 'xchk_tmux_content/indexen_voor_windows_en_panes_instellen.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class CommandPrefixView(ContentView):
    uid = 'xchk_tmux_content_command_prefix'
    template = 'xchk_tmux_content/command_prefix.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))


class PairProgrammingView(ContentView):
    uid = 'xchk_tmux_content_pair_programming'
    template = 'xchk_tmux_content/pair_programming.html'
    strat = Strategy(refusing_check=TrueCheck(),accepting_check=Negation(TrueCheck()))
