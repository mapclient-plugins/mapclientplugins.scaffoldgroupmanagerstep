"""
MAP Client Plugin Step
"""
import os
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.scaffoldgroupmanagerstep.configuredialog import ConfigureDialog

from opencmiss.zinc.context import Context
from opencmiss.zinc.element import Element
from opencmiss.zinc.field import Field, FieldGroup
from opencmiss.zinc.result import RESULT_OK
from opencmiss.utils.zinc.general import ChangeManager


class ScaffoldGroupManager(object):

    def __init__(self, input_scaffold_file, groups):
        self._context = Context('ScaffoldGroupManager')
        self._region = self._context.createRegion()
        self._region.setName('GroupManagerRegion')
        self._field_module = self._region.getFieldmodule()
        self._scaffold_file = input_scaffold_file
        self._model_coordinates_field = None
        self._output_filename = None
        self._groups = groups

        self._load()
        for group in groups["groups"]:
            self._manage_groups(group)

    def _discover_coordinate_fields(self):
        field = None
        if self._model_coordinates_field:
            field = self._field_module.findFieldByName(self._model_coordinates_field)
        else:
            mesh = self._get_highest_dimension_mesh()
            element = mesh.createElementiterator().next()
            if element.isValid():
                field_cache = self._field_module.createFieldcache()
                field_cache.setElement(element)
                fielditer = self._field_module.createFielditerator()
                field = fielditer.next()
                while field.isValid():
                    if field.isTypeCoordinate() and (field.getNumberOfComponents() == 3) \
                            and (field.castFiniteElement().isValid()):
                        if field.isDefinedAtLocation(field_cache):
                            break
                    field = fielditer.next()
                else:
                    field = None
        if field:
            self._set_model_coordinates_field(field)

    def _get_highest_dimension_mesh(self):
        for d in range(2, -1, -1):
            mesh = self._mesh[d]
            if mesh.getSize() > 0:
                return mesh
        return None

    def get_output_file_name(self):
        return self._output_filename

    def _load(self):
        result = self._region.readFile(self._scaffold_file)
        assert result == RESULT_OK, "Failed to load model file" + str(self._scaffold_file)
        self._mesh = [self._field_module.findMeshByDimension(d + 1) for d in range(3)]
        self._discover_coordinate_fields()

    def _manage_groups(self, group):
        with ChangeManager(self._field_module):
            print(group)
            term_group = self._field_module.findFieldByName(group).castGroup()
            term_group.setSubelementHandlingMode(FieldGroup.SUBELEMENT_HANDLING_MODE_FULL)
            mesh2d = self._field_module.findMeshByDimension(2)
            term_face_group = term_group.getFieldElementGroup(mesh2d)
            if not term_face_group.isValid():
                term_face_group = term_group.createFieldElementGroup(mesh2d)
            term_mesh_group = term_face_group.getMeshGroup()
            is_exterior = self._field_module.createFieldIsExterior()
            is_endo = self._field_module.createFieldAnd(is_exterior, self._field_module.createFieldIsOnFace(Element.FACE_TYPE_XI3_0))

            tmp_element_group = self._field_module.createFieldElementGroup(mesh2d)
            tmp_mesh_group = tmp_element_group.getMeshGroup()
            tmp_mesh_group.addElementsConditional(self._field_module.createFieldAnd(term_face_group, is_endo))
            term_group.clear()
            term_mesh_group.addElementsConditional(tmp_element_group)
            # delete any temporary fields
            del tmp_element_group
            del tmp_mesh_group
            del is_endo
            filename = os.path.basename(self._scaffold_file).split('.')[0] + '_regrouped.exf'
            path = os.path.dirname(self._scaffold_file)
            self._output_filename = os.path.join(path, filename)
            self._region.writeFile(self._output_filename)

    def _set_model_coordinates_field(self, model_coordinates_field: Field):
        finite_element_field = model_coordinates_field.castFiniteElement()
        assert finite_element_field.isValid() and (finite_element_field.getNumberOfComponents() == 3)
        self._model_coordinates_field = finite_element_field


class ScaffoldGroupManagerStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(ScaffoldGroupManagerStep, self).__init__('Scaffold Group Manager', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Utility'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/scaffoldgroupmanagerstep/images/utility.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Port data:
        self._port0_input_file = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port1_output_file = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._scaffold_group_manager = None
        self._groups = {}

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.

        if len(self._groups) == 0 and os.path.isfile(os.path.join(self._location, 'groups.config')):
            with open(os.path.join(self._location, 'groups.config'), "r") as f:
                saved_settings = json.loads(f.read())
                self._groups.update(saved_settings)

        self._scaffold_group_manager = ScaffoldGroupManager(self._port0_input_file, self._groups)
        self._port1_output_file = self._scaffold_group_manager.get_output_file_name()
        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        self._port0_input_file = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        return self._port1_output_file  # <not-set>

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """

        dlg = ConfigureDialog(self._location, self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()
        self._groups = dlg.getGroups()
        dlg.saveConfig()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
