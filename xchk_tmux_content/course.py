
from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('tmux','tmux',[(VensterPaneView,[CommandModeActiverenView,PanesMakenEnNavigerenView,WindowsMakenNavigerenBasisSluitenView]),(NamedSessionsMakenView,[TmuxInstallerenView]),(IngebouwdePaneLayoutsGebruikenView,[PanesMakenEnNavigerenView]),(BasisPairProgrammingView,[VastmakenAanEenSessieView]),(CopyModeKeyTableView,[KeyTablesView]),(PaneTijdelijkMaximaliserenView,[CommandModeActiverenView,PanesMakenEnNavigerenView]),(PanesVerplaatsenView,[]),(BeeindigenVanEenBestaandeSessieView,[NamedSessionsMakenView,LosmakenVanEenSessieView]),(KopierenEnPlakkenView,[DoorOutputScrollenCopyModeView]),(OptiesDefaultShortcutsBekijkenView,[]),(KeyTablesView,[CommandPrefixView]),(MouseModeView,[TmuxConfigurerenView]),(CustomConfiguratiefileGebruikenView,[TmuxConfigurerenView]),(CommandDelayView,[TmuxConfigurerenView]),(VastmakenAanEenSessieView,[LosmakenVanEenSessieView]),(CopyBufferOpslaanView,[KopierenEnPlakkenView]),(ConfiguratieKleurenView,[TmuxConfigurerenView]),(TmuxInstallerenView,[WatIsTmuxView]),(CommandPrefixView,[TmuxInstallerenView]),(IndexenVoorWindowsEnPanesInstellenView,[PanesMakenEnNavigerenView,WindowsMakenNavigerenBasisSluitenView,TmuxConfigurerenView]),(StatusLineItemsView,[TmuxConfigurerenView]),(InhoudVanPaneNaarFileSchrijvenView,[EenVolledigPaneKopierenView,CopyBufferOpslaanView]),(WatIsTmuxView,[]),(GroupedSessionsView,[BasisPairProgrammingView]),(SendCommandView,[CommandModeActiverenView]),(TmateView,[GroupedSessionsView]),(PairenMetVerschillendeAccountsView,[BasisPairProgrammingView]),(EenVolledigPaneKopierenView,[KopierenEnPlakkenView]),(CommandModeActiverenView,[CommandPrefixView]),(TmuxCommandsUitvoerenBuitenEenSessieView,[CommandModeActiverenView,VastmakenAanEenSessieView]),(DoorOutputScrollenCopyModeView,[NamedSessionsMakenView]),(PairProgrammingView,[VastmakenAanEenSessieView]),(PaneVensterView,[PanesMakenEnNavigerenView]),(WindowsMakenNavigerenBasisSluitenView,[CommandPrefixView]),(OverzichtWindowsEnSessiesView,[WindowsMakenNavigerenBasisSluitenView,LosmakenVanEenSessieView]),(LosmakenVanEenSessieView,[CommandPrefixView]),(BufferStackView,[KopierenEnPlakkenView]),(TmuxConfigurerenView,[CommandModeActiverenView,PanesMakenEnNavigerenView,WindowsMakenNavigerenBasisSluitenView]),(PanesMakenEnNavigerenView,[WindowsMakenNavigerenBasisSluitenView]),(HooksView,[]),(PanesSluitenView,[PanesMakenEnNavigerenView]),(WindowZoekenOpTitelView,[WindowsMakenNavigerenBasisSluitenView]),(BufferDoorzoekenView,[DoorOutputScrollenCopyModeView])])
