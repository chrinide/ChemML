from .containers import Input, Output, Parameter, req, regression_types, cv_types

class PyScript(object):
    task = 'Enter'
    subtask = 'python script'
    host = 'cheml'
    function = 'PyScript'
    modules = ('cheml','')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        iv1 = Input("iv1","input variable, of any format", ())
        iv2 = Input("iv2","input variable, of any format", ())
        iv3 = Input("iv3","input variable, of any format", ())
        iv4 = Input("iv4","input variable, of any format", ())
        iv5 = Input("iv5","input variable, of any format", ())
        iv6 = Input("iv6", "input variable, of any format", ())
    class Outputs:
        ov1 = Output("ov1","output variable, of any format", ())
        ov2 = Output("ov2","output variable, of any format", ())
        ov3 = Output("ov3","output variable, of any format", ())
        ov4 = Output("ov4","output variable, of any format", ())
        ov5 = Output("ov5","output variable, of any format", ())
        ov6 = Output("ov6", "output variable, of any format", ())
    class WParameters:
        pass
    class FParameters:
        line01 = Parameter('line01', 'type python code')
        line02 = Parameter('line02', 'input tokens are available as ...')
        line03 = Parameter('line03', '... python variables')
        line04 = Parameter('line04', 'type python code')
        line05 = Parameter('line05', 'type python code')
        line06 = Parameter('line06', 'type python code')
        line07 = Parameter('line07', 'type python code')
        line08 = Parameter('line08', 'type python code')
        line09 = Parameter('line09', 'type python code')
        line10 = Parameter('line10', 'type python code')
        line11 = Parameter('line11', 'type python code')
        line12 = Parameter('line12', 'type python code')
        line13 = Parameter('line13', 'type python code')
        line14 = Parameter('line14', 'type python code')
        line15 = Parameter('line15', 'type python code')
        line16 = Parameter('line16', 'type python code')
        line17 = Parameter('line17', 'type python code')
        line18 = Parameter('line18', 'type python code')
        line19 = Parameter('line19', 'type python code')
        line20 = Parameter('line20', 'type python code')

