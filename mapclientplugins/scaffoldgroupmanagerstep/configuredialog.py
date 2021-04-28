import os
import json

from PySide2 import QtWidgets

from mapclientplugins.scaffoldgroupmanagerstep.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.scaffoldgroupmanagerstep.ui_group_configuredialog import Ui_MehGroupConfigureDialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigFile(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self._ui = Ui_MehGroupConfigureDialog()
        self._ui.setupUi(self)

    def get_config(self):
        cfg = dict()
        cfg['groups'] = self._ui.plainTextEdit.toPlainText().split("\n")
        return cfg


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, location=None, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        self._groups = {}
        self._location = location
        self._fileName = "groups.config"
        if self._location:
            if os.path.isfile(os.path.join(self._location, self._fileName)):
                self._ui.label_5.setText(os.path.join(self._location, self._fileName))
                self._loadConfig()

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._previousLocation = ''
        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)
        self._ui.pushButton.clicked.connect(self.__fileChooserClicked)
        self._ui.pushButton_2.clicked.connect(self.__edit)

    def __edit(self):
        editor = ConfigFile(self)
        editor.setModal(True)
        editor.exec_()
        self._groups = editor.get_config()

    def __fileChooserClicked(self):
        location, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File Location', self._previousLocation)
        if os.path.isfile(location):
            with open(location) as config_file:
                cfg = json.load(config_file)
            self._groups = cfg["groups"]
        else:
            return

        if location:
            self._previousLocation = location

    def getGroups(self):
        return self._groups

    def _loadConfig(self):
        try:
            with open(os.path.join(self._location, self._fileName), "r") as f:
                saved_settings = json.loads(f.read())
                self._groups.update(saved_settings)
        except:
            pass

    def saveConfig(self):
        with open(os.path.join(self._location, self._fileName), "w") as f:
            f.write(json.dumps(self._groups, sort_keys=False, indent=4))

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])

