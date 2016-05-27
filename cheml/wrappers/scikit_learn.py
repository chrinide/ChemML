import warnings

class sklearn_Base(object):
    """
    Do not instantiate this class
    """
    def __init__(self, Base,parameters,iblock):
        self.Base = Base
        self.parameters = parameters
        self.iblock = iblock

    def run(self):
        self.legal_IO()
        self.receive()
        self.fit()
        self.send()

    def receive(self):
        recv = [edge for edge in self.Base.graph if edge[2] == self.iblock]
        self.Base.graph = [edge for edge in self.Base.graph if edge[2] != self.iblock]
        # check received tokens
        count = [0] * len(self.legal_inputs)
        for edge in recv:
            if edge[3] in self.legal_inputs:
                ind = self.legal_inputs.index(edge[2])
                count[ind] += 1
                if count[ind] > 1:
                    msg = '@function #%i: only one input per each available input can be received.'%self.iblock + 1
                    raise IOError(msg)
            else:
                msg = "@function #%i: received a non valid input token '%s', sent by function #%i" % (self.iblock + 1, edge[3], edge[0] + 1)
                raise IOError(msg)
        for edge in recv:
            key = edge[0:2]
            if key in self.Base.send:
                value = self.Base.send[key][0]
                self.legal_inputs[edge[3]] = value
                self.Base.send[key][1] -= 1
                if self.Base.send[key][1] == 0:
                    del self.Base.send[key]
            else:
                msg = '@function #%i: broken pipe in edge %s - nothing has been sent' % (self.iblock + 1, str(edge))
                raise IOError(msg)
        return self.legal_inputs

    def send(self):
        send = [edge for edge in self.Base.graph if edge[0]==self.iblock]
        for edge in send:
            key = edge[0:1]
            if key in self.Base.send:
                self.Base.send[key][1] += 1
            else:
                self.Base.send[key] = [self.legal_outputs[edge[1]],1]

    def Imputer_dataframe(self, transformer, df):
        """ keep track of features (columns) that can be removed or changed in the
            Imputer by transforming data back to pandas dataframe structure. This happens based on
            the "statistics_" attribute of Imputer.

        Parameters
        ----------
        transformer: sklearn Imputer class
             The class with adjusted parameters.

        df: Pandas dataframe
            The dataframe that imputer is going to deal with.

        Returns
        -------
        transformed data frame
        fitted imputer class
        """
        df_columns = list(df.columns)
        df = transformer.fit_transform(df)
        if df.shape[1] == 0:
            warnings.warn("empty dataframe: all columns have been removed",Warning)
            return transformer, df
        else:
            stats = transformer.statistics_
            nan_ind = [i for i,val in enumerate(stats) if np.isnan(val)]
            df_columns = list_del_indices(df_columns, nan_ind)
            df = pd.DataFrame(df,columns=df_columns)
            return df

    def Transformer_ManipulateHeader(self, transformer, df):
        """ keep track of features (columns) that can be removed or changed in the
            Scaler by transforming data back to pandas dataframe structure.

        Parameters
        ----------
        scaler: sklearn Scaler class
            The class with adjusted parameters.

        df: Pandas dataframe
            The dataframe that scaler is going to deal with.

        Returns
        -------
        transformed data frame
        fitted scaler class

        """
        df_columns = list(df.columns)
        df = transformer.fit_transform(df)
        if df.shape[1] == 0:
            warnings.warn("@function #%i: empty dataframe - all columns have been removed"%self.iblock+1,Warning)
        if df.shape[1] == len(df_columns):
            df = pd.DataFrame(df,columns=df_columns)
        else:
            df = pd.DataFrame(df)
            warnings.warn("@function #%i: headers untrackable - number of columns before and after transform doesn't match"%self.iblock+1,Warning)
        return df

    def selector_dataframe(self, transformer, df, tf):
        """ keep track of features (columns) that can be removed or changed in the
            VarianceThreshold by transforming data back to pandas dataframe structure.
            This happens based on the "get_support" method of selector.

        Parameters
        ----------
        imputer: sklearn VarianceThreshold class
             The class with adjusted parameters.

        df: Pandas dataframe
            data frame

        tf: Pandas dataframe
            target frame

        Returns
        -------
        transformed data frame
        fitted imputer class
        """
        df_columns = list(df.columns)
        df = transformer.fit_transform(df,tf)
        if df.shape[1] == 0:
            warnings.warn("empty dataframe: all columns have been removed",Warning)
            return transformer, df
        else:
            retained_features_ind = sel.get_support(True)
            df_columns = [df_columns[i] for i in retained_features_ind]
            df = pd.DataFrame(df,columns=df_columns)
            return df


class StandardScaler(sklearn_Base):
    def legal_IO(self):
        self.legal_inputs = {'df': None}
        self.legal_outputs = {'SS_skl_api':None, 'df':None}
        self.Base.requirements.append('scikit_learn')

    def fit(self):
        from sklearn.preprocessing import StandardScaler
        try:
            model = StandardScaler(**self.parameters)
        except Exception as err:
            msg = '@function #%i: '%iblock + type(err).__name__ + ': '+ err.message
            raise TypeError(msg)
        order = [edge[1] for edge in self.Base.graph if edge[0]==self.iblock]
        for token in order:
            if token == 'SS_skl_api':
                self.legal_outputs[token] = model
            elif token == 'df':
                self.legal_outputs[token] = self.Transformer_ManipulateHeader(model, self.legal_inputs['df'])
            else:
                msg = "@function #%i: non valid output token '%s'" % (self.iblock + 1, token)
                raise NameError(msg)

