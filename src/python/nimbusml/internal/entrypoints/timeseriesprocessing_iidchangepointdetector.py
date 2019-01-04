# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TimeSeriesProcessing.IidChangePointDetector
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def timeseriesprocessing_iidchangepointdetector(
        source,
        data,
        name,
        output_data=None,
        model=None,
        confidence=95.0,
        change_history_length=20,
        martingale='Power',
        power_martingale_epsilon=0.1,
        **params):
    """
    **Description**
        This transform detects the change-points in an i.i.d. sequence using
        adaptive kernel density estimation and martingales.

    :param source: The name of the source column. (inputs).
    :param data: Input dataset (inputs).
    :param name: The name of the new column. (inputs).
    :param confidence: The confidence for change point detection in
        the range [0, 100]. (inputs).
    :param change_history_length: The length of the sliding window on
        p-values for computing the martingale score. (inputs).
    :param martingale: The martingale used for scoring. (inputs).
    :param power_martingale_epsilon: The epsilon parameter for the
        Power martingale. (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'TimeSeriesProcessing.IidChangePointDetector'
    inputs = {}
    outputs = {}

    if source is not None:
        inputs['Source'] = try_set(
            obj=source,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if name is not None:
        inputs['Name'] = try_set(
            obj=name,
            none_acceptable=False,
            is_of_type=str,
            is_column=True)
    if confidence is not None:
        inputs['Confidence'] = try_set(
            obj=confidence,
            none_acceptable=False,
            is_of_type=numbers.Real)
    if change_history_length is not None:
        inputs['ChangeHistoryLength'] = try_set(
            obj=change_history_length,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if martingale is not None:
        inputs['Martingale'] = try_set(
            obj=martingale,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'None',
                'Power',
                'Mixture'])
    if power_martingale_epsilon is not None:
        inputs['PowerMartingaleEpsilon'] = try_set(
            obj=power_martingale_epsilon,
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