import pandas as pd

from ..base import BASE

##################################################################### 1 Enter Data

# input

class read_table(BASE):
    def fit(self):
        # step1: check inputs
        # step2: assign inputs to parameters if necessary (param = @token)
        self.paramFROMinput()
        # step3: check the dimension of input data frame
        # step4: import module and make APIs
        try:
            df = pd.read_table(**self.parameters)
        except Exception as err:
            msg = '@Task #%i(%s): '%(self.iblock+1, self.Task) + type(err).__name__ + ': '+ err.message
            raise TypeError(msg)

        # step5: process
        print '(rows, columns): ', df.shape
        # if 'header' in self.parameters and self.parameters['header'] is not None:
        #     print 'headers: ', list(df.columns)

        # step6: send out
        order = [edge[1] for edge in self.Base.graph if edge[0]==self.iblock]
        for token in set(order):
            if token not in self.outputs:
                msg = "@Task #%i(%s): not a valid output token '%s'" % (self.iblock + 1, self.Task, token)
                raise NameError(msg)
            elif token == 'df':
                self.set_value(token, df)
                self.outputs[token].count = order.count(token)
                self.Base.send[(self.iblock, token)] = self.outputs[token]


        # step7: delete all inputs from memory
        del self.inputs

class read_excel(BASE):
    def fit(self):
        # step1: check inputs
        # step2: assign inputs to parameters if necessary (param = @token)
        self.paramFROMinput()
        # step3: check the dimension of input data frame
        # step4: import module and make APIs
        try:
            df = pd.read_excel(**self.parameters)
        except Exception as err:
            msg = '@Task #%i(%s): '%(self.iblock+1, self.Task) + type(err).__name__ + ': '+ err.message
            raise TypeError(msg)

        # step5: process
        print '(rows, columns): ', df.shape
        # if 'header' in self.parameters and self.parameters['header'] is not None:
        #     print 'header: ', df.columns

        # step6: send out
        order = [edge[1] for edge in self.Base.graph if edge[0]==self.iblock]
        for token in set(order):
            if token not in self.outputs:
                msg = "@Task #%i(%s): not a valid output token '%s'" % (self.iblock + 1, self.Task, token)
                raise NameError(msg)
            elif token == 'df':
                self.set_value(token, df)
                self.outputs[token].count = order.count(token)
                self.Base.send[(self.iblock, token)] = self.outputs[token]

        # step7: delete all inputs from memory
        del self.inputs



# Search
class corr(BASE):
    def fit(self):
        # step1: check inputs
        self.required('df', True)
        df = self.inputs['df'].value
        # step2: assign inputs to parameters if necessary (param = @token)
        self.paramFROMinput()
        # step3: check the dimension of input data frame
        # step4: import module and make APIs
        try:
            df_out = df.corr(**self.parameters)
        except Exception as err:
            msg = '@Task #%i(%s): '%(self.iblock+1, self.Task) + type(err).__name__ + ': '+ err.message
            raise TypeError(msg)

        # step5: process
        # step6: send out
        order = [edge[1] for edge in self.Base.graph if edge[0]==self.iblock]
        for token in set(order):
            if token not in self.outputs:
                msg = "@Task #%i(%s): not a valid output token '%s'" % (self.iblock + 1, self.Task, token)
                raise NameError(msg)
            elif token == 'df':
                self.set_value(token, df_out)
                self.outputs[token].count = order.count(token)
                self.Base.send[(self.iblock, token)] = self.outputs[token]

        # step7: delete all inputs from memory
        del self.inputs
