
from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('tmux','tmux',[(BasisPairProgrammingView,[VastmakenAanEenSessieView]),(BeeindigenVanEenBestaandeSessieView,[LosmakenVanEenSessieView,NamedSessionsMakenView]),(BufferDoorzoekenView,[DoorOutputScrollenCopyModeView]),(BufferStackView,[KopierenEnPlakkenView]),(CommandDelayView,[TmuxConfigurerenView]),(CommandInMeerderePanesUitvoerenView,[PanesMakenEnNavigerenView,CommandModeActiverenView]),(CommandModeActiverenView,[CommandPrefixView]),(CommandPrefixView,[TmuxInstallerenView]),(ConfiguratieKleurenView,[TmuxConfigurerenView]),(CopyBufferOpslaanView,[KopierenEnPlakkenView]),(CopyModeKeyTableView,[KeyTablesView]),(CustomConfiguratiefileGebruikenView,[TmuxConfigurerenView]),(DoorOutputScrollenCopyModeView,[NamedSessionsMakenView]),(EenVolledigPaneKopierenView,[KopierenEnPlakkenView]),(GroupedSessionsView,[BasisPairProgrammingView]),(HooksView,[]),(IndexenVoorWindowsEnPanesInstellenView,[TmuxConfigurerenView]),(IngebouwdePaneLayoutsGebruikenView,[PanesMakenEnNavigerenView]),(InhoudVanPaneNaarFileSchrijvenView,[CopyBufferOpslaanView,EenVolledigPaneKopierenView]),(KeyTablesView,[CommandPrefixView]),(KopierenEnPlakkenView,[DoorOutputScrollenCopyModeView]),(LosmakenVanEenSessieView,[CommandPrefixView]),(MouseModeView,[TmuxConfigurerenView]),(NamedSessionsMakenView,[TmuxInstallerenView]),(OptiesDefaultShortcutsBekijkenView,[]),(OverzichtWindowsEnSessiesView,[LosmakenVanEenSessieView,WindowsMakenNavigerenBasisSluitenView]),(PairProgrammingView,[VastmakenAanEenSessieView]),(PairenMetVerschillendeAccountsView,[BasisPairProgrammingView]),(PaneOpenenInHuidigeDirectoryView,[PanesMakenEnNavigerenView]),(PaneTijdelijkMaximaliserenView,[CommandModeActiverenView,PanesMakenEnNavigerenView]),(PaneVensterView,[PanesMakenEnNavigerenView]),(PanesMakenEnNavigerenView,[WindowsMakenNavigerenBasisSluitenView]),(PanesSluitenView,[PanesMakenEnNavigerenView]),(PanesVerplaatsenView,[VensterPaneView]),(SendCommandView,[CommandModeActiverenView]),(StatusLineItemsView,[TmuxConfigurerenView]),(TmateView,[GroupedSessionsView]),(TmuxCommandsUitvoerenBuitenEenSessieView,[VastmakenAanEenSessieView,CommandModeActiverenView]),(TmuxConfigurerenView,[PanesMakenEnNavigerenView,CommandModeActiverenView]),(TmuxInstallerenView,[WatIsTmuxView]),(VastmakenAanEenSessieView,[LosmakenVanEenSessieView]),(VensterPaneView,[CommandModeActiverenView,PanesMakenEnNavigerenView]),(VenstersOfPanesMetEenCommandoView,[NamedSessionsMakenView,PanesMakenEnNavigerenView]),(WatIsTmuxView,[]),(WindowZoekenOpTitelView,[WindowsMakenNavigerenBasisSluitenView]),(WindowsMakenNavigerenBasisSluitenView,[CommandPrefixView])])