class RDKitFingerprint(object):
    task = 'Prepare'
    subtask = 'feature representation'
    host = 'cheml'
    function = 'RDKitFingerprint'
    modules = ('cheml','chem')
    requirements = (req(0), req(2), req(3))
    documentation = ""

    class Inputs:
        molfile = Input("molfile","the molecule file path", ("<type 'str'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        removed_rows = Output("removed_rows","output variable, of any format", ())
    class WParameters:
        pass
    class FParameters:
        FPtype = Parameter('FPtype', 'Morgan')
        vector = Parameter('vector', 'bit')
        nBits = Parameter('nBits', 1024)
        radius = Parameter('radius', 2)
        removeHs = Parameter('removeHs', True)
        molfile = Parameter('molfile', 'required_required')
        path = Parameter('path', None)
        arguments = Parameter('arguments', [])

class Dragon(object):
    task = 'Prepare'
    subtask = 'feature representation'
    host = 'cheml'
    function = 'Dragon'
    modules = ('cheml','chem')
    requirements = (req(0), req(2), req(4), req(5))
    documentation = ""

    class Inputs:
        molfile = Input("molfile","the molecule file path", ("<type 'str'>","<type 'dict'>","<type 'list'>"))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        script = Parameter('script', 'new')
    class FParameters:
        FPtype = Parameter('output_directory', './')
        script = Parameter('script', 'new')

        SaveStdOut = Parameter('SaveStdOut', False)
        DisconnectedCalculationOption = Parameter('DisconnectedCalculationOption', "'0'", format="string")
        MaxSR = Parameter('MaxSR', "'35'", format="string")
        SaveFilePath = Parameter('SaveFilePath', "Dragon_descriptors.txt")
        SaveExcludeMisMolecules = Parameter('SaveExcludeMisMolecules', False)
        SaveExcludeStdDev = Parameter('SaveExcludeStdDev', False)
        SaveExcludeNearConst = Parameter('SaveExcludeNearConst', False)
        SaveProject = Parameter('SaveProject', False)
        Add2DHydrogens = Parameter('Add2DHydrogens', False)
        blocks = Parameter('blocks',
                           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                            26, 27, 28, 29])
        SaveProjectFile = Parameter('SaveProjectFile', 'Dragon_project.drp')
        SaveOnlyData = Parameter('SaveOnlyData', False)
        MissingValue = Parameter('MissingValue', 'NaN')
        RejectDisconnectedStrucuture = Parameter('RejectDisconnectedStrucuture', False)
        SaveExclusionOptionsToVariables = Parameter('SaveExclusionOptionsToVariables', False)
        LogEdge = Parameter('LogEdge', True)
        LogPathWalk = Parameter('LogPathWalk', True)
        SaveLabelsOnSeparateFile = Parameter('SaveLabelsOnSeparateFile', False)
        version = Parameter('version', 6)
        DefaultMolFormat = Parameter('DefaultMolFormat', "'1'", format='string')
        molFile = Parameter('molFile', 'required_required')
        HelpBrowser = Parameter('HelpBrowser', "/usr/bin/xdg-open")
        SaveExcludeRejectedMolecules = Parameter('SaveExcludeRejectedMolecules', False)
        knimemode = Parameter('knimemode', False)
        RejectUnusualValence = Parameter('RejectUnusualValence', False)
        SaveStdDevThreshold = Parameter('SaveStdDevThreshold', "'0.0001'", format='string')
        SaveExcludeConst = Parameter('SaveExcludeConst', False)
        SaveFormatSubBlock = Parameter('SaveFormatSubBlock', "%b-%s-%n-%m.txt")
        Decimal_Separator = Parameter('Decimal_Separator','.')
        SaveExcludeCorrelated = Parameter('SaveExcludeCorrelated', False)
        MaxSRDetour = Parameter('MaxSRDetour', "'30'", format='string')
        consecutiveDelimiter = Parameter('consecutiveDelimiter', False)
        molInputFormat = Parameter('molInputFormat', "SMILES")
        SaveExcludeAllMisVal = Parameter('SaveExcludeAllMisVal', False)
        Weights = Parameter('Weights',
                            ['Mass', 'VdWVolume', 'Electronegativity', 'Polarizability', 'Ionization', 'I-State'])
        external = Parameter('external', False)
        RoundWeights = Parameter('RoundWeights', True)
        MaxSRforAllCircuit = Parameter('MaxSRforAllCircuit', "'19'",format="string")
        fileName = Parameter('fileName', None)
        RoundCoordinates = Parameter('RoundCoordinates', True)
        Missing_String = Parameter('Missing_String', "NaN")
        SaveExcludeMisVal = Parameter('SaveExcludeMisVal', False)
        logFile = Parameter('logFile', "Dragon_log.txt")
        RoundDescriptorValues = Parameter('RoundDescriptorValues', True)
        PreserveTemporaryProjects = Parameter('PreserveTemporaryProjects', True)
        SaveLayout = Parameter('SaveLayout', True)
        molInput = Parameter('molInput', "file")
        SaveFormatBlock = Parameter('SaveFormatBlock',"%b-%n.txt")
        SaveType = Parameter('SaveType', "singlefile")
        ShowWorksheet = Parameter('ShowWorksheet', False)
        delimiter = Parameter('delimiter',",")
        RetainBiggestFragment = Parameter('RetainBiggestFragment', False)
        CheckUpdates = Parameter('CheckUpdates', True)
        MaxAtomWalkPath = Parameter('MaxAtomWalkPath', "'2000'", format='string')
        logMode = Parameter('logMode', "file")
        SaveCorrThreshold = Parameter('SaveCorrThreshold', "'0.95'", format='string')
        SaveFile = Parameter('SaveFile', True)

class Coulomb_Matrix(object):
    task = 'Prepare'
    subtask = 'feature representation'
    host = 'cheml'
    function = 'Coulomb_Matrix'
    modules = ('cheml','chem')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        molecules = Input("molecules","the molecule numpy array or data frame", ("<class 'pandas.core.frame.DataFrame'>",
                                                                                 "<type 'numpy.ndarray'>","<type 'dict'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        CMtype = Parameter('CMtype', 'SC')
        max_n_atoms = Parameter('max_n_atoms', 'auto')
        nPerm = Parameter('nPerm', 3)
        const = Parameter('const', 1)

class Bag_of_Bonds(object):
    task = 'Prepare'
    subtask = 'feature representation'
    host = 'cheml'
    function = 'Bag_of_Bonds'
    modules = ('cheml','chem')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        molecules = Input("molecules","the molecule numpy array or data frame", ("<class 'pandas.core.frame.DataFrame'>",
                                                                                 "<type 'numpy.ndarray'>","<type 'dict'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        const = Parameter('const', 1)

class DistanceMatrix(object):
    task = 'Prepare'
    subtask = 'feature representation'
    host = 'cheml'
    function = 'DistanceMatrix'
    modules = ('cheml','chem')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        df = Input("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        norm_type = Parameter('norm_type', 'fro')
        nCores = Parameter('nCores', 1)

class MissingValues(object):
    task = 'Prepare'
    subtask = 'preprocessor'
    host = 'cheml'
    function = 'MissingValues'
    modules = ('cheml','preprocessing')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        api = Input("api","instance of ChemML's MissingValues class", ("<class 'cheml.preprocessing.handle_missing.missing_values'>",))
        df = Input("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        api = Output("api","instance of ChemML's MissingValues class", ("<class 'cheml.preprocessing.handle_missing.missing_values'>",))
    class WParameters:
        func_method = Parameter('func_method','None','String',
                        description = "",
                        options = ('fit_transform','transform', None))
    class FParameters:
        strategy = Parameter('strategy', 'ignore_row',
                             format='String',
                             options = ['interpolate','zero','ignore_row','ignore_column'])
        string_as_null = Parameter('string_as_null', True, format = 'Boolean')
        inf_as_null = Parameter('inf_as_null', True, format = 'Boolean')
        missing_values = Parameter('missing_values', False, format = 'list of strings/floats/integers')

class Merge(object):
    task = 'Prepare'
    subtask = 'basic operators'
    host = 'cheml'
    function = 'Merge'
    modules = ('cheml','initialization')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        df1 = Input("df1","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        df2 = Input("df2","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        pass

class Split(object):
    task = 'Prepare'
    subtask = 'basic operators'
    host = 'cheml'
    function = 'Split'
    modules = ('cheml','initialization')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        df = Input("df", "pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class Outputs:
        df1 = Output("df1","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        df2 = Output("df2","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        selection = Parameter('selection', 1)

class Constant(object):
    task = 'Prepare'
    subtask = 'preprocessor'
    host = 'cheml'
    function = 'Constant'
    modules = ('cheml','preprocessing')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        df = Input("df", "pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        api = Input("api", "instance of ChemML's Constant class", ("<class 'cheml.preprocessing.purge.Constant'>",))
    class Outputs:
        df = Output("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        removed_columns_ = Output("removed_columns_","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        api = Output("api","instance of ChemML's Constant class", ("<class 'cheml.preprocessing.purge.Constant'>",))
    class WParameters:
        func_method = Parameter('func_method','None','string',
                        description = "",
                        options = ('fit_transform','transform', None))
    class FParameters:
        selection = Parameter('selection', 1)

class mlp_hogwild(object):
    task = 'Model'
    subtask = 'regression'
    host = 'cheml'
    function = 'mlp_hogwild'
    modules = ('cheml','nn')
    requirements = (req(0), req(1), req(2))
    documentation = ""

    class Inputs:
        dfx = Input("dfx","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        dfy = Input("dfy", "pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        api = Input("api", "instance of ChemML's mlp_hogwild class", ("<class 'cheml.nn.nn_psgd.mlp_hogwild'>",))
    class Outputs:
        dfy_predict = Output("dfy_predict","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        api = Output("api", "instance of ChemML's mlp_hogwild class", ("<class 'cheml.nn.nn_psgd.mlp_hogwild'>",))
    class WParameters:
        func_method = Parameter('func_method','None','string',
                        description = "",
                        options = ('fit', 'predict', None))
    class FParameters:
        rms_decay = Parameter('rms_decay', 0.9)
        learn_rate = Parameter('learn_rate', 0.001)
        input_act_funcs = Parameter('input_act_funcs', '*required')
        nneurons = Parameter('nneurons', '*required')
        batch_size = Parameter('batch_size', 256)
        n_epochs = Parameter('n_epochs', 10000)
        validation_size = Parameter('validation_size', 0.2)
        print_level = Parameter('print_level', 1)
        n_hist = Parameter('n_hist', 20)
        threshold = Parameter('threshold', 0.1)
        model = Parameter('model', None)
        n_check = Parameter('n_check', 50)
        n_cores = Parameter('n_cores', 1)

class SaveFile(object):
    task = 'Store'
    subtask = 'file'
    host = 'cheml'
    function = 'SaveFile'
    modules = ('cheml','initialization')
    requirements = (req(0), req(2))
    documentation = ""

    class Inputs:
        df = Input("df","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class Outputs:
        filepath = Output("filepath","pandas dataframe", ("<type 'str'>",))
    class WParameters:
        pass
    class FParameters:
        index = Parameter('index', False)
        record_time = Parameter('record_time', False)
        format = Parameter('format', 'csv')
        output_directory = Parameter('output_directory', None)
        header = Parameter('header', True)
        filename = Parameter('filename', 'required_required')

class XYZreader(object):
    task = 'Enter'
    subtask = 'xyz'
    host = 'cheml'
    function = 'XYZreader'
    modules = ('cheml','initialization')
    requirements = (req(0),)
    documentation = ""

    class Inputs:
        pass
    class Outputs:
        molecules = Output("molecules","dictionary of molecules with ['mol', 'file'] keys",
                           ("<type 'dict'>",))

    class WParameters:
        pass
    class FParameters:
        path_pattern = Parameter('path_pattern', 'required_required')
        path_root = Parameter('path_root', None)
        Z = Parameter('Z', {'Ru': 44.0, 'Re': 75.0, 'Rf': 104.0, 'Rg': 111.0, 'Ra': 88.0, 'Rb': 37.0, 'Rn': 86.0, 'Rh': 45.0, 'Be': 4.0, 'Ba': 56.0, 'Bh': 107.0, 'Bi': 83.0, 'Bk': 97.0, 'Br': 35.0, 'H': 1.0, 'P': 15.0, 'Os': 76.0, 'Es': 99.0, 'Hg': 80.0, 'Ge': 32.0, 'Gd': 64.0, 'Ga': 31.0, 'Pr': 59.0, 'Pt': 78.0, 'Pu': 94.0, 'C': 6.0, 'Pb': 82.0, 'Pa': 91.0, 'Pd': 46.0, 'Cd': 48.0, 'Po': 84.0, 'Pm': 61.0, 'Hs': 108.0, 'Uup': 115.0, 'Uus': 117.0, 'Uuo': 118.0, 'Ho': 67.0, 'Hf': 72.0, 'K': 19.0, 'He': 2.0, 'Md': 101.0, 'Mg': 12.0, 'Mo': 42.0, 'Mn': 25.0, 'O': 8.0, 'Mt': 109.0, 'S': 16.0, 'W': 74.0, 'Zn': 30.0, 'Eu': 63.0, 'Zr': 40.0, 'Er': 68.0, 'Ni': 28.0, 'No': 102.0, 'Na': 11.0, 'Nb': 41.0, 'Nd': 60.0, 'Ne': 10.0, 'Np': 93.0, 'Fr': 87.0, 'Fe': 26.0, 'Fl': 114.0, 'Fm': 100.0, 'B': 5.0, 'F': 9.0, 'Sr': 38.0, 'N': 7.0, 'Kr': 36.0, 'Si': 14.0, 'Sn': 50.0, 'Sm': 62.0, 'V': 23.0, 'Sc': 21.0, 'Sb': 51.0, 'Sg': 106.0, 'Se': 34.0, 'Co': 27.0, 'Cn': 112.0, 'Cm': 96.0, 'Cl': 17.0, 'Ca': 20.0, 'Cf': 98.0, 'Ce': 58.0, 'Xe': 54.0, 'Lu': 71.0, 'Cs': 55.0, 'Cr': 24.0, 'Cu': 29.0, 'La': 57.0, 'Li': 3.0, 'Lv': 116.0, 'Tl': 81.0, 'Tm': 69.0, 'Lr': 103.0, 'Th': 90.0, 'Ti': 22.0, 'Te': 52.0, 'Tb': 65.0, 'Tc': 43.0, 'Ta': 73.0, 'Yb': 70.0, 'Db': 105.0, 'Dy': 66.0, 'Ds': 110.0, 'I': 53.0, 'U': 92.0, 'Y': 39.0, 'Ac': 89.0, 'Ag': 47.0, 'Uut': 113.0, 'Ir': 77.0, 'Am': 95.0, 'Al': 13.0, 'As': 33.0, 'Ar': 18.0, 'Au': 79.0, 'At': 85.0, 'In': 49.0})
        reader = Parameter('reader', 'auto')
        skip_lines = Parameter('skip_lines', [2,0])

class ConvertFile(object):
    task = 'Enter'
    subtask = 'Convert'
    host = 'cheml'
    function ='ConvertFile'
    modules = ('cheml','initialization')
    requirements = (req(0),req(6),)
    documentation = "https://openbabel.org/wiki/Babel"

    class Inputs:
        file_path=Input("file_path","the path to the file that needs to be conferted",("<type 'str'>","<type 'dict'>"))
    class Outputs:
        converted_file_paths = Output("converted_file_paths", "list of paths to the converted files", "<type 'list'>")
    class WParameters:
        pass
    class FParameters:
        file_path = Parameter('file_path', 'required_required')
        from_format = Parameter('from_format', 'required_required')
        to_format = Parameter('to_format', 'required_required')

class load_cep_homo(object):
    task = 'Enter'
    subtask = 'datasets'
    host = 'cheml'
    function = 'load_cep_homo'
    modules = ('cheml','datasets')
    requirements = (req(0),req(2))
    documentation = ""

    class Inputs:
        pass
    class Outputs:
        smiles = Output("smiles","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        homo = Output("homo","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        pass

class load_organic_density(object):
    task = 'Enter'
    subtask = 'datasets'
    host = 'cheml'
    function = 'load_organic_density'
    modules = ('cheml','datasets')
    requirements = (req(0),req(2))
    documentation = ""

    class Inputs:
        pass
    class Outputs:
        smiles = Output("smiles","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        density = Output("density","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
        features = Output("features","pandas dataframe", ("<class 'pandas.core.frame.DataFrame'>",))
    class WParameters:
        pass
    class FParameters:
        pass

