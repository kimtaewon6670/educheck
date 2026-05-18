from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Application main window view."""

    MENU_ITEMS = (
        "대시보드",
        "문제은행 관리",
        "진단 문제 풀이",
        "맞춤형 문제 풀이",
        "오답 복습",
        "학습 분석",
    )

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduCheck")
        self.resize(1200, 800)

        self.sidebar = QListWidget()
        self.content_stack = QStackedWidget()

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        central_widget = QWidget()
        root_layout = QHBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        sidebar_container = self._create_sidebar()
        content_container = self._create_content_area()

        root_layout.addWidget(sidebar_container)
        root_layout.addWidget(content_container, 1)

        self.setCentralWidget(central_widget)
        self.sidebar.setCurrentRow(0)

    def _create_sidebar(self):
        container = QFrame()
        container.setObjectName("sidebar")
        container.setFixedWidth(220)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 20, 16, 20)
        layout.setSpacing(16)

        title = QLabel("EduCheck")
        title.setObjectName("sidebarTitle")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.sidebar.setObjectName("navigationList")
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sidebar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for menu_name in self.MENU_ITEMS:
            item = QListWidgetItem(menu_name)
            item.setTextAlignment(Qt.AlignVCenter)
            self.sidebar.addItem(item)

        layout.addWidget(title)
        layout.addWidget(self.sidebar)

        return container

    def _create_content_area(self):
        container = QFrame()
        container.setObjectName("contentArea")

        layout = QVBoxLayout(container)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(0)

        for menu_name in self.MENU_ITEMS:
            self.content_stack.addWidget(self._create_placeholder_page(menu_name))

        layout.addWidget(self.content_stack)

        return container

    def _create_placeholder_page(self, title):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(f"{title} 화면")
        label.setObjectName("placeholderTitle")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        return page

    def _connect_signals(self):
        self.sidebar.currentRowChanged.connect(self.content_stack.setCurrentIndex)
