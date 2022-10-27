# -*- coding: utf-8 -*-
"""AiiDA-ORCA plugin -- ASA Calculations"""

from aiida.orm import SinglefileData
from aiida.common import CalcInfo, CodeInfo
from aiida.engine import CalcJob


class OrcaAsaCalculation(CalcJob):
    """OrcaAsaCalculation is a subclass of CalcJob to run
    ORCA ASA calculation which gets the asa input file and generates the
    absorption and emission spectra.
    """

    _INPUT_FILE = 'aiida.asa.inp'
    _OUTPUT_FILE = 'aiida.asa.out'

    @classmethod
    def define(cls, spec):
        super(OrcaAsaCalculation, cls).define(spec)

        spec.input(
            'input', valid_type=SinglefileData, required=True, help='ORCA asa input generated by main calculation'
        )

        # Turn mpi off by default
        spec.input('metadata.options.withmpi', valid_type=bool, default=False)

        spec.output('output_file', valid_type=SinglefileData)

    # pylint: disable = too-many-locals
    def prepare_for_submission(self, folder):

        # create code info
        codeinfo = CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.cmdline_params = [self._INPUT_FILE]

        # create calculation info
        calcinfo = CalcInfo()
        calcinfo.uuid = self.uuid
        calcinfo.codes_info = [codeinfo]
        calcinfo.retrieve_list = [self._OUTPUT_FILE]

        return calcinfo
