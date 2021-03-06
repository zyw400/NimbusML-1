# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.FeatureSelectorByMutualInformation
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_featureselectorbymutualinformation(
        column,
        data,
        output_data=None,
        model=None,
        slots_in_output=1000,
        label_column='Label',
        num_bins=256,
        **params):
    """
    **Description**
        Selects the top k slots across all specified columns ordered by their
        mutual information with the label column.

    :param column: Columns to use for feature selection (inputs).
    :param slots_in_output: The maximum number of slots to preserve
        in output (inputs).
    :param data: Input dataset (inputs).
    :param label_column: Column to use for labels (inputs).
    :param num_bins: Max number of bins for R4/R8 columns, power of 2
        recommended (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.FeatureSelectorByMutualInformation'
    inputs = {}
    outputs = {}

    if column is not None:
        inputs['Column'] = try_set(
            obj=column,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if slots_in_output is not None:
        inputs['SlotsInOutput'] = try_set(
            obj=slots_in_output,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if label_column is not None:
        inputs['LabelColumn'] = try_set(
            obj=label_column,
            none_acceptable=True,
            is_of_type=str,
            is_column=True)
    if num_bins is not None:
        inputs['NumBins'] = try_set(
            obj=num_bins,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
